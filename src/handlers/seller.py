from aiogram import Bot, F, Router, types
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from src.keyboards.onboarding import StartAction

from db.models import Stall, User
from keyboards.callbacks import CategoryCallback
from keyboards.categories_data import get_category_by_id
from keyboards.seller import get_categories_keyboard, CategoryAction
from states.stall import StallRegistration
from utils.helpers import safe_delete_message, edit_or_send_message, get_valid_callback_message


router = Router()


# 1. When user triggers registration, send or edit menu & store its ID
@router.callback_query(F.data == StartAction.REGISTER_STALL)
async def start_reg(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    trigger_message = await get_valid_callback_message(callback)
    if not trigger_message:
        return

    response_message = await edit_or_send_message(
        bot, trigger_message, state,
        text="<b>Крок 1: Введіть назву точки</b>\n\n(Напишіть текст у чат):"
    )
    # Store menu message_id so text handlers know which message to edit
    await state.update_data(menu_message_id=response_message.message_id)
    await state.set_state(StallRegistration.title)
    await callback.answer()


# 2. When user replies with text
@router.message(StallRegistration.title)
async def process_title(message: types.Message, state: FSMContext, bot: Bot):
    await state.update_data(title=message.text, path_ids=[], selected_ids=[])
    await safe_delete_message(message)
    await state.set_state(StallRegistration.category)

    await edit_or_send_message(
        bot, message, state,
        f"Назва: <b>{message.text}</b>\n\n<b>Крок 2: Оберіть категорії</b> (можна обрати декілька):" ,
        get_categories_keyboard(path_ids=[], selected_ids=set()),
        parse_mode="HTML"
    )


@router.callback_query(StallRegistration.category, CategoryCallback.filter())
async def process_category_navigation(
    callback: types.CallbackQuery,
    callback_data: CategoryCallback,
    state: FSMContext,
):
    if not callback.message or not callback.from_user:
        return

    data = await state.get_data()
    path_ids: list[str] = data.get("cat_path_ids", [])
    selected_ids: set[str] = set(data.get("selected_category_ids", []))

    action = callback_data.action
    target = callback_data.target

    if action == CategoryAction.OPEN:
        path_ids.append(target)

    elif action == CategoryAction.TOGGLE:
        if target in selected_ids:
            selected_ids.remove(target)
        else:
            selected_ids.add(target)

    elif action == CategoryAction.BACK:
        if path_ids:
            path_ids.pop()

    elif action == CategoryAction.DONE:
        if not selected_ids:
            await callback.answer("⚠️ Оберіть хоча б одну категорію!", show_alert=True)
            return

        # Convert English IDs to comma-separated string for storage (e.g. "fresh_veg,fruits")
        category_ids_str = ",".join(sorted(selected_ids))

        user = await User.get(telegram_id=callback.from_user.id)
        stall = await Stall.create(
            title=data.get("title"),
            category=category_ids_str,  # Stores stable IDs in DB
            seller=user,
            is_active=True,
        )

        await state.clear()

        # Convert IDs back to localized names for final UI display
        display_names = [
            get_category_by_id(cid).name_ua
            for cid in selected_ids
            if get_category_by_id(cid)
        ]

        await callback.message.edit_text(
            text=(
                "<b>✅ Точку успішно зареєстровано!</b>\n\n"
                f"<b>Назва:</b> {stall.title}\n"
                f"<b>Категорії:</b> {', '.join(display_names)}\n\n"
                "Тепер покупці зможуть знайти її в каталозі."
            ),
            parse_mode="HTML",
        )
        await callback.answer()
        return

    # Update state
    await state.update_data(
        cat_path_ids=path_ids,
        selected_category_ids=list(selected_ids),
    )

    # Render breadcrumbs in Ukrainian
    path_names = [
        get_category_by_id(cid).name
        for cid in path_ids
        if get_category_by_id(cid)
    ]
    location_str = " ➔ ".join(path_names) if path_names else "Головне меню"

    await callback.message.edit_text(
        text=(
            f"Назва: <b>{data.get('title')}</b>\n"
            f"Розділ: <b>{location_str}</b>\n\n"
            "Оберіть категорії та натисніть <b>Готово</b>:"
        ),
        reply_markup=get_categories_keyboard(
            path_ids=path_ids, selected_ids=selected_ids
        ),
        parse_mode="HTML",
    )
    await callback.answer()