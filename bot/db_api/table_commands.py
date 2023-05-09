import sqlite3 as sq
#в этом файле создание базы данных и всех таблиц в ней. Имя базы берется из юзерИД телеги. Также тут и добавление данных в таблицу, не стал разбивать на разные файлы, создание и добавление в одном файле



# async def add_tables(db):
#     conn = psycopg2.connect(
#         host = "127.0.0.1",
#         user = "postgres",
#         password="YtDktpfqE,mtn",
#         database=db
#         )



#создание базы данных
async def create_db(dbname):
    conn = sq.connect(dbname)
    curs = conn.cursor()

    conn.commit()
    
    # print("База данных успешно создана")


    # добавление всех таблиц в базу       

    curs.execute(
            """CREATE TABLE IF NOT EXISTS food(
            fio TEXT,
            food TEXT,
            volume REAL,
            time INTEGER,
            date TEXT)""")

    curs.execute(
            """CREATE TABLE sleep(
            fio TEXT,            
             number_of_hours REAL,
            date TEXT)""")
        
    curs.execute(
            """CREATE TABLE toilet(
            fio TEXT,
            quantity TEXT,
            date TEXT)""")
        
    curs.execute(
            """CREATE TABLE about_the_child(
             fio TEXT,
             gender TEXT,
             date_of_birth TEXT)""")

    curs.execute(
            """CREATE TABLE polyclinic(
            fio TEXT,             
             height REAL,
             weight REAL,
             date TEXT)""")

    curs.execute(
            """CREATE TABLE reminder(
            fio TEXT,             
             doctor TEXT,             
             time INTEGER,
             date TEXT)""")
    conn.commit()


#добавление еды
async def add_data_food(dbname, fio, food, volume, time, data):
    conn = sq.connect(dbname)
    curs = conn.cursor()

    
    value = (fio, food, volume, time, data)    
    curs.execute(
			"""INSERT INTO food (fio, food, volume, time, date) VALUES
			(?, ?, ?, ?, ?)""", value)
    conn.commit()
    print("[INFO] Data was succesfully inserted")

#добавление сна
async def add_data_sleep(dbname, fio, quantity_sleep, data):
    conn = sq.connect(dbname)
    curs = conn.cursor()

    value = (fio, quantity_sleep, data)
    
    curs.execute(
			"""INSERT INTO sleep (fio, number_of_hours, date) VALUES
			(?, ?, ?)""", value)
    conn.commit()
    print("[INFO] Data was succesfully inserted")

#добавление туалета
async def add_data_toilet(dbname, fio, quantity, data):
    conn = sq.connect(dbname)
    curs = conn.cursor()

    value = (fio, quantity, data)
    
    curs.execute(
			"""INSERT INTO toilet (fio, quantity, date) VALUES
			(?, ?, ?)""", value)
    conn.commit()
    print("[INFO] Data was succesfully inserted")

#добавление нового ребенка
async def add_data_child(dbname, fio, gender, date_of_birth):
    conn = sq.connect(dbname)
    curs = conn.cursor()

    value = (fio, gender, date_of_birth)
    
    curs.execute(#тут мы пишем sql запрос для создания таблицы с нужными нам полями.
			"""INSERT INTO about_the_child (fio, gender, date_of_birth) VALUES
			(?, ?, ?)""", value)
    conn.commit()
    print("[INFO] Data was succesfully inserted")


#добавление записи роста и веса
async def add_data_polyclinic(dbname, fio, height, weight, data):
    conn = sq.connect(dbname)
    curs = conn.cursor()

    value = (fio, height, weight, data)
    
    curs.execute(
			"""INSERT INTO polyclinic (fio, height, weight, date) VALUES
			(?, ?, ?, ?)""", value)
    print("[INFO] Data was succesfully inserted")


#добавление строки в таблицу для напоминания записи к врачу
async def add_data_doctor(dbname, fio, doctor, time, data):
    conn = sq.connect(dbname)
    curs = conn.cursor()

    value = (fio, doctor, time, data)
    
    curs.execute(
			"""INSERT INTO reminder (fio, doctor, time, date) VALUES
			(?, ?, ?, ?)""", value)
    print("[INFO] Data was succesfully inserted")


#функция для выделения ФИО из таблицы списка детей по последней дате
async def change_fio(db):
    conn = sq.connect(db)
    curs = conn.cursor()

    
    curs.execute(
			"""SELECT fio FROM about_the_child WHERE date_of_birth = (SELECT MAX(date_of_birth) FROM about_the_child);"""
		)
    res = curs.fetchone()
    return res

#получение данных из таблицы за период
async def extract_table(tb, db, begin, end):
    conn = sq.connect(db)
    curs = conn.cursor()

    
    curs.execute(f"SELECT * from '{tb}' WHERE date >= '{begin}' and date <= '{end}'")
    a = curs.fetchall()
    return a


#вывод последней позиции по текущей дате
async def extract_table_today(tb, db, data):
    conn = sq.connect(db)
    curs = conn.cursor()
    
    curs.execute(f"SELECT * FROM '{tb}' WHERE {data} = (SELECT MAX({data}) FROM '{tb}')")
    return curs.fetchall()


#просмотр всей таблицы
async def extract_table_all(tb, db):
    conn = sq.connect(db)
    curs = conn.cursor()
    
    curs.execute(f"""SELECT * FROM {tb}""")
    return curs.fetchall()


#Удаление строки из таблицы
async def delete_row(tb, db, data):#data это название поля даты или времени из таблицы SQL, tb название таблицы из SQL, db это название базы из SQL
    conn = sq.connect(db)
    curs = conn.cursor()

    
    curs.execute(f"""DELETE FROM {tb} WHERE {data} = (SELECT MAX({data}) FROM {tb})""")

#подтягивание даты и времени из таблицы напоминаний
async def change_time_date(db):
    conn = sq.connect(db)
    curs = conn.cursor()
    
    curs.execute("""SELECT date, time, doctor FROM reminder""")
    dt = curs.fetchall()

    return dt


