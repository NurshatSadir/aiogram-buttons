from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="3I"),
        ],
        [
            KeyboardButton(text="4E"),
            KeyboardButton(text="3C")
        ],
    ],
    resize_keyboard=True
)