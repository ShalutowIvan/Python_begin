from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#кнопки в одном списке будут идти одной строкой, в разных списках, разными строками
kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Вход'),
            KeyboardButton(text='Регистрация'),
            KeyboardButton(text='Помощь')
        ]
    ],
    resize_keyboard=True
)

