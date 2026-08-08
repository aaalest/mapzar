from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_onboarding_keyboard(stall_count: int = 0) -> InlineKeyboardMarkup:
    view_stalls_btn = InlineKeyboardButton(
        text="🗺️ Переглянути точки",
        callback_data="view_stalls"
    )

    if stall_count > 0:
        seller_btn = InlineKeyboardButton(
            text=f"⚙️ Мої точки ({stall_count})",
            callback_data="manage_stalls"
        )
    else:
        seller_btn = InlineKeyboardButton(
            text="🏪 Зареєструвати точку",
            callback_data="register_stall"
        )

    return InlineKeyboardMarkup(inline_keyboard=[[view_stalls_btn], [seller_btn]])
