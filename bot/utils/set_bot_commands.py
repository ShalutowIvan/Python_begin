from aiogram import types
#тут кнопки для основных команд меню, которое внизу слева
async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
    ])
