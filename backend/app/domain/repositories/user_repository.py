from app.domain.entities.user import db, User
from app.domain.repositories.base_repository import BaseRepository

class UserRepository(BaseRepository):

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
    def remove(user):
        db.session.delete(user)
        db.session.commit()
        # Elimina un usuario de la base de datos y confirma la transacción.
    
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
        # Obtener inforacion sobre un usuario en especifico
    
    @staticmethod
    def update(user):
        db.session.commit()  # Commit los cambios ya que `user` ya está en la sesión
    
    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()
        # verificar el username 


