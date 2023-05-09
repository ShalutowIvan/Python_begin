from background import keep_alive


async def on_startup(dp):  #создали асинхронную функцию которая будет запускаться при запуске бота

  from utils.set_bot_commands import set_default_commands  #импортируем функцию которая устанавливает команды бота
  await set_default_commands(dp)  #запустили ее

  print("Бот работает!")  #вывод сообщения в консоль при запуске бота


# keep_alive()
if __name__ == '__main__':
  from aiogram import executor  #импорт executor для запуска пулинга
  from handlers import dp  #импорт диспетчера

  executor.start_polling(dp, on_startup=on_startup)
