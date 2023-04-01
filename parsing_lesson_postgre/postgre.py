# pip install -U psycopg2-binary это библиотека для работы с БД postgresql. У библиотеки есть документация
#Инструкция по установке linux параллельно с виндой:
# https://www.youtube.com/watch?v=mgjLDpPjlIE
#курс по sql:
# https://www.youtube.com/watch?v=OT7JGcUKWK0&list=PLqGS6O1-DZLp_UAGnZ-t49iZXKsDEts_k
import psycopg2
from config import host, user, password, db_name, port

try:
	#подлключаемся к базе, создаем объект psycopg2, и вызываем метод connect, в нем задаем параметры для подключения к БД
	connection = psycopg2.connect(
		host=host,
		user=user,
		password=password,
		database=db_name
		)
	connection.autocommit = True#прописали автокоммит, теперь изменения в БД будут автоматом записываться
	#также нужно создать объект курсор для выполнения sql команд
	# cursor = connection.cursor()#можно просто создать переменную
	#или воспользоваться менеджером контекста with
	with connection.cursor() as curs:#если мы уже подключились к БД, то можно выполнить простой sql запрос через метод execute объекта connection, который мы уже записали в переменную curs. Запрос будет на версию БД
		curs.execute("SELECT version();")#sql запрос пишется в кавычках
		print(f"Server version: {curs.fetchone()}")

	#create table in base

	# with connection.cursor() as curs:
	# 	curs.execute(#тут мы пишем sql запрос для создания таблицы с нужными нам полями.
	# 		"""CREATE TABLE users2(
	# 		id bigint PRIMARY KEY,
	# 		first_name character varying(200) NOT NULL,
	# 		nick_name character varying(200) NOT NULL);"""
	# 	)
	# 	#далее чтобы изменения записались в БД, нужно вызвать метод commit у объекта БД
	# 	#connection.commit()#но можно прописать и автокоммит
	#
	# 	print("[INFO] Table created succesfully")

	#добавление данных в таблицу
	a = (1, 'Вася', 'Молодец')
	with connection.cursor() as curs:
		curs.execute(#тут мы пишем sql запрос для создания таблицы с нужными нам полями.
			f"""INSERT INTO users (id, first_name, nick_name) VALUES
			(%s, %s, %s);""", a)
		print("[INFO] Data was succesfully insrted")

	#извлечение данных из таблицы
	# with connection.cursor() as curs:
	# 	curs.execute(#тут мы пишем sql запрос для создания таблицы с нужными нам полями.
	# 		"""SELECT * FROM users;"""
	# 	)
	# 	print(curs.fetchall())#тут вывели все поля

	# with connection.cursor() as curs:
	# 	curs.execute(#тут мы пишем sql запрос для создания таблицы с нужными нам полями.
	# 		"""SELECT nick_name FROM users WHERE first_name = 'Vasia';"""
	# 	)
	# 	print(curs.fetchone())#тут вывели только поле ник Васи в виде кортежа
	#
	#удаление все таблицы целиком
	# with connection.cursor() as curs:
	# 	curs.execute(#тут мы пишем sql запрос для создания таблицы с нужными нам полями.
	# 		"""DROP TABLE users;"""
	# 	)
	#
	# 	print("[INFO] table was deleted")
	#теперь табблица будет удалена, извлечь данные из нее больше не сможем

except Exception as _ex:
	print("[INFO] Error while working with PostgreSQL", _ex)

finally:#пропишем закрытие соединения с БД
	if connection:
		# cursor.close()#если создаем просто переменную, то нужно закрывать курсор, в случае с менеджером контекста, закрывать его не надо, так как он автоматом закрывает БД
		connection.close()
		print("[INFO] PostgreSQL conncetion closed")





