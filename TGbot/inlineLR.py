from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os, hashlib

from aiogram.types import InputTextMessageContent, InlineQueryResultArticle

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)


@dp.inline_handler()#это хендлер который улавливает инлайн события бота
async def inline_handler(query: types.InlineQuery):
	text = query.query or "echo"#query.query это текст который мы вводим полсе названия бота, или echo это означает пока пользователь ничего не ввел
	link = 'https://ru.wikipedia.org/wiki/'+text#тут формируется ссылка на сайт к которому мы будем добавлять текст пользователя для формирования итоговой ссылки
	result_id: str = hashlib.md5(text.encode()).hexdigest()#тут формируется идентификатор, это делаем с помощью метода hashlib.md5
#далее формируем ссылку которую мы отправляем
	articles = [types.InlineQueryResultArticle(#это код для всплывающего окошка
id = result_id,#ид нужен для того чтобы привязать событие к окошечку, его мы сформировали ранее в переменной result_id
title = 'Статья wikipedia:',#тут просто надпись
url = link,#это базовая ссылка в окошке которое будет выходить в телеге, в наше случае ссылка link на википедию
input_message_content=types.InputTextMessageContent(message_text=link))]#это то что отправляется в чат
	await query.answer(articles, cache_time=1, is_personal=True)#и тут мы переменную articles передали в ответ в телеге. cache_time это то с какой скоростью будет обновлятьяс окошко после ввода, ставится цифра от 1 до 60

executor.start_polling(dp, skip_updates=True)
