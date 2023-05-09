import emoji
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from db_api import table_commands
from keyboard.default import kb_menu
from keyboard.inline import ikb_toilet
from loader import dp
from states import State_toilet

@dp.message_handler(text='Отмена', state=[State_toilet.toilet])
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Что дальше?', reply_markup=kb_menu)

@dp.callback_query_handler(text='Время_т')
async def bot_reg(call: types.CallbackQuery):
    toilet = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await call.message.answer('Напишите - как покакал ваш ребенок.', reply_markup=toilet)
    await State_toilet.toilet.set()


@dp.message_handler(state=State_toilet.toilet)
async def add_toilet(message: types.Message, state: FSMContext):
    await state.update_data(toilet=message.text)

    data = await state.get_data()
    toilet = data.get('toilet')

    db_name = 'pups_his' + str(message.from_user.id)

    from datetime import datetime
    try:
        fio = await table_commands.change_fio(db=db_name)
        await table_commands.add_data_toilet(dbname=db_name, fio=fio, quantity=toilet, data=str(datetime.now()))
        print(str(datetime.now()))
    except Exception as _ex:
        print(_ex)
        await message.answer('Что-то пошло не так! Попробуйте еще раз.')
    finally:
        await message.answer('Что дальше?', reply_markup=ikb_toilet)
        await state.finish()


@dp.callback_query_handler(text='посмотреть_туалет')
async def bot_call(call: types.CallbackQuery):
    t = await table_commands.extract_table_all(tb="toilet", db="pups_his" + str(call.message.chat.id))
    from datetime import datetime
    try:
        t = [
        [str(j) if type(j) != datetime else str(j)[:-13] for j in i]
        for i in t
        ]
        data = f'<b>Дата: {t[0][2]}</b>\n'
        res = []
        for i in range(len(t)):
            if data != f'<b>Дата: {t[i][2]}</b>\n':
                data = f'<b>Дата: {t[i][2]}</b>\n'
            if data not in res:
                res.append(data)

            for j in range(1, len(t[i]) - 1):
                if j == 1:
                    if len(t[i][j]) < 7:
                        res.append(f"{emoji.emojize(':tornado:')}" + "В этот раз " + t[i][j] + "\n")
                    else:
                        res.append(f"{emoji.emojize(':tornado:')}" + "В этот раз " + t[i][j] + "\n")
                    continue

        res = "<b>ФИО: </b>" + f"<b>{t[0][0]}</b>" + f"\n{emoji.emojize(':toilet:')}" \
                                                 f"<b>Список туалета</b>{emoji.emojize(':toilet:')}" + "\n" + "".join(res)

        await call.message.answer(text=res)

    except Exception as _ex:
        await call.message.answer("Что-то пошло не так!")
        print(_ex)
    finally:
        await call.message.answer("Что дальше?", reply_markup=ikb_toilet)



@dp.callback_query_handler(text='удалить_туалет')
async def view_info(call: types.CallbackQuery):
    try:
        await table_commands.delete_row(tb="toilet", db="pups_his" + str(call.message.chat.id), data="date")
        await call.message.answer(text="Вы удалили запись с самой поздней датой.")
    except Exception as _ex:
        await call.message.answer(text="Что-то пошло не так!")
    finally:
        await call.message.answer(text="Что дальше?", reply_markup=ikb_toilet)



