#тут мы создаем бота
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

#создаем переменную бота и диспетчера сообщений
bot = Bot(token="", parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)

__all__ = ['bot', 'storage', 'dp']
