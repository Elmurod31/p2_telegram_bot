from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from States import UserGoshtState
from database import db
gosht_mahsilotlari_router = Router(name="commands")




#go'sht mahsulotlari
@gosht_mahsilotlari_router.callback_query(F.data == "/Go'sht mahsulotlari")
async def get_gosht(call: CallbackQuery, state: FSMContext):
    await state.set_state(UserGoshtState.turi)

    await call.message.answer("Go'shtni turini kiriting:")

@gosht_mahsilotlari_router.message(UserGoshtState.turi)
async def get_gosht(msg: types.Message, state: FSMContext):
    await state.update_data(turi=msg.text)
    await state.set_state(UserGoshtState.ogirligi)
    await msg.answer("Go'shtni og'irligini kiriting:")

@gosht_mahsilotlari_router.message(UserGoshtState.ogirligi)
async def get_gosht(msg: types.Message, state: FSMContext):
    await state.update_data(ogirligi=msg.text)
    await state.set_state(UserGoshtState.narxi)
    await msg.answer("Go'shtni rangi kiriting:")

@gosht_mahsilotlari_router.message(UserGoshtState.narxi)
async def get_gosht(msg: types.Message, state: FSMContext):
    await state.update_data(rangi=msg.text)
    await state.set_state(UserGoshtState.shakli)
    await msg.answer("Go'shtni shakli kiriting:")

@gosht_mahsilotlari_router.message(UserGoshtState.shakli)
async def get_gosht(msg: types.Message, state: FSMContext):
    await state.update_data(shakli=msg.text)
    await state.set_state(UserGoshtState.shakli)
    data = await state.get_data()
    turi = data["turi"]
    ogirligi = data["ogirligi"]
    rangi = data["rangi"]
    shakli = data["shakli"]

    db.add_to_goshtlar(turi, ogirligi, rangi, shakli)
    await msg.answer(f"turi: {turi},\n"
                     f"ogirligi: {ogirligi},\n"
                     f"rangi: {rangi},\n"
                     f"shakli: {shakli}")