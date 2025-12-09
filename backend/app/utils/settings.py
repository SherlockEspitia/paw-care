from dotenv import dotenv_values
from pydantic_settings import BaseSettings

ENV = dict(dotenv_values('.env'))

class Settings(BaseSettings):
    app_name: str = 'PetCare Api'
    db_user: str = ENV['USER']
    db_pass: str = ENV['PASSWORD']
    db_name: str = ENV['DB_NAME']
    db_conn: str = ENV['DB_CONNECTION']
    secret_key: str = ENV['SECRET_KEY']
    algorithm: str = ENV['ALGORITH']
    access_token_expires_m: str = ENV['ACCESS_TOKEN_EXPIRE_MINUTES'] 
    