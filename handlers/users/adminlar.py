from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(text="/barchasi", user_id=ADMINS)
async def get_allusers(message: types.Message):
    users = db.select_all_users()
    for user in users:
        listlar=list(user)
        name = listlar[2]
        tel = listlar[4]
        ball = listlar[1]
        await message.answer(f" {ball} ovoz , ismi: {name}, tel: {tel} ")
    