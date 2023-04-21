from aiogram import Bot, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.dispatcher import Dispatcher
from datetime import datetime, timedelta, date
from aiogram.utils import executor

bot = Bot(token="")
dp = Dispatcher(bot)



async def send_message_time(bot: Bot):#эту функцию будем запускать через несколько секунд после старта бота
	await bot.send_message(юзерид, 'сообщение чуть позже')
	# await message.reply("Привет! Напиши мне что-нибудь!")


async def send_message_cron(bot: Bot):
	await bot.send_message(message.from_user.id, f'сообщение ежедневно')

async def send_message_interval(bot: Bot):
	await bot.send_message(message.from_user.id, f'сообщение с определенным интервалом')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    # await message.reply("Привет!\nНапиши мне что-нибудь!")

	scheduler = AsyncIOScheduler(timezone='UTC')

	# scheduler.add_job(send_message_time, trigger='date', run_date=datetime.now() + timedelta(seconds=3), kwargs={'bot': bot})
	scheduler.add_job(send_message_time, trigger='date', run_date=datetime.now() + timedelta(seconds=3), kwargs={'bot': bot})

	# scheduler.add_job(send_message_cron, trigger='cron', hour=datetime.now().hour, minute=datetime.now().minute + 1, start_date=datetime.now(), kwargs={'bot': bot})
	# scheduler.add_job(send_message_interval, trigger='interval', seconds=60, kwargs={'bot': bot})
	scheduler.start()



# сделать обработчик команды старт хендлер
# @dp.message_handler()
# async def echo_send(message: types.Message):

# 	# scheduler = await AsyncIOScheduler(timezone='Europe/Moscow')

# 	# await scheduler.add_job(send_message_time, trigger='date', run_date=datetime.now() + timedelta(seconds=3), kwargs={'bot': bot})
# 	# # scheduler.add_job(send_message_cron, trigger='cron', hour=datetime.now().hour, minute=datetime.now().minute + 1, start_date=datetime.now(), kwargs={'bot': bot})
# 	# # scheduler.add_job(send_message_interval, trigger='interval', seconds=60, kwargs={'bot': bot})
# 	# await scheduler.start()

# 	await message.answer(text=message.text)


if __name__ == "__main__":
	executor.start_polling(dp)
