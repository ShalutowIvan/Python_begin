# Ссылки на канал:
# https://www.youtube.com/watch?v=TYs3-uyjC30&list=PLNi5HdK6QEmX1OpHj0wvf8Z28NYoV5sBJ
# https://www.youtube.com/watch?v=axGHFAHlJP8&list=PLmSBSL0-aSglhQu_apL_4GM8VbUKuL2J_
# https://www.youtube.com/watch?v=x-VB3b4pKcU&list=RDCMUCrWWcscvUWaqdQJLQQGO6BA&start_radio=1&rv=x-VB3b4pKcU&t=71
#тут неплохой курс по ботам:
# https://www.youtube.com/watch?v=ayUBlf9pvn0&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=1
#еще один курс, даже лучше чем предыдущий
# https://www.youtube.com/playlist?list=PLwVBSkoL97Q3phZRyInbM4lShvS1cBl-U
#еще канал по боту
# https://www.youtube.com/watch?v=TYs3-uyjC30&list=PLNi5HdK6QEmX1OpHj0wvf8Z28NYoV5sBJ&ab_channel=PythonHubStudio

#/newbot - создание бота в @BotFather (https://t.me/BotFather)
#потом нужно написать имя, это не то имя которое будет в поисковике, а просто имя которое будет у нашего бота
#потом нужно написать имя для бота которое будет в поисковике телеги. Название нужно писать с маленькой буквы и в конце названия написать Bot
#после создания бота нам будет дан токен для взаимодействия с API телеги
#документация аиограм: https://docs.aiogram.dev/en/latest/
#класс диспетчер для общения с ботом. Описание есть в документации
#бот это сервер который будет взаимодейстовать с API телеграма. API телеги это компонент который ответственен за взаимодействие с другими ПО

#урок № 1
# первоначальная настройка виртуального окружения и активация окружения и потом установка аиограм:
# python -m venv venv
# venv\Scripts\activate
# pip install aiogram
#сам бот лучше запускать через bat файл. Так правильнее и безопаснее
# структура бат файла для запуска бота:
# @echo off это для того чтобы служебная инфа не спамила в консоль
#файл активации виртуального окружения это тоже бат файл, нам нужно его вызвать
# %~dp0 это для получения положения батника
# call %~dp0 путь к файлу activate

# cd %~dp0 путь к файлу

# set TOKEN=токен авторизации

# python tgbot.py

# pause это для случая если в скрипте возникнет ошибка и окно консоли закроется и мы не увидит ошибку

#эхо бот
from create_bot import dp
from aiogram.utils import executor#это для запуска бота


#запуск бота. Бота можно запустить в режиме LongPoolling и Webhook
#в режиме LongPoolling бот запускается на локальной машине. Тут бот постоянно опрашивает на наличие сообщений для него. Полезно когда мы разрабатываем бота и тестируем
#режим Webhook, это когда бот находится на сервере, когда туда загружается деплоится. И тут не бот опрашивает сервер телеги, а сервер телеграм опрашивает бота в момент когда сообщения появляются. То есть он постоянно не работает, а работает только тогда когда сервер присылает сообщения
#грубо говоря когда разрабатываем то режим LongPoolling, а когда уже завершили разработку и захостили то Webhook

# @dp.message_handler()
# async def echo_send(message: types.Message):#асинхронная функция. в двух словах, питон однопоточный то есть выполняется поочередно, но боту нужно отвечать на много сообщений и делать это быстро, много действий делать это не очень хорошо. То есть когда в потоке появляется пауза, то в момент паузы исполняется что-то другое, и таким способом ускоряя работу бота. На шу функцию будут попадать сообщения котоыре пользователь будет отправлять в чат.
#     #теперь в теле функции нужно отправить ответное сообщение нашим ботом. Пишем ключевое слово await и потом действие, переводится подождать, пока не появится свободное место для выполнения команды. ТО есть ждем и выполняем действие
#     # await message.answer(message.text)#это ответ от бота. Получается из события message получаем текст
#     # await message.reply(message.text)#метод reply позволяет боту также ответит и упомянуть сообщение на которое отвечает. Он может и в группу и в личку
#     #третий вариант отправляет сообщения в личку пользователю. Если пользователя написал в группу, но не писал пользователю, то бот первый пользователю написать не может
#     # await bot.send_message(message.from_user.id, message.text)#сработает если пользователь уже писал боту или добавился в контакты, в аргументы пишем ид пользователя, которому отправляем, полсе запятой, то что нужно отправить
#     #также тут можно писать и ветвления, чтобы бот отвечал по разному
#     # if message.text == "Привет":
#     #     await message.answer("и тебе привет")
#     await message.answer("Я тебя люблю")
#
# executor.start_polling(dp, skip_updates=True)#skip_updates=True это для того чтобы в момент когда бот не онлайн, чтобы потом при включении он не засыпал сообщениями пользователя. start_polling это функция для запуска.

