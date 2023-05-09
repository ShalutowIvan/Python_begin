from aiogram import types
from loader import dp
from keyboard.inline import ikb_menu, ikb_food, ikb_sleep, ikb_toilet, ikb_info, ikb_poly, ikb_child, ikb_doctor


@dp.message_handler(text='Вход')#при нажатии на кнопку Инлайн меню появляется инлайн меню
async def show_inline_menu(message: types.Message):
    await message.answer('Выберите нужный вам пункт меню', reply_markup=ikb_menu)

@dp.callback_query_handler(text='Еда')
async def send_message(call: types.CallbackQuery):
    await call.message.edit_reply_markup(ikb_food)#отредактировали меню

@dp.callback_query_handler(text="Сон")
async def send_message(call: types.CallbackQuery):
    await call.message.edit_reply_markup(ikb_sleep)#отредактировали меню

@dp.callback_query_handler(text='Туалет')
async def send_message(call: types.CallbackQuery):
    await call.message.edit_reply_markup(ikb_toilet)

@dp.callback_query_handler(text='Инфа')
async def send_message(call: types.CallbackQuery):
    await call.message.edit_reply_markup(ikb_info)

@dp.callback_query_handler(text='запись_врач')
async def send_message(call: types.CallbackQuery):
    await call.message.edit_reply_markup(ikb_doctor)

@dp.callback_query_handler(text='рост_вес')
async def send_message(call: types.CallbackQuery):
    await call.message.edit_reply_markup(ikb_poly)

@dp.callback_query_handler(text='инфо_о_ребенке')
async def send_message(call: types.CallbackQuery):
    await call.message.edit_reply_markup(ikb_child)


@dp.callback_query_handler(text='Назад')
async def send_message(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ikb_menu)

@dp.callback_query_handler(text='Назад_д')
async def send_message(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ikb_info)