from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboard.inline import ikb_menu

ikb_toilet = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Указать время', callback_data='Время_т'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Просмотр', callback_data='посмотреть_туалет'),
                                        InlineKeyboardButton(text='Удалить', callback_data='удалить_туалет'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Назад', callback_data='Назад')
                                    ]

                                ])


