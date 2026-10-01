from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from db.models import User
from keyboards.onboarding import get_onboarding_keyboard

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    if not message.from_user:
        return

    # 1. Get or create user in database
    user, _ = await User.get_or_create(
        telegram_id=message.from_user.id,
        defaults={"username": message.from_user.username},
    )

    # 2. Check seller state via ReverseRelation
    stall_count = await user.stalls.all().count()

    welcome_text = (
        "<b>MapZar - мапа торгових точок Варшавського ринку</b>\n\n"
        "Шукайте точки на карті або додайте свою точку, щоб покупці могли вас знайти.\n\n"
        "<i>Що саме ви б хотіли зробити?</i>"
    )

    sent_message = await message.answer(
        text=welcome_text,
        parse_mode=ParseMode.HTML,
        reply_markup=get_onboarding_keyboard(stall_count=stall_count),
    )
    await state.update_data(menu_message_id=sent_message.message_id)
