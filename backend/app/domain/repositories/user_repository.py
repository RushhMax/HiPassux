from app.domain.entities.user import db, User
from app.domain.repositories.base_repository import BaseRepository
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
    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()
    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
    @staticmethod
    def get_user_by_username(username):
        return db.session.query(User).filter_by(username=username).first()

    
    @staticmethod
    def verify_user(username, password):
        user = UserRepository.get_user_by_username(username)
        if user and user.password == password:
            return user
        return None
