from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_food = InlineKeyboardMarkup(row_width=3,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Указать время приема пищи', callback_data='пища'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Отчет за период', callback_data='посмотреть_пищу'),
                                        InlineKeyboardButton(text='Последняя запись', callback_data='последняя_пища'),
                                        InlineKeyboardButton(text='Удалить', callback_data='Удалить_пищу')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Назад', callback_data='Назад')
                                    ]
                                ])


