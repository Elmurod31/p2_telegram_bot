from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile

from database import db
from keyboards import register_inl_btn, get_phone_btn, add_product_btn

command_router = Router(name="commands")

@command_router.message(CommandStart())
async def start(message: types.Message):
    user = db.get_telegram_user_from_db(message.from_user.id)
    if user:
        await message.answer("Do'konimizga xush kelibsiz!")
        if user.get("is_seller"):

            await message.answer("Mahsulot qo'shishingiz mumkun:",
                                 reply_markup=add_product_btn)
    else:
            await message.answer("Do'konimizga xush kelibsiz!\n"
                                 "Ro'yxatdan o'ting!", reply_markup=register_inl_btn)


@command_router.message(Command("help"))
async def _help(message: types.Message):
    await message.answer("Help")


@command_router.message(Command("images"))
async def get_image(msg: types.Message):
    img = FSInputFile("images/img.png")
    await msg.answer_photo(img, caption="Bu screenshot")


@command_router.message(Command("videos"))
async def get_video(msg: types.Message):
    video = FSInputFile("videos/20250218-0428-29.7812879.mp4")
    await msg.answer_video(video, caption="Bu screenrecorder")


@command_router.message(F.video)
async def get_video(msg: types.Message):
    await msg.answer("Video uchun rahmat")
