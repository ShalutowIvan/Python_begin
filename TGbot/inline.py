from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text#импортировали фильтр Text
import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)

answ = dict()#это словарь для голосования ниже

#Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=2)#инициализировали класс клавиатуры InlineKeyboardMarkup, создался объект, указали свойство объекта это ширина ряда, то есть по одной кнопке в ряд. Ограничение ширины ряда на метод row не распространяется
urlButton = InlineKeyboardButton(text="Ссылка1", url="https://youtube.com")#создали объект кнопки. text это название кнопки, url - это действие которое делает кнопка, в нашем случае переход по ссылке ютуба
urlButton2 = InlineKeyboardButton(text="Ссылка2", url="https://google.com")#тут вторая кнопка
x = [InlineKeyboardButton(text="Ссылка3", url="https://google.com"), InlineKeyboardButton(text="Ссылка4", url="https://google.com"), InlineKeyboardButton(text="Ссылка5", url="https://google.com"), InlineKeyboardButton(text="Ссылка6", url="https://google.com"), InlineKeyboardButton(text="Ссылка7", url="https://google.com")]


urlkb.add(urlButton, urlButton2).row(*x).insert(InlineKeyboardButton(text="Ссылка8", url="https://google.com"))#метод insert добавляет кнопку в ту же строку если лимит кнопок row_width не исчерпан для строки, если исчерпан, то добавляет на новую строку
#метод add мы добавляем кнопки к объекту, методы такие же как с обычной клавой. И добавили ряд кнопок в виде распакованного списка. Ограничение ширины ряда row_width на метод row не распространяется

@dp.message_handler(commands="ссылки")#тут мы пишем простой хендлер для команды, при вводе которой будет появляеться клавиатура с кнопками
async def url_command(message : types.Message):
	await message.answer("Ссылочки:", reply_markup=urlkb)# в reply_markup мы записали наш объект с кнопками

#Колбэк кнопки!!!!
inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Нажми меня", callback_data="www"))#создали объект для инлайн кнопки, срузу к объекту прибавили кнопку. Также прописали callback_data, это имя события которое произойдет, можно для начала написать просто строку, текст из события отправляется боту. Эту строку потом будем ловить хендлером. Туда можно и передавать данные, на основе которых будет работать код

@dp.message_handler(commands="test")#сделали хендлер для инлайн кнопки, срабатывает на команду /test
async def test_commands(message : types.Message):
	await message.answer("Инлайн кнопка", reply_markup=inkb)#сюда передали объект кнопки, inkb это объект

#получается мы сделали объект кнопку с определенным действием, потом сделали команду для того чтобы кнопка появилась
#сейчас наша кнопка ничего не делает, и при нажатии на нее будет на ней значок часиков, он отображается примерно 20-30 сек
#теперь сделаем хендлер который будет ловить колбэк

@dp.callback_query_handler(text="www")#текст на который будет срабатывать этот хендлер
async def www_call(callback : types.CallbackQuery):#callback это параметр, название параметр можно писать любое, но обязательно нужно писать аннотацию типа types.CallbackQuery, чтобы код был читабельный
	# await callback.answer("Нажата инлайн кнопка")#в телеге появится просто уведомление с текстом Нажата инлайн кнопка. То есть у колбека функция answer не отвечает на сообщение, а срабатывает как всплывающее уведомление и потом пропадает
	await callback.message.answer("Нажата инлайн кнопка")#если написать так, message.answer, то появится ответ именно в чате телеги
	#но после нажатия кнопки часики на кнопке будут все еще висеть, потому что бот ждет подтверждения, что код который мы хотели исполнить в callback_query_handler уже выполнен. Поэтому нужно написать следующее:
	# await callback.answer()#то есть пустой callback.answer. Часики пропадут как только код исполнится. ТО есть тут мы как бы подтверждаем, что код отработал и все произошло успешно. Либо можно туда записать текст, и тогда после срабатывания ансвера, часики пропадут сразу и будет выглядеть как какое то действие
	await callback.answer("Все хорошо!", show_alert=True)#бот напишет сообщение в чат и появится всплыващее и исчезающее окно с текстом Все хорошо! А если написать еще show_alert=True, то окно будет не просто исчезающим, а нужно будет еще нажать ок, чтобы окно исчезло, то есть мы явно оповещаем пользователя, что он нажал кнопку

#сделаем подсчет лайков и дизлайков

inlike = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Like", callback_data="like_1"), InlineKeyboardButton(text="dislike", callback_data="like_-1"))#в функцию add можно через запятую добавлять объекты.


@dp.message_handler(commands="test1")
async def test_commands(message : types.Message):
	await message.answer("За видео про деплой бота", reply_markup=inlike)

@dp.callback_query_handler(Text(startswith="like_"))#в скобках пишем условие для фильтра, применяем метод для строк. теперь наш хендлер сработает на текст like_, наши колбеки начинаются с этого текста, то есть сработает для или для первой кнопки или для второй
async def www_like(callback : types.CallbackQuery):
	res = int(callback.data.split("_")[1])#разбили на список строку по _, и взяли второй элемент, это будет 1 или -1, перевели строку в цифру
	if f"{callback.from_user.id}" not in answ:
		answ[f"{callback.from_user.id}"] = res#в словарь по ключу в виде Ид пользователя запишется 1 или -1
		await callback.answer("Вы проголосовали")#увед, вы проголосовали
	else:
		await callback.answer("Вы уже проголосовали ранее", show_alert=True)
#далее можно этот словарь суммировать или куда то записать.... Вернемся к боту для пиццерии


executor.start_polling(dp, skip_updates=True)



