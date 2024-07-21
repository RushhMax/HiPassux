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