from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from db_api import table_commands
from keyboard.default import kb_menu
from keyboard.inline import ikb_info, ikb_child
from loader import dp
from states import State_child

@dp.message_handler(text='Отмена', state=[State_child.fio, State_child.gender, State_child.date_of_birth])
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Что дальше?', reply_markup=kb_menu)

@dp.callback_query_handler(text='добавить_ребенка')
async def bot_b(call: types.CallbackQuery):
    canc = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await call.message.answer("Вы в меню добавления ребенка")
    await call.message.answer('Введите фамилию, имя и отчество ребенка', reply_markup=canc)
    await State_child.fio.set()


@dp.message_handler(state=State_child.fio)
async def add_fio(message: types.Message, state: FSMContext):
    await state.update_data(fio=message.text)
    canc = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer("Мальчик или девочка?", reply_markup=canc)
    await State_child.gender.set()

@dp.message_handler(state=State_child.gender)
async def add_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)

    canc = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text='Отмена')
                ],
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    await message.answer("Напишите дату рождения ребенка в формате год.месяц.день или день.месяц.год", reply_markup=canc)
    await State_child.date_of_birth.set()

@dp.message_handler(state=State_child.date_of_birth)
async def add_date_of_birth(message: types.Message, state: FSMContext):
    await state.update_data(date_of_birth=message.text)
    data = await state.get_data()
    fio = data.get('fio')
    gender = data.get('gender')
    date_of_birth = data.get('date_of_birth')
    db_name = 'pups_his' + str(message.from_user.id)
    try:
        if "." in date_of_birth and int(date_of_birth[:date_of_birth.find(".")]) <= 31:
            date_of_birth = date_of_birth[date_of_birth.rfind(".") + 1:] + "-" + date_of_birth[date_of_birth.find(
                ".") + 1:date_of_birth.rfind(".")] + "-" + date_of_birth[:date_of_birth.find(".")]
        elif "," in date_of_birth and int(date_of_birth[:date_of_birth.find(",")]) <= 31:
            date_of_birth = date_of_birth[date_of_birth.rfind(",") + 1:] + "-" + date_of_birth[date_of_birth.find(
                ",") + 1:date_of_birth.rfind(",")] + "-" + date_of_birth[:date_of_birth.find(",")]
        elif "-" in date_of_birth and int(date_of_birth[:date_of_birth.find("-")]) <= 31:
            date_of_birth = date_of_birth[date_of_birth.rfind("-") + 1:] + "-" + date_of_birth[date_of_birth.find(
                "-") + 1:date_of_birth.rfind("-")] + "-" + date_of_birth[:date_of_birth.find("-")]
        elif "/" in date_of_birth and int(date_of_birth[:date_of_birth.find("/")]) <= 31:
            date_of_birth = date_of_birth[date_of_birth.rfind("/") + 1:] + "-" + date_of_birth[date_of_birth.find(
                "/") + 1:date_of_birth.rfind("/")] + "-" + date_of_birth[:date_of_birth.find("/")]
        elif ":" in date_of_birth and int(date_of_birth[:date_of_birth.find(":")]) <= 31:
            date_of_birth = date_of_birth[date_of_birth.rfind(":") + 1:] + "-" + date_of_birth[date_of_birth.find(
                ":") + 1:date_of_birth.rfind(":")] + "-" + date_of_birth[:date_of_birth.find(":")]

        await table_commands.add_data_child(dbname=db_name, fio=fio, gender=gender, date_of_birth=date_of_birth)
        await message.answer("Данные внесены успешно.")
    except Exception as _ex:
        await message.answer('Что-то пошло не так! Попробуйте еще раз!')
    finally:
        await message.answer("Что дальше?", reply_markup=ikb_child)
        await state.finish()


@dp.callback_query_handler(text='просмотр_инфо')
async def view_info(call: types.CallbackQuery):
    t = await table_commands.extract_table_today(tb="about_the_child", db="pups_his" + str(call.message.chat.id), data='date_of_birth')
    t = [ [str(j) for j in i] for i in t ]
    await call.message.answer(text=f"ФИО: {t[0][0]}\n"
                                   f"Пол: {t[0][1]}\n"
                                   f"Дата рождения: {t[0][2]}\n", reply_markup=ikb_child)

@dp.callback_query_handler(text='удалить_инфу')
async def view_info(call: types.CallbackQuery):
    try:
        await table_commands.delete_row(tb="about_the_child", db="pups_his" + str(call.message.chat.id), data="date_of_birth")
        await call.message.answer(text="Вы удалили запись с самой поздней датой.")
    except Exception as _ex:
        await call.message.answer(text="Что-то пошло не так!")
    finally:
        await call.message.answer(text="Что дальше?", reply_markup=ikb_child)

