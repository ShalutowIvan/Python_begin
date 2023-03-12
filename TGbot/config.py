from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "токен"
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def echo(message: types.Message):
	await message.answer(text=message.text.upper())#


if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)#запустили бота





