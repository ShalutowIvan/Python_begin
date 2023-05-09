from aiogram.dispatcher.filters.state import StatesGroup, State
#далее в хендлерах мы создали файл register. В ините конечно имортировали класс

class State_doctor(StatesGroup):
    doctor = State()
    tm = State()
    dt = State()

class State_doctor_report(StatesGroup):
    begin = State()
    end = State()





