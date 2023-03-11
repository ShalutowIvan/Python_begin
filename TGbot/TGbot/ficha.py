#тут фишки для ботов. Сделаем бота, который будет ловить только команды. Команды будут отлавливаться, а есл будет другое сообщение, то него один ответ "нет такой команды"
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

@dp.message_handler()
async def empty(message: types.Message):
	await message.answer('Нет такой команды')
	await message.delete()



executor.start_polling(dp, skip_updates=True)




