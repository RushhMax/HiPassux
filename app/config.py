import os

class Config:
    #SQLALCHEMY_DATABASE_URI = f'mysql://{os.environ.get("MYSQL_USERNAME")}:{os.environ.get("MYSQL_PASSWORD")}@localhost/your_db'  # Update with your DB details
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://fernando:your_password@localhost/RedSocial') #mysql://username:password@host:port/database_name
    SQLALCHEMY_TRACK_MODIFICATIONS = False
