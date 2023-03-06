# Ссылки на канал:
# https://www.youtube.com/watch?v=TYs3-uyjC30&list=PLNi5HdK6QEmX1OpHj0wvf8Z28NYoV5sBJ
# https://www.youtube.com/watch?v=axGHFAHlJP8&list=PLmSBSL0-aSglhQu_apL_4GM8VbUKuL2J_
# https://www.youtube.com/watch?v=x-VB3b4pKcU&list=RDCMUCrWWcscvUWaqdQJLQQGO6BA&start_radio=1&rv=x-VB3b4pKcU&t=71
#тут неплохой курс по ботам:
# https://www.youtube.com/watch?v=ayUBlf9pvn0&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=1
#еще один курс, даже лучше чем предыдущий
# https://www.youtube.com/playlist?list=PLwVBSkoL97Q3phZRyInbM4lShvS1cBl-U
#еще канал по питону
# https://www.youtube.com/watch?v=Alg3a4KW9uQ&list=PLF4MWzDJPFSZJeqc7u65mRAjR-1eFKUfd&ab_channel=%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B9%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%7CPython
#/newbot - создание бота в @BotFather (https://t.me/BotFather)
#потом нужно написать имя, это не то имя которое будет в поисковике, а просто имя которое будет у нашего бота
#потом нужно написать имя для бота которое будет в поисковике телеги. Название нужно писать с маленькой буквы и в конце названия написать Bot
#после создания бота нам будет дан токен для взаимодействия с API телеги
#документация аиограм: https://docs.aiogram.dev/en/latest/
#класс диспетчер для общения с ботом. Описание есть в документации
#бот это сервер который будет взаимодейстовать с API телеграма. API телеги это компонент который ответственен за взаимодействие с другими ПО
# import aiogram
from aiogram import Bot, Dispatcher, executor, types
TOKEN_API = ""#скопировали токен из ботфазера и записали его в переменную, это токен для подключения к телеграм API. Токен из бота для теории

bot = Bot(TOKEN_API)#создали экземпляр класса Bot, и в качестве свойства передали наш токен
dp = Dispatcher(bot)#содали объект класса Dispatcher, в качестве параметра передали объект бота, который создали выше. Этот класс нужен для взаимодействия бота в телеге 

@dp.message_handler()#получается на любой апдейт, будет срабатывать функция. Наш декоратор добавляет функционал для функции
async def echo(message: types.Message):#прописали аннотацию в асинхронной функции
	if len(message.text.split()) == 2:
		await message.answer(text=message.text.upper())#capitalize пишет текст с загланой буквы

	# await message.answer(text=message.text.upper())#message это объект с сообщением, которое отправил нам пользователь, text это атрибут с текстом который отправил нам пользователь




if __name__ == "__main__":
	executor.start_polling(dp)#запустили бота





