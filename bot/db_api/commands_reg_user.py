import sqlite3 as sq


async def add_user(user_id: int, first_name: str, last_name: str, user_name: str):#добавление пользователя, точнее записи в БД
    conn = sq.connect('users.db')
    cur = conn.cursor()
    
    k = (user_id, first_name, last_name, user_name)

    cur.execute("""CREATE TABLE IF NOT EXISTS list_users(
        user_id INTEGER,
        first_name TEXT,
        last_name TEXT,
        user_name TEXT
        ) """)
    
    conn.commit()

    cur.execute("SELECT * FROM list_users")
    t = cur.fetchall()  

    if k not in t:
        cur.execute("INSERT INTO list_users (user_id, first_name, last_name, user_name) VALUES (?, ?, ?, ?)", k)
        conn.commit()


    



