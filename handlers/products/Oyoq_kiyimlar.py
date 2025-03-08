from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from States import UserOyoqKiyimState
from database import db
Oyoq_kiyimlar_router = Router(name="commands")



#Oyoq kiyimlar
@Oyoq_kiyimlar_router.callback_query(F.data == "/Oyoq kiyimlar")
async def get_Oyoq(call: CallbackQuery, state: FSMContext):
    await state.set_state(UserOyoqKiyimState.brendi)
    await call.message.answer("Oyoq kiyimning brendini kiriting:")

@Oyoq_kiyimlar_router.message(UserOyoqKiyimState.brendi)
async def get_Oyoq(msg: types.Message, state: FSMContext):
    await state.update_data(brendi=msg.text)
    await state.set_state(UserOyoqKiyimState.razmeri)
    await msg.answer("Oyoq kiyimning razmerini kiriting:")

@Oyoq_kiyimlar_router.message(UserOyoqKiyimState.razmeri)
async def get_Oyoq(msg: types.Message, state: FSMContext):
    await state.update_data(razmeri=msg.text)
    await state.set_state(UserOyoqKiyimState.materyali)
    await msg.answer("Oyoq kiyimning materyalini kiriting:")

@Oyoq_kiyimlar_router.message(UserOyoqKiyimState.materyali)
async def get_Oyoq(msg: types.Message, state: FSMContext):
    await state.update_data(materyali=msg.text)
    await state.set_state(UserOyoqKiyimState.narxi)
    await msg.answer("Oyoq kiyimning narxi kiriting:")

@Oyoq_kiyimlar_router.message(UserOyoqKiyimState.narxi)
async def get_Oyoq(msg: types.Message, state: FSMContext):
    await state.update_data(narxi=msg.text)
    await state.set_state(UserOyoqKiyimState.narxi)
    data = await state.get_data()
    brendi = data["brendi"]
    razmeri = data["razmeri"]
    materyali = data["materyali"]
    narxi = data["narxi"]

    db.add_to_Oyoq_Kiyim(brendi, razmeri, materyali, narxi)
    await msg.answer(f"brendi: {brendi},\n"
                     f"razmeri: {razmeri},\n"
                     f"materyali: {materyali},\n"
                     f"narxi: {narxi}")