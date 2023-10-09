import asyncio
from datasets.client import client
from datasets.sanitizing import preprocess_text
from common.categories import Categories
from .output import write_data, category_exists
from .channels import channels


async def parse_from_channel(url: str) -> list[str]:
    channel = await client.get_entity(url)
    messages = await client.iter_messages(channel, limit=500).collect()
    return [
        text
        for text in [preprocess_text(msg.message) for msg in messages]
        if text.strip()
    ]


async def parse_and_save(urls: list[str], category: Categories):
    if not category_exists(category):
        rows = []
        for texts in await asyncio.gather(*[parse_from_channel(url) for url in urls]):
            rows += texts
        write_data(rows, category)
    else:
        print(f"{category.name} exists")


async def parse_all():
    async with client:
        await asyncio.gather(
            *[parse_and_save(value, key) for key, value in channels.items()]
        )
