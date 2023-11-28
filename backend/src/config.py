from pathlib import Path

from decouple import config 

DATABASE_URL = config('DATABASE_URL')
JWT_SECRET_KEY = config('JWT_SECRET_KEY')
TEST_DATABASE_URL = config('TEST_DATABASE_URL')
STATIC_DIR = Path(__file__).resolve().parent / 'static'
