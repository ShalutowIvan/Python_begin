from aiogram.dispatcher.filters.state import StatesGroup, State

class State_toilet(StatesGroup):
    toilet = State()

class State_toilet_report(StatesGroup):
    begin = State()
    end = State()




