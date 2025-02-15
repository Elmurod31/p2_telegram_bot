from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

register_inl_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Ro'yxatdan o'tish", callback_data="/register")]
])

get_phone_btn = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="telefon raqamni jo'natish", request_contact=True),
    ]
], resize_keyboard=True)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Button"),
        KeyboardButton(text="Yordam"),
        KeyboardButton(text="Button3"),
    ],
    [
        KeyboardButton(text="Button4"),
        KeyboardButton(text="Button5"),
        KeyboardButton(text="Button6"),
    ]
])

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Inline Keyboard", callback_data="Yordam"),
         InlineKeyboardButton(text="Inline Keyboard2", callback_data="Test2", url="https://telegram.org")]
    ]
)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Button"),
        KeyboardButton(text="Yordam"),
        KeyboardButton(text="Help"),
    ],
    [
        KeyboardButton(text="/images"),
        KeyboardButton(text="/video"),
        KeyboardButton(text="Button6"),
    ]
])



inline_keyboard1 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Inline Keyboard", callback_data="Yordam"),
            InlineKeyboardButton(text="Inline Keyboard2", callback_data="Test2", url="https://www.youtube.com/@foreveryakudza")
        ],
        [
            InlineKeyboardButton(text="Inline Keyboard3", callback_data="Test3", url="https://www.youtube.com/c/CardinalPUBG"),
            InlineKeyboardButton(text="Inline Keyboard4", callback_data="Test4", url="https://hipolink.me/ultrapubg")
        ]
])