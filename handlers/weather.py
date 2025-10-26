from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.weather import WeatherStates

router = Router()


@router.message(Command('weather'))
async def start_weather(message: types.Message, state: FSMContext):
    """Начинаем диалог о погоде"""
    await message.answer("В каком городе хотите узнать погоду?")
    await state.set_state(WeatherStates.waiting_city)


@router.message(WeatherStates.waiting_city)
async def handle_city(message: types.Message, state: FSMContext):
    """Обрабатываем ввод города"""
    city = message.text
    # Здесь будет запрос к погодному API
    await message.answer(f"Погода в {city}: 20°C, солнечно 🌤")
    await state.clear()