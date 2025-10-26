from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
import config
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.survey import router as survey_router

bot = Bot(config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

dp.include_router(survey_router)


@dp.message(Command('start'))
async def start_command(message: Message):
    user_name = message.from_user.first_name
    await message.answer(f'Привет, {user_name}! Я бот на aiogram!')


@dp.message(Command('help'))
async def help_command(message: Message):
    help_text = '''
    Доступные команды:
    /start - начать работу
    /help - показать справку
    /echo - эхо-ответ
    /survey - пройти опрос
    '''
    await message.answer(help_text)


@dp.message(Command('echo'))
async def echo_command(message: Message):
    await message.answer(f'Напиши и я повторю твой текст!')


@dp.message(F.text.lower().startswith('привет'))
async def hello_handler(message: Message):
    await message.answer('Привет-привет!')


@dp.message(F.text.contains('как дела'))
async def how_are_you_handler(message: Message):
    await message.answer('Дела хорошо! Работаю на aiogram!')


@dp.message(F.text.contains('погода'))
async def weather_handler(message: Message):
    await message.answer('Пока не могу ничего сказать по погоде :(')


async def main():
    print('Бот запущен!')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())