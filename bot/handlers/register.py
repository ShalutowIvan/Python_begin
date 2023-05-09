from aiogram import types
from db_api import table_commands as comm
from loader import dp



@dp.message_handler(text='Регистрация')
async def register(message: types.Message):
    dbname = 'pups_his' + str(message.from_user.id) + ".db"
    try:
        await comm.create_db(dbname)
        await message.answer("Вы успешно зарегистрированы!")
    except Exception as _ex:
        print(_ex)
        await message.answer("Вы уже зарегистрированы и можете воспользоваться входом!")

    # try:
    #     await comm.add_tables(dbname)
    # except Exception as err:
    #     print("Таблицы уже созданы", err)













