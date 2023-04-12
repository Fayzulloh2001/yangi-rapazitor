from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp
import logging

    

@dp.message_handler(text="Ovoz to`plash")
async def boshlash(message: types.Message):
  
    text = f"Assalomu alaykum Hurmatli fuqarolar!\nSizlarga <b>Advokat va yuristlar</b> guruhi yuristlari xizmatidan foydalinishda qulayliklar yaratish maqsadida oʼzimizni yangi loyihamizni ishga tushirdik. <b>USHBU LINKNI YAQINLARINGIZGA YUBORISH ORQALI OʻZ OVOZINGIZNI YIGʻING.</b>  Advokat va yuristlarimiz sizlarga oʻz  yordamini berishda qulaylik  va imtiyozlar yaratib berishadi.Shu bilan bir qatorda eng ko`p ovoz yig`gan ishtirokchiga  <b> 100000 so`m </b> pul mukofoti bilan <b> 19-aprel </b>  kuni taqdirlanadi. Shoshiling o`z ovozlaringizni yig`ing !!!"
    text += f"https://t.me/Advakatovoz_bot?start={message.from_user.id}"

    
    await message.answer(text)
@dp.message_handler(text="To`liqroq malumot")
async def malumotlar(message: types.Message):
    malumot = f"Koproq ovoz yig`ish ushun <b> Ovoz to`plash </b> buyrug`i bosing, bot siz uchun link yaratib beradi, ushbu linkni ko`proq insonlarga tarqating va o`z ovozlaringizni to`plang !!!"
    await message.answer(malumot) 
    
