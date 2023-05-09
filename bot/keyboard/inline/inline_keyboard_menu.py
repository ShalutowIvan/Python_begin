from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=3,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Еда', callback_data='Еда'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Сон', callback_data='Сон'),
                                        InlineKeyboardButton(text='Туалет', callback_data='Туалет')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Информация о ребенке', callback_data='Инфа'),
                                    ]

                                ])


