from app.domain.entities.user import db, User
from werkzeug.security import generate_password_hash
from datetime import datetime

class UserService:
    @staticmethod
    def update_user(user_id, data):
        try:
            usuario = User.query.get(user_id)
            if not usuario:
                return None

            if 'username' in data:
                usuario.username = data['username']
            if 'first_name' in data:
                usuario.first_name = data['first_name']
            if 'last_name' in data:
                usuario.last_name = data['last_name']
            if 'birth_date' in data:
                try:
                    usuario.birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d')
                except ValueError:
                    return {'error': 'Formato de fecha inválido.'}
            if 'phone_number' in data:
                usuario.phone_number = data['phone_number']
            if 'gender' in data:
                usuario.gender = data['gender']
            if 'email' in data:
                usuario.email = data['email']
            if 'password' in data:
                usuario.password = generate_password_hash(data['password'], method='sha256')

            db.session.commit()
            return usuario

        except Exception as e:
            db.session.rollback()
            return {'error': f'Ocurrió un error: {str(e)}'}

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_all_users():
        return User.query.all()