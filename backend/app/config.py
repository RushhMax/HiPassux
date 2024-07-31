from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://fernando:your_password@localhost/RedSocial') #mysql://username:password@host:port/database_name
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG= True
