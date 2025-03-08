from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from States import UserSmartfonState
from database import db
Smartfon_router = Router(name="commands")



#Smartfon
@Smartfon_router.callback_query(F.data == "/Smartfon")
async def get_Smartfon(call: CallbackQuery, state: FSMContext):
    await state.set_state(UserSmartfonState.brendi)
    await call.message.answer("Smartfonning brendini kiriting:")

@Smartfon_router.message(UserSmartfonState.brendi)
async def get_Smartfon(msg: types.Message, state: FSMContext):
    await state.update_data(brendi=msg.text)
    await state.set_state(UserSmartfonState.modeli)
    await msg.answer("Smartfonning modelini kiriting:")

@Smartfon_router.message(UserSmartfonState.modeli)
async def get_Smartfon(msg: types.Message, state: FSMContext):
    await state.update_data(modeli=msg.text)
    await state.set_state(UserSmartfonState.xotira)
    await msg.answer("Smartfonning xotirasini kiriting:")

@Smartfon_router.message(UserSmartfonState.xotira)
async def get_Smartfon(msg: types.Message, state: FSMContext):
    await state.update_data(xotira=msg.text)
    await state.set_state(UserSmartfonState.narxi)
    await msg.answer("Smartfonning narxi kiriting:")

@Smartfon_router.message(UserSmartfonState.narxi)
async def get_Smartfon(msg: types.Message, state: FSMContext):
    await state.update_data(narxi=msg.text)
    await state.set_state(UserSmartfonState.narxi)
    data = await state.get_data()
    brendi = data["brendi"]
    modeli = data["modeli"]
    xotira = data["xotira"]
    narxi = data["narxi"]

    db.add_to_Smartfonlar(brendi, modeli, xotira, narxi)
    await msg.answer(f"brendi: {brendi},\n"
                     f"modeli: {modeli},\n"
                     f"xotirasi: {xotira},\n"
                     f"narxi: {narxi}")