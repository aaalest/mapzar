from aiogram.filters.callback_data import CallbackData


class CategoryCallback(CallbackData, prefix="cat"):
    action: str  # "open", "toggle", "back", "done"
    target: str = ""  # Category English ID (e.g. "fresh_veg")
