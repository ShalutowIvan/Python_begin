import sqlite3 as sq#подключили модуль по работе с БД sqlite. Она представляет собой файл, для нее не нужен отдельный сервер, она работает прям в самом приложении
#питон использует 1 поток исполнения, нам здесь подойдет любая БД. sqliteэто встроенная в питоне БД, то есть модуль встроенный, его не надо скачивать и устанавливать
from create_bot import dp, bot

def sql_start():#это функция для создания ДБ или подключения если она уже создана
    global base, cur
    base = sq.connect('pizza_cool.db')#тут у нас происходит подключение к БД. Если файла такого нет, то он создасться, если он есть, то произойдет подключение к нему. Файл базы будет создан в корневой папке с ботом
    cur = base.cursor()#создаем переменную для курсора, это функция для осуществляет поиск встраивание и выборку данных
    if base:
        print('Database connected OK!')#это просто принт в момент подключении БД
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')#CREATE TABLE IF NOT EXIST menu это означает создать таблицу если такой не существует. Если есть такая, то строка игнорируется. Тут создаются ячейки для полей img, name, description, price
    base.commit()#сохраняем эти изменения
#для начала код из этого файла нужно запустить, это нужно сделать в основном файле в методе on_startup
async def sql_add_command(state):#в параметр state будет попадать наше состояние
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))#тут мы записываем значения в БД из data
        base.commit()#сохранили изменения

async def sql_read(message):
    for ret in cur.execute("SELECT * FROM menu").fetchall():#"SELECT * FROM menu" это означает выбрать все из таблицы меню. fetchall выгружает все в виде списка, и мы его перебираем в цикле
        await bot.send_photo(message.from_user.id, ret[0], f"{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}")
#в цикле мы перебираем все строки таблицы и отправляем пользователю в личку. В каждой строке есть отдельная пицца со всеми ее свойствами, фото, название цена. список состоит из объектов пицц

async def sql_read2():
    return cur.execute("SELECT * FROM menu").fetchall()#просто считывается все меню

async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))#по названию ищем запись и удаляем ее
    base.commit()



