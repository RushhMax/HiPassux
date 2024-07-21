from app.domain.entities.user import db, User

class UserRepository:

    @staticmethod
    def get_all_users():
        return User.query.all()
    
    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()
