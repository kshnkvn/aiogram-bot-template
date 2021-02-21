from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app import dp, locale, keyboards


@dp.message_handler(lambda m: m.text == locale.t['buttons']['about'])
async def about(message: types.Message):
    '''Обработчик запроса информации'''

    await message.answer(locale.t['texts']['undefined'])


@dp.message_handler(lambda m: m.text == locale.t['buttons']['settings'])
async def settings(message: types.Message):
    '''Обработчик запроса настроек'''

    markup = keyboards.inlines.settigs()

    await message.answer(locale.t['texts']['settings'], reply_markup=markup)
