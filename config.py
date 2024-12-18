from dotenv import load_dotenv
from decouple import config


load_dotenv()

DB_URL = config('DB_URL')
