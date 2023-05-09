from aiogram import types, Bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboard.inline import ikb_doctor
from db_api import table_commands
from keyboard.default import kb_menu
from loader import dp, bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta, date
import emoji

async def send_message_time(call: types.CallbackQuery, dc):
	await call.message.answer(text=f"{emoji.emojize(':alarm_clock:')} Завтра прием к этому врачу: {dc} {emoji.emojize(':backhand_index_pointing_left:')}")


@dp.callback_query_handler(text='включить_напоминание_врач')
async def run_reminder(call: types.CallbackQuery):
    #вводить в таблицу нужно дату и время когда нужно напоминание, а в название врача писать все что связано с записью к врачу
    # сначала пишется функция которую вызываем, потом в kwargs пишем параметры для этой функции в виде словаря, ключи это названия аргументов вызываемой функции, значения подставляем те которые нам надо

    try:
        info = await table_commands.change_time_date(db='pups_his' + str(call.message.chat.id))
        dt = [
        [datetime.strptime(str(i[0]) + " " + str(i[1]) + ".000000", '%Y-%m-%d %H:%M:%S.%f'), i[2]]
        for i in info
             ]#тут список дат

        scheduler = AsyncIOScheduler()
        for i in dt:
            scheduler.add_job(send_message_time, trigger='date', run_date=i[0], kwargs={'call': call, "dc": i[1]})

        scheduler.start()
        await call.message.answer('Напоминание включили!')
    except Exception as _ex:
        await call.message.answer("Что-то пошло не так! Попробуйте еще раз!")
    finally:
        await call.message.answer('Что дальше?')




