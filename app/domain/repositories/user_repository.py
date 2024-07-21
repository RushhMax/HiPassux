from app.domain.entities.user import User
from app.extensions import db
class UserRepository:

    @staticmethod
    def get_all_users():
        return User.query.all()
    