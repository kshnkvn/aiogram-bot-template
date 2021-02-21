from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app import dp, locale, keyboards
from app.helpers import localization


@dp.callback_query_handler(lambda c: c.data.startswith('change_lang'))
async def change_language(callback: types.CallbackQuery):
    '''Список доступных языков'''

    markup = InlineKeyboardMarkup()

    # при команде формата change_lang_back возвращаемся в настройки
    if callback.data.endswith('back'):
        markup = keyboards.inlines.settigs()
    # иначе отображаем список доступных языков
    else:
        for lang in locale.available_langs:
            f_lang = localization.format_lang_name(lang)
            markup.add(InlineKeyboardButton(
                f_lang, callback_data=f'setup_lang_{lang}'))

        markup.add(InlineKeyboardButton(
            locale.t['buttons']['back'], callback_data=f'change_lang_back'))

        await callback.message.edit_text(
            locale.t['texts']['which_lang_setup'])

    await callback.message.edit_reply_markup(markup)


@dp.callback_query_handler(lambda c: c.data.startswith('setup_lang'))
async def setup_language(callback: types.CallbackQuery):
    '''Обработчик изменения языка'''

    lang = callback.data.split('_')[-1]
    locale.user_lang = lang

    markup = keyboards.inlines.settigs()

    await callback.message.edit_text(locale.t['texts']['settings'])
    await callback.message.edit_reply_markup(markup)
