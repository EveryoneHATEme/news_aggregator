import asyncio
import torch
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandStart
from aiogram.enums.parse_mode import ParseMode
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from settings import settings

from sentence_transformers import SentenceTransformer, util
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
classifier_model = AutoModelForSequenceClassification.from_pretrained("./model")
sentence_model = SentenceTransformer("./model_output", device="cpu")

from functools import reduce

from datasets.client import client
from datasets.categories.parse import get_messages_from_channel
from datasets.categories.channels import channels


bot = Bot(settings.TG_TOKEN)
dp = Dispatcher()

update_keyboard = ReplyKeyboardBuilder().button(text="🔁 Update").as_markup()


def predict_category(text: str) -> str:
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        logits = classifier_model(**inputs).logits
        predicted_class_id = logits.argmax().item()
        return classifier_model.config.id2label[predicted_class_id]


async def run_update() -> list[str]:
    async with client:
        messages = reduce(
            lambda prev, curr: prev + curr,
            await asyncio.gather(
                *[
                    get_messages_from_channel(channel)
                    for _, channels_list in channels.items()
                    for channel in channels_list
                ]
            ),
            [],
        )

    print(messages)

    by_category = {}

    for message in messages:
        if not message or not message.strip():
            continue
        category = predict_category(text=message)
        if category not in by_category:
            by_category[category] = []
        by_category[category].append(message)

    texts = {}

    for category in by_category:
        duplicates = {}
        embeddings = sentence_model.encode(
            by_category[category], convert_to_tensor=True
        )
        cosine_scores = util.cos_sim(embeddings, embeddings)

        for i in range(len(cosine_scores) - 1):
            for j in range(i + 1, len(cosine_scores)):
                if cosine_scores[i][j] >= 0.5:
                    for key in duplicates:
                        if key in duplicates[key]:
                            continue
                    if i not in duplicates:
                        duplicates[i] = set()
                    duplicates[i].add(j)
        texts[category] = [by_category[category][key] for key in duplicates.keys()]

    return [
        f"Category: **{category.capitalize()}**\n{text}"
        for category in texts
        for text in texts[category]
    ]


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "Hola! This is a bot for parsing news from random channels. Press 🔁 Update button when you want to update news. Parsing in progres...",
        reply_markup=update_keyboard,
    )
    for msg in await run_update():
        await message.answer(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message(F.text.contains("date"))
async def update_handler(message: types.Message):
    await message.answer(
        "Update started. Press 🔁 Update whenever you want to update news"
    )
    for msg in await run_update():
        await message.answer(msg, parse_mode=ParseMode.MARKDOWN)
