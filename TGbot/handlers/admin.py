# в этом файле админ ловит сообщения и записывает их в словарь. Скорее всего это потом пойдет в записи Бд
from aiogram.dispatcher import FSMContext#для аннотаций типов,мы будем потом указвать в хендлерах, что хендлре использует машину состояний
from aiogram.dispatcher.filters.state import State, StatesGroup#импортировали еще 2 класса
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import button_admin

ID = None

#нужно создать класс наших состояний
class FSMAdmin(StatesGroup):#этот клас наследуется от базового класса StatesGroup. В нем будут переменные для формирования БД. Для каждой переменной мы создаем объект класса State - состояние
    photo = State()#создаем экземпляр класса State, это класс состояний, потом мы будем переходить между состояниями
    name = State()
    description = State()
    price = State()
    #этот класс нужен для записи состояний. Мы его потом запишем в хендлер

#Получаем ID текущего модератор. Это для того чтобы узнать кто администратор в группе
# @dp.message_handler(commands=['moderator'], is_chat_admin=True)#проверка админа чата в группе, сообщения будут срабатывать только если пользователь прошел проверку
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что надо хозяин???'), reply_markup=button_case_admin
    await message.delete()


#начало диалога для загрузки нового пункта меню
# @dp.message_handler(commands="Загрузить", state=None)#для нее тоже сделаем кнопку. Состояние прописываем None, потому что пока состояния нет, так как это старт
async def cm_start(message: types.Message):
    # if message.from_user.id == ID:
        await FSMAdmin.photo.set()#после нажатия команды загрузить, бот перейдет из обычного режима работы в режим работы машины состояний и будет ожидать загрузки фото. Это делается с помощью метода set
        await message.reply("Загрузи фото")#и попросит загрузить фото. Потом нужно написать еще один хендлер, который поймает картинку

#выход из состояний
# @dp.message_handler(state="*", commands="отмена")#звездочка это означает, что берется любое состояние и к нему применяется команда отмена
# @dp.message_handler(Text(equals="отмена", ignore_case=True), state="*")#фильтр текста, берем текст отмена и в любом виде это ignore_case, и любое состояние звездочка
async def cancel_handler(message: types.Message, state: FSMContext):
    # if message.from_user.id == ID:
        current_state = await state.get_state()#получили состояние бота и записали его в переменную
        if current_state is None:#проверяем находится ли бот в каком либо состоянии, если состояние None, то просто возвращаем None, то есть просто return пишем
            return
        await state.finish()#если состояние не None, то закрываем финишем все состояния
        await message.reply("OK")


#ловим ответ и пишем в словарь
# @dp.message_handler(content_types=["photo"], state=FSMAdmin.photo)#в этот ответ попадет фото, тут мы состояние прописали то, которое указали в предыдущей функции с методом set. Теперь состояние другое и эта функция теперь загружает фото
async def load_photo(message: types.Message, state: FSMContext):#FSMContext это для указания того, что в функции используется состояние
    # if message.from_user.id == ID:
        async with state.proxy() as data:#теперь мы сохраняем фото в словарь машины состояний то есть класса FSMAdmin
            data["photo"] = message.photo[0].file_id#тут мы записали в словарь ИД фотки, бот будет отправлять картинку по этому ИД. В телеге есть такая фишка, у фоток есть свой Ид
        await FSMAdmin.next()#с помощью метода next мы переводим нашего бота в ожидание следующего ответа. Теперь бот находится в состоянии name
        await message.reply("Теперь введи название")#и пишем подсказку чтобы ввели следующий параметр

#ловим второй ответ
# @dp.message_handler(state=FSMAdmin.name)#указали что в этот хендлер будет попадать второй ответ
async def load_name(message: types.Message, state: FSMContext):#в функции все по аналогии с предыдущим вариантом, только теперь мы ловим не фото и текст названия, и также записываем в словарь
    # if message.from_user.id == ID:
        async with state.proxy() as data:
            data["name"] = message.text
        await FSMAdmin.next()#и также переходим к третьему состоянию
        await message.reply("Введи описание")


#ловим третий ответ
# @dp.message_handler(state=FSMAdmin.description)#указали что в этот хендлер будет попадать второй ответ
async def load_description(message: types.Message, state: FSMContext):#в функции все по аналогии с предыдущим вариантом, также записываем в словарь значение описания по ключу description
    # if message.from_user.id == ID:
        async with state.proxy() as data:
            data["description"] = message.text
        await FSMAdmin.next()
        await message.reply("Введи цену")

#ловим четвертый и последний ответ
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):#в функции все по аналогии с предыдущим вариантом, также записываем в словарь значение. Но состояние в итоге будет последнее
    # if message.from_user.id == ID:
        async with state.proxy() as data:
            data["price"] = float(message.text)

        # async with state.proxy() as data:#самое простое это просто вывести в чат. Но вообще это значение можно записать в базу данных. это будет потом
        #     await message.reply(str(data))


        await sqlite_db.sql_add_command(state)#запустили функцию их файла питона для ДБ, она добавит инфу в БД. Отправляется словарь, state это словарь
        await state.finish()#как только мы дошли до этого состояния, то полностью очищает все что мы написали при запусках состояний, весь словарь очищается. То есть все что нужно сделать с данными до финиша, нужно сделать до написания функции finish


#теперь нам нужно зарегистрировать все эти хендлеры, так как нужно импортировать все в основной файл

#регистрируем хендлеры
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=["Загрузить"], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands="отмена")#тут зарегали функцию отмены состояний
    dp.register_message_handler(cancel_handler, Text(equals="отмена", ignore_case=True), state="*")#Text это фильтр скорее всего функция, его мы импортировали выше. 2 декоратора, это чтобы срабатывало и со слешем и без слеша
    dp.register_message_handler(load_photo, content_types=["photo"], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    # dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)



#теперь еще нужно сделать отмену состояний. То есть если пользователь передумал добавлять пиццу. ПРоверка на адмнистратора еще сделаем. Ее можно сделать по ИД пользователя телеги, и тогда именно этот польщзователь будет админом бота, или можно просто проверить является ли пользователь группы администратором группы. Я пока не делал проверку на администратора группы, так как нет группы












