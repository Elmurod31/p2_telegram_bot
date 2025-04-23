from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from database import db
Mahsulot_korish_router = Router(name="commands")


#Mahsulot_ko'rish
@Mahsulot_korish_router.callback_query(F.data == "/Maxsulotlarni_ko'rish")
async def get_Mahsulot_korish(call: CallbackQuery, state: FSMContext):
    mahsulot_korish = db.get_ichimliklar()
    await call.message.answer(f"{mahsulot_korish[1][1]}")