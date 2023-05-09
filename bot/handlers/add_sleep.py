import emoji
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboard.inline import ikb_sleep
from db_api import table_commands
from keyboard.default import kb_menu
from loader import dp
from states import State_sleep, State_sleep_report


@dp.message_handler(text='Отмена', state=[State_sleep.sleep, State_sleep_report.begin, State_sleep_report.end])
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Что дальше?', reply_markup=kb_menu)

@dp.callback_query_handler(text='Время_сна')
async def bot_call(call: types.CallbackQuery):
    sleep = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await call.message.answer('Введите количество часов сна', reply_markup=sleep)
    await State_sleep.sleep.set()


@dp.message_handler(state=State_sleep.sleep)
async def add_sl(message: types.Message, state: FSMContext):
    await state.update_data(sleep=message.text)

    data = await state.get_data()
    sleep = data.get('sleep')

    db_name = 'pups_his' + str(message.from_user.id)
    fio = await table_commands.change_fio(db=db_name)
    from datetime import date
    try:
        await table_commands.add_data_sleep(dbname=db_name, fio=fio, quantity_sleep=sleep, data=str(date.today()))
        await message.answer("Данные внесены успешно!")
    except Exception as _ex:
        await message.answer("Что-то пошло не так! Попробуйте еще раз.")
    finally:
        await message.answer("Что дальше?", reply_markup=ikb_sleep)
        await state.finish()


@dp.callback_query_handler(text='посмотреть_сон')
async def view_sleep(call: types.CallbackQuery):
    canc = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await call.message.answer('Введите дату начала отчета в формате день.месяц.год.', reply_markup=canc)
    await State_sleep_report.begin.set()


@dp.message_handler(state=State_sleep_report.begin)
async def add_volume(message: types.Message, state: FSMContext):
    await state.update_data(begin=message.text)
    canc = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer('Введите дату конца отчета.', reply_markup=canc)
    await State_sleep_report.end.set()

@dp.message_handler(state=State_sleep_report.end)
async def add_volume(message: types.Message, state: FSMContext):
    await state.update_data(end=message.text)
    data = await state.get_data()
    begin = str(data.get('begin'))
    end = str(data.get('end'))

    try:
        #преобразование begin это дата начала периода
        if "." in begin and int(begin[:begin.find(".")]) <= 31:
            begin = begin[begin.rfind(".") + 1:] + "-" + begin[begin.find(
                ".") + 1:begin.rfind(".")] + "-" + begin[:begin.find(".")]
        elif "," in begin and int(begin[:begin.find(",")]) <= 31:
            begin = begin[begin.rfind(",") + 1:] + "-" + begin[begin.find(
                ",") + 1:begin.rfind(",")] + "-" + begin[:begin.find(",")]
        elif "-" in begin and int(begin[:begin.find("-")]) <= 31:
            begin = begin[begin.rfind("-") + 1:] + "-" + begin[begin.find(
                "-") + 1:begin.rfind("-")] + "-" + begin[:begin.find("-")]
        elif "/" in begin and int(begin[:begin.find("/")]) <= 31:
            begin = begin[begin.rfind("/") + 1:] + "-" + begin[begin.find(
                "/") + 1:begin.rfind("/")] + "-" + begin[:begin.find("/")]
        elif ":" in begin and int(begin[:begin.find(":")]) <= 31:
            begin = begin[begin.rfind(":") + 1:] + "-" + begin[begin.find(
                ":") + 1:begin.rfind(":")] + "-" + begin[:begin.find(":")]
        # преобразование end это дата конца периода
        if "." in end and int(end[:end.find(".")]) <= 31:
            end = end[end.rfind(".") + 1:] + "-" + end[end.find(
                ".") + 1:end.rfind(".")] + "-" + end[:end.find(".")]
        elif "," in end and int(end[:end.find(",")]) <= 31:
            end = end[end.rfind(",") + 1:] + "-" + end[end.find(
                ",") + 1:end.rfind(",")] + "-" + end[:end.find(",")]
        elif "-" in end and int(end[:end.find("-")]) <= 31:
            end = end[end.rfind("-") + 1:] + "-" + end[end.find(
                "-") + 1:end.rfind("-")] + "-" + end[:end.find("-")]
        elif "/" in end and int(end[:end.find("/")]) <= 31:
            end = end[end.rfind("/") + 1:] + "-" + end[end.find(
                "/") + 1:end.rfind("/")] + "-" + end[:end.find("/")]
        elif ":" in end and int(end[:end.find(":")]) <= 31:
            end = end[end.rfind(":") + 1:] + "-" + end[end.find(
                ":") + 1:end.rfind(":")] + "-" + end[:end.find(":")]

        # begin = begin + " 00:00:00"
        # end = end + " 23:59:00"

        #присвоение отчета по дате
        t = await table_commands.extract_table(tb="sleep", db='pups_his' + str(message.from_user.id), begin=begin, end=end)

        #форматирование отчета
        from datetime import datetime, time
        t = [
            [str(j) if type(j) != datetime else str(j)[:-9] for j in i]
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
                    if len(t[i][j]) < 5:
                        res.append(f"{emoji.emojize(':alarm_clock:')}" + t[i][j] + " чс" + "\n")
                    else:
                        res.append(f"{emoji.emojize(':alarm_clock:')}" + t[i][j] + " чс" + "\n")
                    continue

        res = "<b>ФИО: </b>" + f"<b>{t[0][0]}</b>" + f"\n{emoji.emojize(':sleeping_face:')}" \
                                  f"<b>Количество часов сна</b>{emoji.emojize(':sleeping_face:')}" + "\n" + "".join(res)

        await message.answer(text=res)
    except Exception as _ex:
        await message.answer("Что-то пошло не так!")
        print(_ex)
    finally:
        await message.answer("Что дальше?", reply_markup=ikb_sleep)
        await state.finish()


@dp.callback_query_handler(text='удалить_сон')
async def view_info(call: types.CallbackQuery):
    try:
        await table_commands.delete_row(tb="sleep", db="pups_his" + str(call.message.chat.id), data="date")
        await call.message.answer(text="Вы удалили запись с самой поздней датой.")
    except Exception as _ex:
        await call.message.answer(text="Что-то пошло не так!")
    finally:
        await call.message.answer(text="Что дальше?", reply_markup=ikb_sleep)



