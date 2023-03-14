from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)

#Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=2)#инициализировали класс клавиатуры, указали свойство объекта это ширина ряда, то есть по одной кнопке в ряд. Ограничение ширины ряда на метод row не распространяется
urlButton = InlineKeyboardButton(text="Ссылка1", url="https://youtube.com")#создали объект кнопки. text это название кнопки, url - это действие которое делает кнопка, в нашем случае переход по ссылке ютуба
urlButton2 = InlineKeyboardButton(text="Ссылка2", url="https://google.com")#тут вторая кнопка
x = [InlineKeyboardButton(text="Ссылка3", url="https://google.com"), InlineKeyboardButton(text="Ссылка4", url="https://google.com"), InlineKeyboardButton(text="Ссылка5", url="https://google.com"), InlineKeyboardButton(text="Ссылка6", url="https://google.com"), InlineKeyboardButton(text="Ссылка7", url="https://google.com")]


urlkb.add(urlButton, urlButton2).row(*x).insert(InlineKeyboardButton(text="Ссылка8", url="https://google.com"))#метод insert добавляет кнопку в ту же строку если лимит кнопок row_width не исчерпан для строки, если исчерпан, то добавляет на новую строку
#метод add мы добавляем кнопки к объекту, методы такие же как с обычной клавой. И добавили ряд кнопок в виде распакованного списка. Ограничение ширины ряда row_width на метод row не распространяется

@dp.message_handler(commands="ссылки")#тут мы пишем простой хендлер для команды, при вводе которой будет появляеться клавиатура с кнопками
async def url_command(message : types.Message):
	await message.answer("Ссылочки:", reply_markup=urlkb)# в reply_markup мы записали наш объект с кнопками

#Колбэк кнопки!!!!
inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Нажми меня", callback_data="www"))







executor.start_polling(dp, skip_updates=True)



