import telebot
from telebot import types
import logging
from rembg import remove
from PIL import Image

TOKEN = '5955524409:AAGNgRUswxFMt1yNadILkCRFpDphMPYKk_M'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu Alaykum! Stiker yaratish uchun rasm jo'nating 😇")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    photo = message.photo[-1].file_id
    bot.send_message(message.chat.id, "Stiker yaratilmoqda... Kuting 🥱")
    file_info = bot.get_file(photo)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("image.png", 'wb') as new_file:
        new_file.write(downloaded_file)
        img = Image.open("image.png")
        R = remove(img)
        R.save("bot.png")
        sti = open('bot.png', 'rb')
    
        bot.send_sticker(message.chat.id, sticker=sti)
        bot.send_message(message.chat.id, "Stiker yaratildi 🤭")
    
        
    
   
bot.polling()