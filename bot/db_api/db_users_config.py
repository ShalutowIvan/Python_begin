# import psycopg2

# conn = psycopg2.connect(
#     dbname="main",
#     user="postgres",
#     password="YtDktpfqE,mtn",
#     host="127.0.0.1")
# cursor = conn.cursor()
#
# # создаем таблицу people
# cursor.execute("CREATE TABLE users (user_id bigint PRIMARY KEY, first_name character varying(200), last_name character varying(200), user_name character varying(200))")
# # поддверждаем транзакцию
# conn.commit()
# print("Таблица people успешно создана")
#
# cursor.close()
# conn.close()






# async def on_startup(dispatcher: Dispatcher):
#     print('Установка связи с postgresql')
#     await db.set_bind(config.POSTGRES_URI)



