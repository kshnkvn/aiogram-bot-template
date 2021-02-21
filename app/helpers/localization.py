import logging


def format_lang_name(lang):
    '''Функция для форматирования ISO кода языка'''

    langs = {
        'en': '🇺🇸 English',
        'ru': '🇷🇺 Русский'
    }

    try:
        return langs[lang]
    except KeyError:
        logging.error(f'Для <{lang}> отсутствует форматирование!')
        return lang
