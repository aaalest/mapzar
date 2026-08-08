from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    telegram_id = fields.BigIntField(unique=True, index=True)
    username = fields.CharField(max_length=255, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    stalls: fields.ReverseRelation["Stall"]

    class Meta:
        table = "users"

    def __str__(self) -> str:
        return f"User({self.telegram_id}, {self.username})"

    async def is_seller(self) -> bool:
        return await self.stalls.all().count() > 0


class Stall(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    category = fields.CharField(max_length=100)
    is_active = fields.BooleanField(default=True)
    seller = fields.ForeignKeyField("models.User", related_name="stalls")

    class Meta:
        table = "stalls"

    def __str__(self) -> str:
        return f"Stall({self.title}, {self.category})"