from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from States import UserSutState
from database import db
Sutlar_router = Router(name="commands")



#Sutlar
@Sutlar_router.callback_query(F.data == "/Sut mahsulotlari")
async def get_sut(call: CallbackQuery, state: FSMContext):
    await state.set_state(UserSutState.nomi)
    await call.message.answer("Sutning nomini kiriting:")

@Sutlar_router.message(UserSutState.nomi)
async def get_sut(msg: types.Message, state: FSMContext):
    await state.update_data(nomi=msg.text)
    await state.set_state(UserSutState.yog_mikdori)
    await msg.answer("Sutning yog' miqdorini kiriting:")

@Sutlar_router.message(UserSutState.yog_mikdori)
async def get_sut(msg: types.Message, state: FSMContext):
    await state.update_data(yog_mikdori=msg.text)
    await state.set_state(UserSutState.ogirligi)
    await msg.answer("Sutning og'iligini kiriting:")

@Sutlar_router.message(UserSutState.ogirligi)
async def get_sut(msg: types.Message, state: FSMContext):
    await state.update_data(ogirligi=msg.text)
    await state.set_state(UserSutState.narxi)
    await msg.answer("Sutning narxi kiriting:")

@Sutlar_router.message(UserSutState.narxi)
async def get_sut(msg: types.Message, state: FSMContext):
    await state.update_data(narxi=msg.text)
    await state.set_state(UserSutState.narxi)
    data = await state.get_data()
    nomi = data["nomi"]
    yog_mikdori = data["yog_mikdori"]
    ogirligi = data["ogirligi"]
    narxi = data["narxi"]

    db.add_to_sutlar(nomi, yog_mikdori, ogirligi, narxi)
    await msg.answer(f"nomi: {nomi},\n"
                     f"yog' miqdori: {yog_mikdori},\n"
                     f"og'rligi: {ogirligi},\n"
                     f"narxi: {narxi}")