from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboard.inline import ikb_doctor
from db_api import table_commands
from keyboard.default import kb_menu
from loader import dp
from states import State_doctor
import emoji


@dp.message_handler(text='Отмена', state=[State_doctor.doctor, State_doctor.tm, State_doctor.dt])
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Что дальше?', reply_markup=kb_menu)


@dp.callback_query_handler(text='добавить_запись_врач')
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
    await call.message.answer('Введите название врача, к которому вы записались.', reply_markup=canc)
    await State_doctor.doctor.set()

@dp.message_handler(state=State_doctor.doctor)
async def add_doctor(message: types.Message, state: FSMContext):
    await state.update_data(doctor=message.text)
    canc = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer("Введите время, на которое вы записались, в формате часы.минуты.", reply_markup=canc)
    await State_doctor.tm.set()

@dp.message_handler(state=State_doctor.tm)
async def add_weight(message: types.Message, state: FSMContext):
    await state.update_data(tm=message.text)
    canc = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer("Введите дату, на которую вы записались, в формате день.месяц.год.", reply_markup=canc)
    await State_doctor.dt.set()

@dp.message_handler(state=State_doctor.dt)
async def add_weight(message: types.Message, state: FSMContext):
    await state.update_data(dt=message.text)
    data = await state.get_data()
    doctor = data.get("doctor")
    tm = data.get("tm")
    dt = data.get("dt")
    db_name = 'pups_his' + str(message.from_user.id)
    try:
        #преобразование даты
        if "." in dt and int(dt[:dt.find(".")]) <= 31:
            dt = dt[dt.rfind(".") + 1:] + "-" + dt[dt.find(
                ".") + 1:dt.rfind(".")] + "-" + dt[:dt.find(".")]
        elif "," in dt and int(dt[:dt.find(",")]) <= 31:
            dt = dt[dt.rfind(",") + 1:] + "-" + dt[dt.find(
                ",") + 1:dt.rfind(",")] + "-" + dt[:dt.find(",")]
        elif "-" in dt and int(dt[:dt.find("-")]) <= 31:
            dt = dt[dt.rfind("-") + 1:] + "-" + dt[dt.find(
                "-") + 1:dt.rfind("-")] + "-" + dt[:dt.find("-")]
        elif "/" in dt and int(dt[:dt.find("/")]) <= 31:
            dt = dt[dt.rfind("/") + 1:] + "-" + dt[dt.find(
                "/") + 1:dt.rfind("/")] + "-" + dt[:dt.find("/")]
        elif ":" in dt and int(dt[:dt.find(":")]) <= 31:
            dt = dt[dt.rfind(":") + 1:] + "-" + dt[dt.find(
                ":") + 1:dt.rfind(":")] + "-" + dt[:dt.find(":")]
        # преобразование времени
        tm = "".join([i for i in tm if i.isdigit()])
        tm = tm[:2] + ":" + tm[2:]
        if int(tm[:2]) > 23:
            tm = tm[3:] + ":" + tm[:2]
        fio = await table_commands.change_fio(db=db_name)
        await table_commands.add_data_doctor(dbname=db_name, fio=fio, doctor=doctor, time=tm, data=dt)
        await message.answer("Данные внесены успешно!")
    except Exception as _ex:
        await message.answer("Что-то пошло не так! Попробуйте еще раз.")
    finally:
        await message.answer("Что дальше?", reply_markup=ikb_doctor)
        await state.finish()

@dp.callback_query_handler(text='смотреть_запись_врач')
async def bot_call(call: types.CallbackQuery):
    t = await table_commands.extract_table_all(tb="reminder", db="pups_his" + str(call.message.chat.id))
    t = ["|".join([str(i[j]) for j in range(1, len(i))]) for i in t]
    t = f"{emoji.emojize(':hourglass_done:')} Врач | время | дата{emoji.emojize(':hourglass_done:')}\n" + "\n".join(t)
    await call.message.answer(text=t, reply_markup=ikb_doctor)


@dp.callback_query_handler(text='удалить_запись_врач')
async def view_info(call: types.CallbackQuery):
    try:
        await table_commands.delete_row(tb="reminder", db="pups_his" + str(call.message.chat.id), data="date")
        await call.message.answer(text="Вы удалили запись с самой поздней датой.")
    except Exception as _ex:
        await call.message.answer(text="Что-то пошло не так!")
    finally:
        await call.message.answer(text="Что дальше?", reply_markup=ikb_doctor)








