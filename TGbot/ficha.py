#тут фишки для ботов. Сделаем бота, который будет ловить только команды. Команды будут отлавливаться, а есл будет другое сообщение, то него один ответ "нет такой команды". Тут еще будет парсинг сообщений. И кнопки с нужными нам названиями
from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
	await message.reply('Здарово')


@dp.message_handler(commands=['команда'])
async def echo(message: types.Message):
	await message.answer(message.text)

@dp.message_handler(lambda message: 'такси' in message.text)
async def taxi(message: types.Message):
	await message.answer('такси')

@dp.message_handler(lambda message: 'нло' in message.text)
async def ufo(message: types.Message):
	await message.answer('нло')
#по аналогии можно писать и эту функцию Text(equals="отмена", ignore_case=True). Фукнция текст есть в модуле aiogram.dispatcher.filters


@dp.message_handler()
async def empty(message: types.Message):
	await message.answer('Нет такой команды')
	await message.delete()



executor.start_polling(dp, skip_updates=True)




