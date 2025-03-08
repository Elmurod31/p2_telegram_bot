from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from States import UserElektromobilState
from database import db
Elektramobilar_router = Router(name="commands")



#Elektramobilar
@Elektramobilar_router.callback_query(F.data == "/Elektramobilar")
async def get_Elektramobilar(call: CallbackQuery, state: FSMContext):
    await state.set_state(UserElektromobilState.modeli)
    await call.message.answer("Elektramobilarning modelini kiriting:")

@Elektramobilar_router.message(UserElektromobilState.modeli)
async def get_Elektramobilar(msg: types.Message, state: FSMContext):
    await state.update_data(modeli=msg.text)
    await state.set_state(UserElektromobilState.quvvat)
    await msg.answer("Elektramobilarning quvvatni kiriting:")

@Elektramobilar_router.message(UserElektromobilState.quvvat)
async def get_Elektramobilar(msg: types.Message, state: FSMContext):
    await state.update_data(quvvat=msg.text)
    await state.set_state(UserElektromobilState.batareya)
    await msg.answer("Elektramobilarning batareyani kiriting:")

@Elektramobilar_router.message(UserElektromobilState.batareya)
async def get_Elektramobilar(msg: types.Message, state: FSMContext):
    await state.update_data(batareya=msg.text)
    await state.set_state(UserElektromobilState.narxi)
    await msg.answer("Elektramobilarning narxi kiriting:")

@Elektramobilar_router.message(UserElektromobilState.narxi)
async def get_Elektramobilar(msg: types.Message, state: FSMContext):
    await state.update_data(narxi=msg.text)
    await state.set_state(UserElektromobilState.narxi)
    data = await state.get_data()
    modeli = data["modeli"]
    quvvat = data["quvvat"]
    batareya = data["batareya"]
    narxi = data["narxi"]

    db.add_to_Elektromobillar(modeli, quvvat, batareya, narxi)
    await msg.answer(f"modeli: {modeli},\n"
                     f"quvvat: {quvvat},\n"
                     f"batareya: {batareya},\n"
                     f"narxi: {narxi}")