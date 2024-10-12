from app.utils.settings import Settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionMaker

settings = Settings()

URL_CONN = settings.db_conn

