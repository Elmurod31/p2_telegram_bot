from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from States import UserSoatState
from database import db
Soatlar_router = Router(name="commands")



#Soatlar
@Soatlar_router.callback_query(F.data == "/Soatlar")
async def get_soat(call: CallbackQuery, state: FSMContext):
    await state.set_state(UserSoatState.brendi)
    await call.message.answer("Soatlarni brendini kiriting:")

@Soatlar_router.message(UserSoatState.brendi)
async def get_soat(msg: types.Message, state: FSMContext):
    await state.update_data(brendi=msg.text)
    await state.set_state(UserSoatState.materiali)
    await msg.answer("Soatlarni materyalini kiriting:")

@Soatlar_router.message(UserSoatState.materiali)
async def get_soat(msg: types.Message, state: FSMContext):
    await state.update_data(materyali=msg.text)
    await state.set_state(UserSoatState.narxi)
    await msg.answer("Soatlarni narxini kiriting:")

@Soatlar_router.message(UserSoatState.narxi)
async def get_soat(msg: types.Message, state: FSMContext):
    await state.update_data(narxi=msg.text)
    await state.set_state(UserSoatState.turi)
    await msg.answer("Soatlarni turini kiriting:")

@Soatlar_router.message(UserSoatState.turi)
async def get_soat(msg: types.Message, state: FSMContext):
    await state.update_data(turi=msg.text)
    await state.set_state(UserSoatState.turi)
    data = await state.get_data()
    brendi = data["brendi"]
    materyali = data["materyali"]
    narxi = data["narxi"]
    turi = data["turi"]

    db.add_to_soatlar(brendi, materyali, narxi, turi)
    await msg.answer(f"brendi: {brendi},\n"
                     f"materyali: {materyali},\n"
                     f"narxi: {narxi},\n"
                     f"turi: {turi}")