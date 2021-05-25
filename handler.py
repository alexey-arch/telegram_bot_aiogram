from main import bot, dp
from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup
from config import admin_id
from aiogram import types
import random
from aiogram.dispatcher.filters import Command, Text 
import pytube
import os
from mat import a
async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен!")

@dp.message_handler(Command("start"))
async def start(message: Message):
    markup = ReplyKeyboardMarkup(keyboard = [
            [
                KeyboardButton(text="Скачать видео🔴"),
            ],
        ],
        resize_keyboard = True
    )
    user_name = message.from_user.first_name 
    await message.answer(f"Привет, {user_name}!✋\nЧем я могу вам помочь?🙃".format(message.from_user),
    reply_markup=markup)


@dp.message_handler(lambda message: message.text == "Скачать видео🔴")
async def vid(message: types.Message):
    await message.answer(text="Отправьте мне ссылку на видео.😌", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(lambda message: "https://www.youtube.com/" in message.text or "https://youtube.com/" in message.text)
async def vid_echo(message: types.Message):
    try:
        text = f"загрузка началась.👌\nДождитесь окончания загрузки.😉"
        await bot.send_message(chat_id=message.chat.id, text=text)
        youtube = pytube.YouTube(message.text)
        video = youtube.streams.get_highest_resolution()
        
        video.download()
        new_name = random.randint(1, 50)
        os.rename(video.default_filename, str(new_name)+".mp4")

        fn = str(new_name)+".mp4"
        data = open(fn,'rb')
        await bot.send_video(message.chat.id, data)
        await message.answer("Вот ваше видео!😉")

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), fn)
        os.remove(path)
    except:
        await message.answer(text="Ой! что-то пошло не так! видимо не верная ссылка повторите попытку.🙁")


@dp.message_handler(Command("help"))
async def info_help(message: Message):
    markup = ReplyKeyboardMarkup(keyboard = [
            [
                KeyboardButton(text="Информация обо мне🙃 и моем создатиле.😎"),
                KeyboardButton(text="как пользоваься этой штукой?🤔"),
            ],
        ],
        resize_keyboard = True
    )
    await message.answer(text="Чем я могу вам помочь?🙃",
    reply_markup=markup)
    

@dp.message_handler(lambda message: message.text == "Информация обо мне🙃 и моем создатиле.😎")
async def info(message: types.Message):
    user_name = message.from_user.first_name
    text = f'Привет {user_name}! Меня зовут ... я бот который помогает людям скачать видео с Ютуб.\n\
мой создатель Мустафин Алексей добрый, веселый парень.'
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())

@dp.message_handler(lambda message: message.text == "как пользоваься этой штукой?🤔")
async def hel(message: types.Message):
    text = f'Для начала скопируйте ссылку желающего видео, а затем напишите мне /start.'
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(lambda message: message.text != "/start" or message.text != "/help")
async def welcome(message: Message):
    user_name = message.from_user.first_name 
    text = f"Привет {user_name}! рад вас видеть. Для продолжения работы напишите мне /start.\n\
А если хотите узнать больше то напишите /help."

    if message.text in a :
        await message.answer(text="Попрошу вас не выражаться ненормативной лексикой!😠")
    else:
        await message.answer(text=text)

