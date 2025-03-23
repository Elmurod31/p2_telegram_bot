from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from States import UserNotebookState
from database import db
Notebook_router = Router(name="commands")



#Notebook
@Notebook_router.callback_query(F.data == "/Notebooklar")
async def get_Notebook(call: CallbackQuery, state: FSMContext):
    await state.set_state(UserNotebookState.brendi)
    await call.message.answer("Notebookning brendini kiriting:")

@Notebook_router.message(UserNotebookState.brendi)
async def get_Notebook(msg: types.Message, state: FSMContext):
    await state.update_data(brendi=msg.text)
    await state.set_state(UserNotebookState.protsessor)
    await msg.answer("Notebookning protsessorni kiriting:")

@Notebook_router.message(UserNotebookState.protsessor)
async def get_Notebook(msg: types.Message, state: FSMContext):
    await state.update_data(protsessor=msg.text)
    await state.set_state(UserNotebookState.ram)
    await msg.answer("Notebookning ramsini kiriting:")

@Notebook_router.message(UserNotebookState.ram)
async def get_Notebook(msg: types.Message, state: FSMContext):
    await state.update_data(ram=msg.text)
    await state.set_state(UserNotebookState.narxi)
    await msg.answer("Notebookning narxi kiriting:")

@Notebook_router.message(UserNotebookState.narxi)
async def get_Notebook(msg: types.Message, state: FSMContext):
    await state.update_data(narxi=msg.text)
    await state.set_state(UserNotebookState.narxi)
    data = await state.get_data()
    brendi = data["brendi"]
    protsessor = data["protsessor"]
    ram = data["ram"]
    narxi = data["narxi"]

    db.add_to_Notebooklar(brendi, protsessor, ram, narxi)
    await msg.answer(f"brendi: {brendi},\n"
                     f"protsessor: {protsessor},\n"
                     f"ramsi: {ram},\n"
                     f"narxi: {narxi}")