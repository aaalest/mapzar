from tortoise import Tortoise
from config import settings

# Aerich migration tool reads this dictionary
TORTOISE_ORM = {
    "connections": {
        "default": settings.database_url,  # Reads "sqlite://mapzar.db" or "postgres://..."
    },
    "apps": {
        "models": {
            "models": ["db.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}


async def init_db():
    await Tortoise.init(config=TORTOISE_ORM)
    # Auto-generate schemas for local dev if they don't exist yet
    await Tortoise.generate_schemas(safe=True)


async def close_db():
    await Tortoise.close_connections()