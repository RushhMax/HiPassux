from app.domain.entities.user import db, User

class UserRepository:

    @staticmethod
    def get_all_users():
        return User.query.all()
    
    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()
    
    @staticmethod
    def update_user(user):
        db.session.commit()
    
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
