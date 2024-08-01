from flask import Blueprint, render_template, request , redirect, url_for, flash
from app.domain.services.user_service import UserService
from datetime import datetime
from werkzeug.security import check_password_hash
bp = Blueprint('user', __name__)

actualizar_perfilHTML = 'actualizar_perfil.html'

@bp.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    return render_template('users.html', users=users)

def is_valid_gmail(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return re.match(pattern, email) is not None

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = request.form['username']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            birth_date = datetime.strptime(request.form['birth_date'], '%Y-%m-%d')
            phone_number = request.form.get('phone_number')
            gender = request.form.get('gender')
            email = request.form['email']
            password = request.form['password']

            UserService.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
                phone_number=phone_number,
                gender=gender,
                email=email,
                password=password
            )
            return redirect(url_for('user.get_users'))  

        except Exception as e:
            return render_template('register.html', error=f'Ocurrió un error: {e}')
    
    return render_template('register.html')


@bp.route('/update/<int:user_id>', methods=['GET', 'POST'])
def actualizar_usuario(user_id):
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            birth_date_str = request.form.get('birth_date')
            phone_number = request.form.get('phone_number')
            gender = request.form.get('gender')
            email = request.form.get('email')
            password = request.form.get('password')

            try:
                birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
            except (ValueError, TypeError):
                return render_template(actualizar_perfilHTML, error='Formato de fecha inválido.', user_id=user_id)

            result = UserService.update_user(
                user_id=user_id,
                username=username,
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
                phone_number=phone_number,
                gender=gender,
                email=email,
                password=password
            )

            if isinstance(result, dict) and 'error' in result:
                return render_template(actualizar_perfilHTML, error=result['error'], user_id=user_id)

            return redirect(url_for('user.get_users'))

        except Exception as e:
            return render_template(actualizar_perfilHTML, error=f'Ocurrió un error: {e}', user_id=user_id)

    user = UserService.get_user_by_id(user_id)
    if user:
        return render_template(actualizar_perfilHTML, user=user)
    else:
        return render_template(actualizar_perfilHTML, error='Usuario no encontrado.', user_id=user_id)
    
@bp.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = UserService.authenticate_user(username, password)
        if user:
            message = '¡Felicidades! Has iniciado sesión correctamente.'
        else:
            message = 'Nombre de usuario o contraseña incorrectos.'
    return render_template('login.html', message=message)