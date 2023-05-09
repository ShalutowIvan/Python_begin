from aiogram.dispatcher.filters.state import StatesGroup, State


class State_child(StatesGroup):
    fio = State()
    gender = State()
    date_of_birth = State()


