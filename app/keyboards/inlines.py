from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app import locale


def settigs():
    '''Клавиатура настроек'''

    inline_markup = InlineKeyboardMarkup()
    inline_markup.add(InlineKeyboardButton(
        locale.t['buttons']['language'], callback_data='change_lang'))

    return inline_markup
