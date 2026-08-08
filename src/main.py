import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from config import settings
from db.session import close_db, init_db
from handlers import common

async def main():
    # Configure logging output for PyCharm console
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    # Initialize Bot & Dispatcher
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()

    # Register Routers
    dp.include_router(common.router)

    # Startup: Initialize Database Pool
    await init_db()
    logging.info("Database initialized successfully.")

    try:
        logging.info("Starting bot polling...")
        # await bot.delete_webhook(drop_pending_updates=True)  # Drop pending updates so old messages sent while bot was off are ignored
        await dp.start_polling(bot)
    finally:
        # Shutdown: Gracefully release database connections
        await close_db()
        logging.info("Database connections closed.")


if __name__ == "__main__":
    asyncio.run(main())