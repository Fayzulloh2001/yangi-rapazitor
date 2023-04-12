from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 1-usul.
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Azo bo`lish 1 guruh", url="https://t.me/Advokat_va_Yuristlar"),
       
    ],
    [
        InlineKeyboardButton(text="Azo bo`lish 1 kanal", url="https://t.me/Yurist_Sardorbek"),
    ],
    [
        InlineKeyboardButton(text="Tekshirish", callback_data="tekshir"),
    ],
])
