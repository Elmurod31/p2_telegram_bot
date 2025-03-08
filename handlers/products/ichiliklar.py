from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from States import UserIchimliklarState
from database import db
ichimlaiklar_router = Router(name="commands")

#ichimliklar
@ichimlaiklar_router.callback_query(F.data == "/ichimliklar")
async def user_ichimliklar(call: CallbackQuery, state: FSMContext):
    await state.set_state(UserIchimliklarState.nomi)

    await call.message.answer("Ichimlikni nomini kiriting:")


@ichimlaiklar_router.message(UserIchimliklarState.nomi)
async def user_ichimliklar_hajmi(msg: types.Message, state: FSMContext):
    await state.update_data(nomi=msg.text)
    await state.set_state(UserIchimliklarState.hajmi)
    await msg.answer("Ichimlikni hajmini kiriting:")

@ichimlaiklar_router.message(UserIchimliklarState.hajmi)
async def user_ichimliklar_hajmi(msg: types.Message, state: FSMContext):
    await state.update_data(hajmi=msg.text)
    await state.set_state(UserIchimliklarState.soni)
    await msg.answer("Ichimlikni sonini kiriting:")

@ichimlaiklar_router.message(UserIchimliklarState.soni)
async def user_ichimliklar_soni(msg: types.Message, state: FSMContext):
    await state.update_data(soni=msg.text)
    await state.set_state(UserIchimliklarState.shakarli)
    await msg.answer("Ichimlik shakarli bo'lsinmi:")

@ichimlaiklar_router.message(UserIchimliklarState.shakarli)
async def user_ichimliklar_shakarli(msg: types.Message, state: FSMContext):
    await state.set_state(UserIchimliklarState.shakarli)
    await state.update_data(shakarli=msg.text)
    data = await state.get_data()
    nomi = data["nomi"]
    hajmi = data["hajmi"]
    soni = data["soni"]
    shakarli = data["shakarli"]

    db.add_to_ichimliklar(nomi, hajmi, soni, shakarli)
    await msg.answer(f"nomi: {nomi},\n"
                     f"hajmi: {hajmi},\n"
                     f"soni: {soni},\n"
                     f"shakarlimi: {shakarli}")