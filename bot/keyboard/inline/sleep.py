from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboard.inline import ikb_menu

ikb_sleep = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Указать время сна', callback_data='Время_сна'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Отчет', callback_data='посмотреть_сон'),
                                        InlineKeyboardButton(text='Удалить', callback_data='удалить_сон'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Назад', callback_data='Назад')
                                    ]

                                ])


