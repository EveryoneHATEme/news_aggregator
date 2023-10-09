import asyncio
from telethon.tl.types import Message, MessageEntityTextUrl
from datasets.client import client, get_post_text
from .database import create_table, connection, insert_duplicates, get_min_label, to_csv


async def parse_nyan():
    create_table()
    async with client:
        channel = await client.get_entity("https://t.me/nyannews")
        messages = await client.iter_messages(channel, max_id=get_min_label()).collect()
        await asyncio.gather(*[parse_post(msg) for msg in messages])
        to_csv("out.csv")


async def parse_post(msg: Message):
    label = msg.id
    if not msg.entities or msg.pinned:
        return
    urls = list(
        {
            entity.url
            for entity in msg.entities
            if isinstance(entity, MessageEntityTextUrl)
            and "t.me" in entity.url
            and "nyannews" not in entity.url
        }
    )
    if not urls:
        return
    values = [
        (post[0], post[1], label)
        for post in await asyncio.gather(*[get_post_text(url) for url in urls])
        if post and post[1].strip()
    ]
    insert_duplicates(values)
    connection.commit()
    print(label)
