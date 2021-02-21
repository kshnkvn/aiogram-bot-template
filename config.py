from os import path, getenv

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = path.abspath(path.dirname(__file__))
LOCALES_DIR = path.join(BASE_DIR, 'locales')

BOT_TOKEN = getenv('BOT_TOKEN')
