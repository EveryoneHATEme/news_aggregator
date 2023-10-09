import asyncio
from datasets.duplicates.nyan import parse_nyan
from datasets.categories.parse import parse_all


async def main():
    await parse_all()


asyncio.run(main())
