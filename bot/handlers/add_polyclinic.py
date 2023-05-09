from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from db_api import table_commands
from keyboard.default import kb_menu
from keyboard.inline import ikb_info, ikb_poly
from loader import dp
from states import State_polyclinic
import emoji

@dp.message_handler(text='Отмена', state=[State_polyclinic.height, State_polyclinic.weight, State_polyclinic.dat])
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Что дальше?', reply_markup=kb_menu)

@dp.callback_query_handler(text='добавить_рост_вес')
async def bot_beg(call: types.CallbackQuery):
    canc = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await call.message.answer('Введите рост ребенка одной цифрой в единице измерения СМ, можно вводить целые и дробные числа', reply_markup=canc)
    await State_polyclinic.height.set()


@dp.message_handler(state=State_polyclinic.height)
async def add_height(message: types.Message, state: FSMContext):
    await state.update_data(height=message.text)
    canc = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer("Введите вес ребенка одной цифрой в единице измерения КГ, можно вводить целые и дробные числа", reply_markup=canc)
    await State_polyclinic.weight.set()

@dp.message_handler(state=State_polyclinic.weight)
async def add_weight(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    canc = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer("Введите дату измерения роста и веса в формате день.месяц.год или год.месяц.день", reply_markup=canc)
    await State_polyclinic.dat.set()

@dp.message_handler(state=State_polyclinic.dat)
async def add_weight(message: types.Message, state: FSMContext):
    await state.update_data(dat=message.text)
    data = await state.get_data()
    height = data.get('height')
    weight = data.get('weight')
    dat = data.get('dat')
    db_name = 'pups_his' + str(message.from_user.id)
    try:
        if "." in dat and int(dat[:dat.find(".")]) <= 31:
            dat = dat[dat.rfind(".") + 1:] + "-" + dat[dat.find(
                ".") + 1:dat.rfind(".")] + "-" + dat[:dat.find(".")]
        elif "," in dat and int(dat[:dat.find(",")]) <= 31:
            dat = dat[dat.rfind(",") + 1:] + "-" + dat[dat.find(
                ",") + 1:dat.rfind(",")] + "-" + dat[:dat.find(",")]
        elif "-" in dat and int(dat[:dat.find("-")]) <= 31:
            dat = dat[dat.rfind("-") + 1:] + "-" + dat[dat.find(
                "-") + 1:dat.rfind("-")] + "-" + dat[:dat.find("-")]
        elif "/" in dat and int(dat[:dat.find("/")]) <= 31:
            dat = dat[dat.rfind("/") + 1:] + "-" + dat[dat.find(
                "/") + 1:dat.rfind("/")] + "-" + dat[:dat.find("/")]
        elif ":" in dat and int(dat[:dat.find(":")]) <= 31:
            dat = dat[dat.rfind(":") + 1:] + "-" + dat[dat.find(
                ":") + 1:dat.rfind(":")] + "-" + dat[:dat.find(":")]

        fio = await table_commands.change_fio(db=db_name)
        await table_commands.add_data_polyclinic(dbname=db_name, fio=fio, height=height, weight=weight, data=str(dat))
        await message.answer("Данные внесены успешно!")
    except Exception as _ex:
        await message.answer("Что-то пошло не так! Попробуйте еще раз.")
    finally:
        await message.answer("Что дальше?", reply_markup=ikb_poly)
        await state.finish()


@dp.callback_query_handler(text='просмотр_рост_вес')
async def bot_call(call: types.CallbackQuery):
    t = await table_commands.extract_table_all(tb="polyclinic", db="pups_his" + str(call.message.chat.id))
    t = [[str(i[j]) if j != 1 else str(i[j]) + " см" for j in range(len(i))] for i in t]
    t = ["|".join([str(i[j]) if j != 2 else str(i[j]) + " кг" for j in range(len(i))]) for i in t]
    t = f"{emoji.emojize(':hourglass_done:')}| ФИО | Рост | Вес | Дата|{emoji.emojize(':hourglass_done:')}\n" + "\n".join(t)
    await call.message.answer(text=t, reply_markup=ikb_poly)


@dp.callback_query_handler(text='Удалить_рост_вес')
async def view_info(call: types.CallbackQuery):
    try:
        await table_commands.delete_row(tb="polyclinic", db="pups_his" + str(call.message.chat.id), data="date")
        await call.message.answer(text="Вы удалили запись с самой поздней датой.")
    except Exception as _ex:
        await call.message.answer(text="Что-то пошло не так!")
    finally:
        await call.message.answer(text="Что дальше?", reply_markup=ikb_info)




