from aiogram.dispatcher.filters.state import StatesGroup, State


class State_food(StatesGroup):
    food = State()
    volume = State()
    time = State()

class State_food_report(StatesGroup):
    begin = State()
    end = State()


