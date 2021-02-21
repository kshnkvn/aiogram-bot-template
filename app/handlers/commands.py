from aiogram import types

from app import dp, locale


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    '''Обработчик команды /start
    '''

    await message.answer(locale.t['commands']['start'])
