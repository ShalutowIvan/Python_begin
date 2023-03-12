from aiogram import Bot
from aiogram.dispatcher import Dispatcher #этот класс улавливает события в чате от пользователей, позволяет реагировать
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage# тут мы подключили класс для записи данные в озу потом их сразу используем
#также аиограм поддерживает базы данных редис и монго, если нужно данные гдето хранить то можно использовать их

storage = MemoryStorage()#создали объект для записи данных из озу
#тут создаются объекты для бота
bot = Bot(token=os.getenv("TOKEN"))#прочитали токен
dp = Dispatcher(bot, storage=storage)#вызвали класс Dispatcher и передали в него бота, и записали второй параметр хранилище


