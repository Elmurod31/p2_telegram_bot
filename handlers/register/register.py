from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from States import UserRegisterState
from database import db
from keyboards import get_phone_btn
register_router = Router(name="commands")


#register
@register_router.callback_query(F.data == "/register")
async def user_register(call: CallbackQuery, state: FSMContext):
    await state.set_state(UserRegisterState.full_name)

    await call.message.answer("Ismingizni kiriting:")


@register_router.message(UserRegisterState.full_name)
async def get_full_name(msg: types.Message, state: FSMContext):
    await state.update_data(full_name=msg.text)
    await state.set_state(UserRegisterState.phone_number)
    await msg.answer("Telefon raqamingizni kiriting: ", reply_markup=get_phone_btn)


@register_router.message(UserRegisterState.phone_number)
async def get_phone_number(msg: types.Message, state: FSMContext):
    if msg.text:
        await state.update_data(phone_number=msg.text)
    elif msg.contact.phone_number:
        await state.update_data(phone_number=msg.contact.phone_number)
    await msg.answer("Yoshingizni kiriting:")
    await state.set_state(UserRegisterState.age)


@register_router.message(UserRegisterState.age)
async def get_age(msg: types.Message, state: FSMContext):
    await state.update_data(age=msg.text)
    await msg.answer("Manzilingizni kiriting: ")
    await state.set_state(UserRegisterState.address)


@register_router.message(UserRegisterState.address)
async def get_address(msg: types.Message, state: FSMContext):
    await state.update_data(address=msg.text)
    data = await state.get_data()
    full_name = data["full_name"]
    phone_number = data["phone_number"]
    age = data["age"]
    address = data["address"]
    telegram_id = msg.from_user.id

    db.add_to_users(full_name, phone_number, age, address, telegram_id)



    await msg.answer("Malumotlaringiz saqlandi!")
    await state.clear()