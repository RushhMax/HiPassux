from app.models.user import User

class UserRepository:

    @staticmethod
    def get_all_users():
        return User.query.all()
