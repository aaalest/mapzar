import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis
import sys
import os

from middlewares.logging import EventLoggingMiddleware
from handlers import common, seller
from config import settings
from db.session import close_db, init_db


async def main():
    # Configure logging output for PyCharm console
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        stream=sys.stdout
    )

    # 1. Ensure the data directory exists
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
    os.makedirs(data_dir, exist_ok=True)

    # 2. Spawn redis-server
    redis_process = await asyncio.create_subprocess_exec(
        "redis-server",
        "--port", "6379",
        "--dir", data_dir,
        "--appendonly", "yes",
        "--appendfsync", "everysec",
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL,
    )
    await asyncio.sleep(0.2)

    # 3. Connect to Redis
    redis_client = Redis.from_url("redis://localhost:6379/0")
    storage = RedisStorage(redis=redis_client)

    # 4. Initialize Bot & Dispatcher
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher(storage=storage)

    # Register middleware for both messages and button clicks
    dp.message.outer_middleware(EventLoggingMiddleware())
    dp.callback_query.outer_middleware(EventLoggingMiddleware())

    # Register Routers
    dp.include_router(common.router)
    dp.include_router(seller.router)

    # Startup: Initialize Database Pool
    await init_db()
    logging.info("Database initialized successfully.")

    try:
        logging.info("Starting bot polling...")
        await dp.start_polling(bot)
    finally:
        # 5. Graceful cleanup on stop/restart
        await close_db()
        await redis_client.aclose()
        redis_process.terminate()
        await redis_process.wait()
        logging.info("Database, Redis process, and connections closed.")


if __name__ == "__main__":
    asyncio.run(main())
