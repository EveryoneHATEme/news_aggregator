from telethon import TelegramClient

from settings import settings
from .sanitizing import preprocess_text

client = TelegramClient(
    "datasets",
    settings.TG_API_ID,
    settings.TG_API_HASH,
    device_model="Linux 5.15.0",
    system_version="Ubuntu 20.04.6 LTS",
)
client.session.save()


async def get_post_text(url: str) -> tuple[int, str]:
    channel_url, message_id = url.rsplit("/", maxsplit=1)
    message_id = int(message_id)
    async for message in client.iter_messages(
        await client.get_entity(channel_url),
        min_id=message_id - 1,
        max_id=message_id + 1,
    ):
        return message_id, preprocess_text(message.message)
