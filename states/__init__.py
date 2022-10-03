from aiogram.dispatcher.filters.state import StatesGroup, State

class Request_reg(StatesGroup):
    
    header = State()
    text = State()
    time_or_remind = State()
    time = State()
    confirm = State()