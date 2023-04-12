from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ovoz to`plash'),
            KeyboardButton(text='To`liqroq malumot'),
        ],
        [
            KeyboardButton(text='Yig`ilgan ovozlar'),
            
        ],
    ],
    resize_keyboard=True
)
