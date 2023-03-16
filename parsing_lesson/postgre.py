# pip install -U psycopg2-binary это библиотека для работы с БД postgresql. У библиотеки есть документация
import psycopg2
from config import host, user, password, db_name, port

try:
	#подлключаемся к базе, создаем объект psycopg2
	connection = psycopg2.connect(
		host=host,
		user=user,
		password=password
		database=db_name
		)
	#также нужно создать объект курсор для выполнения sql команд
	cursor = connection.cursor()#можно просто создать переменную


except Exception as _ex:
	print("[INFO] Error while working with PosgreSQL", _ex)
finally:
	#пропишем закрытие соединения с БД
	if connection:
		connection.close()
		print("[INFO] PosgreSQL conncetion closed")





