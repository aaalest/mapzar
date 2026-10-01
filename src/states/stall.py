from aiogram.fsm.state import State, StatesGroup


class StallRegistration(StatesGroup):
    title = State()     # Waiting for user to send spot title/number
    category = State()  # Waiting for user to select a category