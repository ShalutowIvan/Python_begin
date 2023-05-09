from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from db_api import table_commands
from keyboard.default import kb_menu
from keyboard.inline import ikb_food
from loader import dp
from states import State_food, State_food_report
import emoji

@dp.message_handler(text='Отмена', state=[State_food.food, State_food.volume, State_food.time, State_food_report.begin, State_food_report.end])
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Что дальше?', reply_markup=kb_menu)

@dp.message_handler(text='Отмена', state=[State_food_report.begin, State_food_report.end])
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Что дальше?', reply_markup=kb_menu)

@dp.callback_query_handler(text='пища')
async def bot_reg(call: types.CallbackQuery):
    food = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await call.message.answer('Вы находитесь в меню ввода еды')
    await call.message.answer('Напишите, что кушал малыш?', reply_markup=food)
    await State_food.food.set()


@dp.message_handler(state=State_food.food)
async def add_food(message: types.Message, state: FSMContext):
    await state.update_data(food=message.text)
    volume = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer("Введите объем еды в миллилитрах одной цифрой", reply_markup=volume)
    await State_food.volume.set()

@dp.message_handler(state=State_food.volume)
async def add_volume(message: types.Message, state: FSMContext):
    await state.update_data(volume=message.text)
    time = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer("Напишите время кормления в формате часы.минуты", reply_markup=time)
    await State_food.time.set()


@dp.message_handler(state=State_food.time)
async def add_time(message: types.Message, state: FSMContext):
    await state.update_data(time=message.text)
    data = await state.get_data()
    food = data.get('food')
    volume = data.get('volume')
    time = data.get('time')

    db_name = 'pups_his' + str(message.from_user.id) + ".db"
    from datetime import datetime
    try:
        #получение фио из таблицы детей
        fio = await table_commands.change_fio(db=db_name)
        #преобразование времени
        time = "".join([i for i in time if i.isdigit()])
        time = time[:2] + ":" + time[2:]
        if int(time[:2]) > 23:
            time = time[3:] + ":" + time[:2]
        if not volume.isdigit():
            al = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz"
            volume = "".join([x if x.lower() not in al else "" for x in volume])
        if "," in volume:
            volume = volume.replace(",", ".")
        elif "-" in volume:
            volume = volume.replace("-", ".")
        elif "/" in volume:
            volume = volume.replace("/", ".")

        await table_commands.add_data_food(dbname=db_name, fio=fio, food=food, volume=volume, time=time, data=str(datetime.now()))
        await message.answer('Данные внесены успешно')
    except Exception as _ex:
        print(_ex)
        await message.answer(text="Что-то пошло не так! Попробуйте еще раз.")
    finally:
        await message.answer('Что дальше?', reply_markup=ikb_food)
        await state.finish()


#запуск машины состояний для отчета за период
@dp.callback_query_handler(text='посмотреть_пищу')
async def view_food(call: types.CallbackQuery):
    canc = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await call.message.answer('Введите дату начала отчета.', reply_markup=canc)
    await State_food_report.begin.set()


@dp.message_handler(state=State_food_report.begin)
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
    await State_food_report.end.set()

@dp.message_handler(state=State_food_report.end)
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

        begin = begin + " 00:00:00"
        end = end + " 23:59:00"

        #присвоение отчета по дате
        t = await table_commands.extract_table(tb="food", db='pups_his' + str(message.from_user.id), begin=begin, end=end)

        #форматирование отчета
        from datetime import datetime, time
        t = [
            [str(j) if type(j) != datetime else str(j)[:-16] for j in i]
            for i in t
            ]
        data = f'<b>Дата: {t[0][4]}</b>\n'
        res = []
        for i in range(len(t)):
            if data != f'<b>Дата: {t[i][4]}</b>\n':
                data = f'<b>Дата: {t[i][4]}</b>\n'
            if data not in res:
                res.append(data)

            for j in range(1, len(t[i]) - 1):
                if j == 1:
                    if len(t[i][j]) < 20:
                        res.append(emoji.emojize(':baby_bottle:') + t[i][j] + " " * (20 - len(t[i][j])))
                    else:
                        res.append(emoji.emojize(':baby_bottle:') + t[i][j])
                if j == 2:
                    if len(t[i][j]) < 7:
                        res.append(emoji.emojize(':baby_bottle:') + t[i][j] + " " * (7 - len(t[i][j])))
                    else:
                        res.append(emoji.emojize(':baby_bottle:') + t[i][j])

                if j == 3:
                    res.append(emoji.emojize(':baby_bottle:') + t[i][j] + f"{emoji.emojize(':baby_bottle:')}\n")
                    continue

        res = "<b>ФИО: </b>" + f"<b>{t[0][0]}</b>" + f"\n{emoji.emojize(':baby_bottle:')}" \
                                  f"<b>        Пища        </b>" \
                                  f"{emoji.emojize(':baby_bottle:')}" \
                                  f"<b>Объем</b>" \
                                  f"{emoji.emojize(':baby_bottle:')}" \
                                  f"<b>Время</b>" \
                                  f"{emoji.emojize(':baby_bottle:')}" + "\n" + "".join(res)

        await message.answer(text=res)
    except Exception as _ex:
        await message.answer("Что-то пошло не так!")
        print(_ex)
    finally:
        await message.answer("Что дальше?", reply_markup=ikb_food)
        await state.finish()

@dp.callback_query_handler(text='последняя_пища')
async def view_food_last(call: types.CallbackQuery):
    t = await table_commands.extract_table_today(tb="food", db='pups_his' + str(call.message.chat.id), data="date")
    from datetime import datetime
    t = [
        [str(j) if type(j) != datetime else str(j)[:-16] for j in i]
        for i in t
    ]
    if len(t[0][1]) < 30:
        space = 30 - len(t[0][1])
    t = "<b>ФИО: </b>" + f"<b>{t[0][0]}</b>" + f"\n{emoji.emojize(':baby_bottle:')}" \
                                                 f"<b>        Пища        </b>" \
                                                 f"{emoji.emojize(':baby_bottle:')}" \
                                                 f"<b>Объем</b>" \
                                                 f"{emoji.emojize(':baby_bottle:')}" \
                                                 f"<b>Время</b>" \
                                                 f"{emoji.emojize(':baby_bottle:')}" + "\n" + f"<b>{t[0][4]}</b>\n{emoji.emojize(':baby_bottle:')}{t[0][1]}" + " " * space + "          ".join(t[0][2:4])
    await call.message.answer(text=t, reply_markup=ikb_food)


@dp.callback_query_handler(text='Удалить_пищу')
async def delete_food(call: types.CallbackQuery):
    try:
        await table_commands.delete_row(tb="food", db="pups_his" + str(call.message.chat.id), data="date")
        await call.message.answer(text="Вы удалили запись с самым поздним временем.")
    except Exception as _ex:
        await call.message.answer(text="Что-то пошло не так!")
    finally:
        await call.message.answer(text="Что дальше?", reply_markup=ikb_food)




