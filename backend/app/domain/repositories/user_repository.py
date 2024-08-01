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