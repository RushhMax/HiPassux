from flask import Blueprint, request
from app.domain.entities.user import db, User  # importante tienes que poner el directorio del modelo de tu tabla
from datetime import datetime

routes = Blueprint('routes', __name__)

@routes.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
    try:
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birth_date = datetime.strptime(request.form['birth_date'], '%Y-%m-%d')
        phone_number = request.form.get('phone_number')
        gender = request.form.get('gender')
        email = request.form['email']
        password = request.form['password']

        nuevo_usuario = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            phone_number=phone_number,
            gender=gender,
            email=email,
            password=password
        )

        db.session.add(nuevo_usuario)
        db.session.commit()

        return 'Usuario creado exitosamente!', 200  # Mensaje de éxito con código de estado 200

    except Exception as e:
    
        return f'Ocurrió un error: {e}', 500  # Mensaje de error con código de estado 500

def init_routes(app):
    app.register_blueprint(routes)
