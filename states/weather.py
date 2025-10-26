from aiogram.fsm.state import State, StatesGroup


class WeatherStates(StatesGroup):
    waiting_city = State()
