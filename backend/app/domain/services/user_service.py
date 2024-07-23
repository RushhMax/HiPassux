from app.domain.repositories.user_repository import User,UserRepository

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