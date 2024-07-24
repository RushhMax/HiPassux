from flask import Blueprint, render_template, request , redirect, url_for
from app.domain.services.user_service import UserService
from datetime import datetime
bp = Blueprint('user', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    return render_template('users.html', users=users)

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

            return redirect(url_for('user.get_users'))  # Redirige después de crear el usuario

        except Exception as e:
            return render_template('register.html', error=f'Ocurrió un error: {e}')
    
    # Si es GET, simplemente muestra el formulario
    return render_template('register.html')


@bp.route('/update/<int:user_id>', methods=['GET', 'POST'])
def actualizar_usuario(user_id):
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            birth_date = datetime.strptime(request.form.get['birth_date'], '%Y-%m-%d')
            phone_number = request.form.get('phone_number')
            gender = request.form.get('gender')
            email = request.form.get('email')
            password = request.form.get('password')

            # Convertir la fecha si está presente
            if birth_date:
                try:
                    birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
                except ValueError:
                    return render_template('actualizar_perfil.html', error='Formato de fecha inválido.', user_id=user_id)

            # Llamar al servicio para actualizar el usuario
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

            if 'error' in result:
                return render_template('actualizar_perfil.html', error=result['error'], user_id=user_id)

            return redirect(url_for('user.get_users'))

        except Exception as e:
            return render_template('actualizar_perfil.html', error=f'Ocurrió un error: {e}', user_id=user_id)
    
    # Si es GET, mostrar el formulario con los datos del usuario
    user = UserService.get_user_by_id(user_id)
    if user:
        return render_template('actualizar_perfil.html', user=user)
    else:
        return render_template('actualizar_perfil.html', error='Usuario no encontrado.', user_id=user_id)