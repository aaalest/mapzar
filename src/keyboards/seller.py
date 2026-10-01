from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.callbacks import CategoryCallback
from keyboards.categories_data import resolve_category_path
from models.category import Category
from enum import Enum, auto


class CategoryAction(str, Enum):
    OPEN = "open"
    TOGGLE = "toggle"
    BACK = "back"
    DONE = "done"



def get_categories_keyboard(
    path_ids: list[str], selected_ids: set[str]
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    node = resolve_category_path(path_ids)
    buttons = []
    for child in node.children:
        if child.is_leaf:
            is_checked = child.id in selected_ids
            prefix = "✅ " if is_checked else ""
            text = f"{prefix}{child.name}"
            action = CategoryAction.TOGGLE
        else:
            text = child.name
            action = CategoryAction.OPEN

        builder.button(
            text=text,
            callback_data=CategoryCallback(
                action=action,
                target=child.id
            ).pack(),
        )
        buttons.append(1)

    # Bottom Actions: Back & Done
    if path_ids:
        builder.button(
            text="◀️ Назад",
            callback_data=CategoryCallback(action=CategoryAction.BACK).pack(),
        )

    count = f" ({len(selected_ids)})" if selected_ids else ""
    builder.button(
        text=f"✅ Готово{count}",
        callback_data=CategoryCallback(action=CategoryAction.DONE).pack(),
    )

    buttons.append(2)
    builder.adjust(*buttons)

    return builder.as_markup()

