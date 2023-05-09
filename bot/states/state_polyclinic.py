from aiogram.dispatcher.filters.state import StatesGroup, State


class State_polyclinic(StatesGroup):
    height = State()
    weight = State()
    dat = State()

class State_polyclinic_report(StatesGroup):
    begin = State()
    end = State()
