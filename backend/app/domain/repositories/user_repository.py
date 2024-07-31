from app.domain.entities.user import db, User
from app.domain.repositories.base_repository import BaseRepository

class UserRepository:

    @staticmethod
    def get_all_users():
        return User.query.all()
        # Obtiene todos los usuarios de la base de datos.

    @staticmethod
    def add(user):
        db.session.add(user)
        db.session.commit()
        # Añade un usuario a la base de datos y confirma la transacción.
    
    @staticmethod
    def update_user(user):
        db.session.commit()
    
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
