from app.domain.repositories.user_repository import User,UserRepository
from werkzeug.security import generate_password_hash
from datetime import datetime

class UserService:

    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()

    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def get_user_by_username(username):
        user = UserRepository.get_user_by_username(username)
        return user

    @staticmethod
    def get_user_by_email(email):
        user = UserRepository.get_user_by_email(email)
        return user

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            UserRepository.remove(user)
            return True
        return False

    @staticmethod
    def authenticate(username, password):
        user = UserRepository.get_user_by_username(username)
        if user and user.password == password:
            return user
        return None

    @staticmethod
    def authenticate_user(username, password):
        return UserRepository.verify_user(username, password)

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
            password=generate_password_hash(password, method='pbkdf2:sha256')  # Use pbkdf2:sha256
        )
        UserRepository.add_user(new_user)
        return new_user

    @staticmethod
    def update_user(user_id, data):
        try:
            usuario = UserRepository.get_user_by_id(user_id)
            if not usuario:
                return {'error': 'Usuario no encontrado'}

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
                usuario.password = generate_password_hash(data['password'], method='pbkdf2:sha256')

            UserRepository.update_user(usuario)
            return usuario

        except Exception as e:
            return {'error': f'Ocurrió un error al actualizar el usuario: {str(e)}'}