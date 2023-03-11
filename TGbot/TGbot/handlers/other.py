from aiogram import types, Dispatcher# types для аннотаций типов
from create_bot import dp
import json, string


# @dp.message_handler()#пустой хендлер надо писать в конце до всех хендлеров с командами
async def echo_send(message: types.Message):#сделаем фильтр мата. создадим базу данных с матами и файл json. Бдует txt файл с словами, будет написано слово, потом пропущена строка, потом еще слово и тд
    if {i.lower().translate(str.maketrans("", "", string.punctuation)) for i in message.text.split(" ")}.intersection(set(json.load(open("cenz.json")))) != set():#string.punctuation это перечень знаков пунктуации. Тут мы в итоге получаем все слова которые написал нам пользователь без знаков препинания
        await message.reply("это слово запрещено")
        await message.delete()


def register_handler_other(dp: Dispatcher):#эта функция вместо декораторов. Так как мы функции выше будет передавать через импорт
    dp.register_message_handler(echo_send)