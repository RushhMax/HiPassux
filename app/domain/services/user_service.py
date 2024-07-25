from app.domain.repositories.user_repository import User,UserRepository
from werkzeug.security import generate_password_hash
from datetime import datetime
class UserService:

    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()

    @staticmethod
    def create_user(username, first_name, last_name, birth_date, phone_number, gender, email, password):
        new_user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            phone_number=phone_number,
            gender=gender,
            email=email,
            password=password
        )
        UserRepository.add_user(new_user)

    @staticmethod
    def update_user(user_id, username, first_name, last_name, birth_date, phone_number, gender, email, password=None):
        try:
            usuario = UserRepository.get_user_by_id(user_id)
            if not usuario:
                return {'error': 'Usuario no encontrado'}

            usuario.username = username
            usuario.first_name = first_name
            usuario.last_name = last_name

            if isinstance(birth_date, str):
                try:
                    usuario.birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
                except ValueError:
                    return {'error': 'Formato de fecha inválido.'}
            else:
                usuario.birth_date = birth_date

            usuario.phone_number = phone_number
            usuario.gender = gender
            usuario.email = email

            if password:
                usuario.password = generate_password_hash(password, method='sha256')

            UserRepository.update_user(usuario)
            return usuario
        except Exception as e:
            return {'error': f'Ocurrió un error al actualizar el usuario: {str(e)}'}

    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_user_by_id(user_id)