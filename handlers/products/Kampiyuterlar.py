from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from States import UserKompyuterState
from database import db
Kompyuter_router = Router(name="commands")



#Kompyuter
@Kompyuter_router.callback_query(F.data == "/Kampiyuterlar")
async def get_Kompyuter(call: CallbackQuery, state: FSMContext):
    await state.set_state(UserKompyuterState.brendi)
    await call.message.answer("Kompyuterning brendini kiriting:")

@Kompyuter_router.message(UserKompyuterState.brendi)
async def get_Kompyuter(msg: types.Message, state: FSMContext):
    await state.update_data(brendi=msg.text)
    await state.set_state(UserKompyuterState.protsessor)
    await msg.answer("Kompyuterning protsessorni kiriting:")

@Kompyuter_router.message(UserKompyuterState.protsessor)
async def get_Kompyuter(msg: types.Message, state: FSMContext):
    await state.update_data(protsessor=msg.text)
    await state.set_state(UserKompyuterState.videokarta)
    await msg.answer("Kompyuterning videokartasini kiriting:")

@Kompyuter_router.message(UserKompyuterState.videokarta)
async def get_Kompyuter(msg: types.Message, state: FSMContext):
    await state.update_data(videokarta=msg.text)
    await state.set_state(UserKompyuterState.narxi)
    await msg.answer("Kompyuterning narxi kiriting:")

@Kompyuter_router.message(UserKompyuterState.narxi)
async def get_Kompyuter(msg: types.Message, state: FSMContext):
    await state.update_data(narxi=msg.text)
    await state.set_state(UserKompyuterState.narxi)
    data = await state.get_data()
    brendi = data["brendi"]
    protsessor = data["protsessor"]
    videokarta = data["videokarta"]
    narxi = data["narxi"]

    db.add_to_Kompyuterlar(brendi, protsessor, videokarta, narxi)
    await msg.answer(f"brendi: {brendi},\n"
                     f"protsessor: {protsessor},\n"
                     f"videokartasi: {videokarta},\n"
                     f"narxi: {narxi}")