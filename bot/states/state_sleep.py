from aiogram.dispatcher.filters.state import StatesGroup, State

class State_sleep(StatesGroup):
    sleep = State()

class State_sleep_report(StatesGroup):
    begin = State()
    end = State()
