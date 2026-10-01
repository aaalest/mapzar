from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from enum import Enum, auto


class StartAction(str, Enum):
    VIEW_STALLS = "view_stalls"
    MANAGE_STALLS = "manage_stalls"
    REGISTER_STALL = "register_stall"


def get_onboarding_keyboard(stall_count: int = 0) -> InlineKeyboardMarkup:
    view_stalls_btn = InlineKeyboardButton(
        text="🗺️ Переглянути точки",
        callback_data=StartAction.VIEW_STALLS
    )

    if stall_count > 0:
        seller_btn = InlineKeyboardButton(
            text=f"⚙️ Мої точки ({stall_count})",
            callback_data=StartAction.MANAGE_STALLS
        )
    else:
        seller_btn = InlineKeyboardButton(
            text="🏪 Зареєструвати точку",
            callback_data=StartAction.REGISTER_STALL
        )

    return InlineKeyboardMarkup(inline_keyboard=[[view_stalls_btn], [seller_btn]])
