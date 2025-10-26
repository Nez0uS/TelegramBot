from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.survey import SurveyStates, WeatherStates


router = Router()


@router.message(Command('survey'))
async def start_survey(message: types.Message, state: FSMContext):
    await message.answer(f'Давайте проведем небольшой опрос! Как Вас зовут?')
    await state.set_state(SurveyStates.waiting_name)


@router.message(SurveyStates.waiting_name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)

    await message.answer(f'Приятно познакомиться, {message.text}! Сколько Вам лет?')
    await state.set_state(SurveyStates.waiting_age)


@router.message(SurveyStates.waiting_age)
async def process_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)

    await message.answer(f'Из какого вы города?')
    await state.set_state(SurveyStates.waiting_city)


@router.message(SurveyStates.waiting_city)
async def process_city(message: types.Message, state: FSMContext):
    user_data = await state.get_data()

    name = user_data.get('name', 'Неизвестно')
    age = user_data.get('age', 'Неизвестно')
    city = message.text

    result_text = f"""
    ✅ Спасибо за участие в опросе!

    📊 Ваши данные:
    • Имя: {name}
    • Возраст: {age}
    • Город: {city}
    """
    await message.answer(result_text)

    await state.clear()





