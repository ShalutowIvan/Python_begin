from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

# @dp.message_handler(commands=["start", "help"])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Привет медвед", reply_markup=kb_client)#reply_markup=kb_client это для создания кнопки для команды
        # await message.delete()#лишнее сообщение будет удалено
    except:
        await message.reply("вы не добавили бота, зайдите в бота и запустите ему или напишите боту\nhttps://t.me/learnTH_Bot")


# @dp.message_handler(commands=["Режим_работы"])
async def commands_work(message: types.Message):
    await bot.send_message(message.from_user.id, "с 9 до 18")


# @dp.message_handler(commands=["Расположение"])
async def commands_location(message: types.Message):
    await bot.send_message(message.from_user.id, "в нужном месте")#, reply_markup=ReplyKeyboardRemove())#отправляем сюда класс для удаления клавиатуры. Если теперь нажать на кнопку с расположение, то клавиатура удалится. НО если стартунуть она опять появится


# @dp.message_handler(commands=["Меню"])
async def pizza_menu_command(message: types.Message):#функция для вызова меню, она считывает БД. сама функция прописана в файле sqlite_db
    await sqlite_db.sql_read(message)
    

def register_handler_client(dp: Dispatcher):#эта функция вместо декораторов. Так как мы функции выше будет передавать через импорт
    dp.register_message_handler(commands_start, commands=["start", "help"])
    dp.register_message_handler(commands_work, commands=["Режим_работы"])
    dp.register_message_handler(commands_location, commands=["Расположение"])
    dp.register_message_handler(pizza_menu_command, commands=["Меню"])



