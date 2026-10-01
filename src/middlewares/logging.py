import logging
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject
from aiogram.fsm.context import FSMContext


logger = logging.getLogger("mapzar.events")


async def _get_current_state(data: Dict[str, Any]) -> str | None:
    state: FSMContext = data.get("state")
    return await state.get_state() if state else None


def _format_user_info(user) -> str:
    if not user:
        return "id=unknown"
    return f"@{user.username}" if user.username else f"id={user.id}"


class EventLoggingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        current_state = await _get_current_state(data)
        user_info = _format_user_info(event.from_user)

        if isinstance(event, Message):
            text = event.text or event.caption or f"[{event.content_type}]"
            logger.info(f"📩 MESSAGE from {user_info}: {text}, state: {current_state}")

        elif isinstance(event, CallbackQuery):
            button_data = event.data
            logger.info(f"🔘 BUTTON CLICK from {user_info}: data='{button_data}', state: {current_state}")

        return await handler(event, data)
