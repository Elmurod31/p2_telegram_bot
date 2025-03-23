import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers.commands.command import command_router
from handlers.products.Elektramobillar import Elektramobilar_router
from handlers.products.Kampiyuterlar import Kompyuter_router
from handlers.products.Notebooklar import Notebook_router
from handlers.products.Oyoq_kiyimlar import Oyoq_kiyimlar_router
from handlers.products.Smartfonlar import Smartfon_router
from handlers.products.Soatlar import Soatlar_router
from handlers.products.gosht_mahsulotlari import gosht_mahsilotlari_router
from handlers.products.ichiliklar import ichimlaiklar_router
from handlers.products.mevalar import mevalar_router
from handlers.products.sut_mahsulotlari import Sutlar_router
from handlers.register.register import register_router

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
dp.include_router(command_router)
dp.include_router(ichimlaiklar_router)
dp.include_router(mevalar_router)
dp.include_router(gosht_mahsilotlari_router)
dp.include_router(Sutlar_router)
dp.include_router(Soatlar_router)
dp.include_router(Oyoq_kiyimlar_router)
dp.include_router(register_router)
dp.include_router(Elektramobilar_router)
dp.include_router(Smartfon_router)
dp.include_router(Notebook_router)
dp.include_router(Kompyuter_router)





async def main():
    print("Starting...bot")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())