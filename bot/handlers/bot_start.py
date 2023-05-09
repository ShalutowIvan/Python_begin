#новый файл для старта с регистрацией пользователя по профилю из телеги
from aiogram import types

from loader import dp
from db_api import commands_reg_user as commands
from keyboard.default import kb_menu

@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    try:
        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                user_name=message.from_user.username)
        await message.answer('Ты успешно зарегистрировался!', reply_markup=kb_menu)
    except Exception as _ex:
        print(_ex)
        await message.answer('Доброго времени суток!', reply_markup=kb_menu)






