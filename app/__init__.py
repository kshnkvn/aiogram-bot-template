from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config
from app.localization import Localization

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

locale = Localization(config.LOCALES_DIR)


def create_app():
    # в моммент создания объекта бота импорт обработчиков
    from app import handlers

    return dp