#урок № 2

async def on_startup(_):#функция которая будет срабатывать при включении бота. в параметре пишем _. Это функция старта
    print("Бот вышел в онлайн")#это просто сообщение. Также в этой функции потом будем писать подключение к базе данных. Также эту функцию нужно передать в executor

# # *------------------------Клиентская часть------------------------*
# #декоратор для команд старт и хелп. Их лучше писать вместе. Этот декоратор сработает когда пользователь добавится к нашему боту или когда напишет /start или /help. ПОлучается message_handler это декоратор который добавляет функционал для реагирования на сообщения. Получается в классе диспетчер есть такая функция декоратор
# @dp.message_handler(commands=["start", "help"])
# async def commands_start(message: types.Message):
#     # await bot.send_message(message.from_user.id, "Привет медвед")#при нажатии на старт, будет написано Привет медвед, но можно е сделать так, чтобы сразу появлялось клавиатура с кнопками
#     #если бот добавлен в группе, то сообщения он отправлять в личку не может если пользователь не добавил бота себе, то есть не нажал запустить в боте. Можно написать для этого обработчик исключений
#     try:
#         await bot.send_message(message.from_user.id, "Привет медвед")
#         await message.delete()#лишнее сообщение будет удалено
#     except:
#         await message.reply("вы не добавили бота, зайдите в бота и запустите ему или напишите боту\nhttps://t.me/learnTH_Bot")#написали в случае исключения, чтобы написали боту. Пустые хенделры лучше писать в самом низу, чтобы обработчики исключений сработали
#
# #обработчик команд можно писать и на кирилице. То есть будет выглядеть так /Режим работы. и после этого сработает наша функция
# @dp.message_handler(commands=["Режим_работы"])#команды боту нужно писать одним словом, если у нас в команде 2 слова то их писать через нижнее подчеркивание
# async def commands_start(message: types.Message):
#     await bot.send_message(message.from_user.id, "с 9 до 18")
#
# @dp.message_handler(commands=["Расположение"])#все команды можно потом поместить в кнопки. вообще в хендлерах можно писать любой код который нам нужен.
# async def commands_start(message: types.Message):
#     await bot.send_message(message.from_user.id, "в нужном месте")

# *------------------------Админская часть------------------------*
# *------------------------Общая часть------------------------*
#
#
# @dp.message_handler()#пустой хендлер надо писать в конце до всех хендлеров с командами
# async def echo_send(message: types.Message):#сделаем фильтр мата. создадим базу данных с матами и файл json. Бдует txt файл с словами, будет написано слово, потом пропущена строка, потом еще слово и тд
#     if {i.lower().translate(str.maketrans("", "", string.punctuation)) for i in message.text.split()}.intersection(set(json.load(open("cenz.json")))) != set():#string.punctuation это перечень знаков пунктуации. Тут мы в итоге получаем все слова которые написал нам пользователь без знаков препинания
#         await message.reply("это слово запрещено")
#         await message.delete()

#перенесли клиентскую и общую часть в отдельные файлы. В файлах есть объекты, которые созданы в основном файле, и созданий объектов этих же нет в отдельных файлах. Нужно объекты из основного файла передать в файлы для клиентской админской и тд частей. Как это сделать. Нужно создать отдельный файл, в нем сделаем взаимоимпорты
from handlers import client, admin, other

client.register_handler_client(dp)
admin.register_handlers_admin(dp)
other.register_handler_other(dp)#опять же пустой хенлер импортировать последним, так как предыдущие могут не сработать


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)#у этой функции есть такой параметр с названием on_startup

#урок № 5.
#кнопки и клавиатура
#В аиограм есть кнопки клавиатуры и инлайн кнопки

#урок №6. FSM Машина состояний админка для бота. В админке есть админ, который пишет изменения разные в бд и тд
#админку можно сделать через django или flask. Но можно сделать через саму телегу. Если через телеграм, то владелец меню пицерии может вносить корректировки через телегу в компа или телефона
#для бота нет разницы в каком порядке мы нажимаем кнопки. Можно сделать некое анкетирование. Например ввести назнвание пиццы потом фотку, потом состав и тд, это все запишется в бд, и потом другой пользователь сможет посмотреть меню. Чтобы записывать в бд, нужна машина состояний

# остановился на 25,40. И почему то не работает загрузка фото, точнее не переходит к следующему состоянию. Скорее всего не работает метод где загружается фото, нужно с ним разобраться. Скорее всего из-за версии питона или аиограм, так как на работе все заработало и ничего не менял

# Урок № 7. lambda фильтр и фильтр Text







