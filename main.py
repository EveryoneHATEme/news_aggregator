import asyncio
from bot.bot import dp, bot

asyncio.run(dp.start_polling(bot))
