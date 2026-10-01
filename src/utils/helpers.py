from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, Message
from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, Message


async def safe_delete_message(message: Message | None) -> bool:
    """Safely deletes a message, ignoring errors if it's already deleted or too old."""
    if not message:
        return False
    try:
        await message.delete()
        return True
    except TelegramBadRequest:
        return False


async def edit_or_send_message(
    bot: Bot,
    message: Message,
    state: FSMContext,
    text: str,
    reply_markup: InlineKeyboardMarkup | None = None,
    parse_mode: str = "HTML",
) -> Message:
    """Edits the existing menu message if possible; otherwise sends a new one and updates FSM state."""
    data = await state.get_data()
    target_message_id = message.message_id if message.from_user and message.from_user.is_bot else data.get("menu_message_id")

    if target_message_id:
        try:
            result = await bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=target_message_id,
                text=text,
                reply_markup=reply_markup,
                parse_mode=parse_mode,
            )
            # Satisfy the type checker since edit_message_text can technically return a bool
            if isinstance(result, Message):
                return result
        except TelegramBadRequest:
            # Fallback triggered if message was deleted or content is identical
            pass

    # Send a new message if editing failed or no target_message_id existed
    new_msg = await message.answer(
        text=text,
        reply_markup=reply_markup,
        parse_mode=parse_mode,
    )
    await state.update_data(menu_message_id=new_msg.message_id)
    return new_msg


async def get_valid_callback_message(
    callback: CallbackQuery,
    alert_text: str = "Повідомлення застаріло або недоступне."
) -> Message | None:
    """Ensures callback.message is a valid regular Message.
    Otherwise, answers the callback with an alert and returns None.
    """
    if not isinstance(callback.message, Message):
        await callback.answer(alert_text, show_alert=True)
        return None
    return callback.message
