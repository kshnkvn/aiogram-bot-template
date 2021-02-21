import json
import logging
from os import path, listdir
from json.decoder import JSONDecodeError

from aiogram import types


class Localization:
    '''Класс для реализации многоязычности

    Загружает из указанной папки JSON файлы локализации.
    Каждый файл должен иметь название в соответствии с ISO 639-1.
    Расширение файлов: .json
    Структура файлов: стандартный JSON.

    Attributes:
        locales_dir (str):
            полный путь к папке с JSON файлами локализации
    '''

    def __init__(self, locales_dir):
        self.locales_dir = path.abspath(locales_dir)
        self.__languages = self.__load_langs(self.locales_dir)
        self.__user_lang = dict()

    @property
    def available_langs(self):
        '''Список загруженных языков'''

        return tuple(self.__languages.keys())

    @property
    def t(self):
        '''Сокращение для self.text'''

        return self.text

    @property
    def text(self):
        '''Метод для получения словаря с текстами нужного языка'''

        return self.__languages[self.user_lang]

    @property
    def user_lang(self):
        '''Значение языка пользователя'''

        user = types.User.get_current()

        # TODO: убрать хард-код языка по-умолчанию в случае ошибки
        return self.__user_lang.get(user.id, 'ru')

    @user_lang.setter
    def user_lang(self, lang):
        '''Метод для установки языка пользователю

        freezed_lang используется что бы "заморозить" установленный язык
        и не дать хэндлерам устанавливать язык при каждом сообщении.
        '''

        user = types.User.get_current()

        if lang in self.available_langs:
            self.__user_lang[user.id] = lang

    def __load_langs(self, locales_dir):
        '''Загрузка доступных локализаций

        Returns:
            languages (dict): {
                <lang_name>: dict
            }
        '''

        languages = dict()

        for file in listdir(locales_dir):
            if file.endswith('.json'):
                f_path = path.join(locales_dir, file)
                lang = file.split('.')[0]

                # загрузка языка
                try:
                    languages[lang] = json.load(
                        open(f_path, 'r', encoding='utf-8'))
                except JSONDecodeError:
                    logging.exception(f'Ошибка загрузки локализации {file}')

        return languages
