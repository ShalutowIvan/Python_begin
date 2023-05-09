from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



ikb_info = InlineKeyboardMarkup(row_width=3,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Запись к врачу', callback_data='запись_врач'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Рост и вес', callback_data='рост_вес'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Добавить ребенка', callback_data='инфо_о_ребенке'),

                                    ],
                                    [
                                        InlineKeyboardButton(text='Назад', callback_data='Назад')
                                    ]

                                ])

ikb_doctor = InlineKeyboardMarkup(row_width=3,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Добавить запись', callback_data='добавить_запись_врач'),
                                        InlineKeyboardButton(text='Просмотр записей', callback_data='смотреть_запись_врач'),
                                        InlineKeyboardButton(text='Удалить', callback_data='удалить_запись_врач'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Включить напоминание', callback_data='включить_напоминание_врач'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Назад', callback_data='Назад_д')
                                    ]


                                ])

ikb_poly = InlineKeyboardMarkup(row_width=3,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Добавить запись', callback_data='добавить_рост_вес'),
                                        InlineKeyboardButton(text='Просмотр', callback_data='просмотр_рост_вес'),
                                        InlineKeyboardButton(text='Удалить', callback_data='Удалить_рост_вес')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Назад', callback_data='Назад_д')
                                    ]
                                ])

ikb_child = InlineKeyboardMarkup(row_width=3,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Добавить ребенка', callback_data='добавить_ребенка'),
                                        InlineKeyboardButton(text='Просмотр', callback_data='просмотр_инфо'),
                                        InlineKeyboardButton(text='Удалить', callback_data='удалить_инфу'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Назад', callback_data='Назад_д')
                                    ],
                                    ])