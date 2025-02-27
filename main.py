import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from app.user import user_router
from app.database.db import init_db


async def main():
    await init_db()
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(user_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try: 
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
