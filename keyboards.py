from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

register_inl_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Ro'yxatdan o'tish", callback_data="/register")]
])

get_phone_btn = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="telefon raqamni jo'natish", request_contact=True),
    ]
], resize_keyboard=True)

add_product_btn = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Mahsulot qo'shish", callback_data="/add_product"),
    ],
    [
        InlineKeyboardButton(text="Ichimliklar", callback_data="/ichimliklar"),
        InlineKeyboardButton(text="Mevalar", callback_data="/Mevalar")
    ],
    [
        InlineKeyboardButton(text="Go'sht mahsulotlari", callback_data="/Go'sht mahsulotlari"),
        InlineKeyboardButton(text="Sut mahsulotlari", callback_data="/Sut mahsulotlari"),
    ],
    [
        InlineKeyboardButton(text="Soatlar", callback_data="/Soatlar"),
        InlineKeyboardButton(text="Oyoq kiyimlar", callback_data="/Oyoq kiyimlar"),
    ],
    [
        InlineKeyboardButton(text="Elektramobilar", callback_data="/Elektramobilar"),
        InlineKeyboardButton(text="Smartfonlar", callback_data="/Smartfonlar")
    ],
    [
        InlineKeyboardButton(text="Notebooklar", callback_data="/Notebooklar"),
        InlineKeyboardButton(text="Kampiyuterlar", callback_data="/Kampiyuterlar"),
    ]
], resize_keyboard=True)