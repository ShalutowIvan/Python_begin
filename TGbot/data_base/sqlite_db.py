import sqlite3 as sq#подключили модуль по работе с БД sqlite. Она представляет собой файл, для нее не нужен отдельный сервер, она работает прям в самом приложении
#питон использует 1 поток исполнения, нам здесь подойдет любая БД. sqliteэто встроенная в питоне БД, то есть модуль встроенный, его не надо скачивать и устанавливать

def sql_start():#это функция для создания ДБ или подключения если она уже создана
    global base, cur
    base = sq.connect('pizza_cool.db')#тут у нас происходит подключение к БД. Если файла такого нет, то он создасться, если он есть, то произойдет подключение к нему
    cur = base.cursor()#создаем переменную для курсора, это функция для осуществляет поиск встраивание и выборку данных
    if base:
        print('Database connected OK!')#это просто принт в момент подключении БД
    base.execute('CREATE TABLE IF NOT EXIST menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')#CREATE TABLE IF NOT EXIST menu это означает создать таблицу если такой не существует. Если есть такая, то строка игнорируется. Тут создаются ячейки для полей img, name, description, price
    base.commit()#сохраняем эти изменения
#для начала код из этого файла нужно запустить, это нужно сделать в основном файле в методе on_startup
async def sql_add_command(state):#в параметр state будет попадать наше состояние
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))#тут мы записываем значения в БД из data
        base.commit()