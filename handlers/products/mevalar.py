from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from States import UserMevalarState
from database import db
mevalar_router = Router(name="commands")


#Mevalar
@mevalar_router.callback_query(F.data == "/Mevalar")
async def get_mevalar(call: CallbackQuery, state: FSMContext):
    await state.set_state(UserMevalarState.nomi)
    await call.message.answer("Mevani nomini kiriting:")

@mevalar_router.message(UserMevalarState.nomi)
async def get_mevalar(msg: types.Message, state: FSMContext):
    await state.update_data(nomi=msg.text)
    await state.set_state(UserMevalarState.ogirligi)
    await msg.answer("Mevanlarni og'irligini kiriting:")

@mevalar_router.message(UserMevalarState.ogirligi)
async def get_mevalar(msg: types.Message, state: FSMContext):
    await state.update_data(ogirligi=msg.text)
    await state.set_state(UserMevalarState.rangi)
    await msg.answer("Mevani rangi kiriting:")

@mevalar_router.message(UserMevalarState.rangi)
async def get_mevalar(msg: types.Message, state: FSMContext):
    await state.update_data(rangi=msg.text)
    await state.set_state(UserMevalarState.shakli)
    await msg.answer("Mevani shakli kiriting:")

@mevalar_router.message(UserMevalarState.shakli)
async def get_mevalar(msg: types.Message, state: FSMContext):
    await state.update_data(shakli=msg.text)
    await state.set_state(UserMevalarState.shakli)
    data = await state.get_data()
    nomi = data["nomi"]
    ogirligi = data["rangi"]
    rangi = data["rangi"]
    shakli = data["shakli"]

    db.add_to_mevalar(nomi, ogirligi, rangi, shakli)
    await msg.answer(f"nomi: {nomi},\n"
                     f"ogirligi: {ogirligi},\n"
                     f"rangi: {rangi},\n"
                     f"shakli: {shakli}")