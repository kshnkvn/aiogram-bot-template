import logging
import sys

from aiogram import executor

from app import create_app

logging.basicConfig(
    handlers=[logging.StreamHandler(sys.stdout)],
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s]: %(message)s'
)

dp = create_app()


if __name__ == '__main__':
    while True:
        try:
            executor.start_polling(
                dispatcher=dp,
                skip_updates=True
            )
        except Exception:
            logging.exception(f'Ошибка polling\'а')
