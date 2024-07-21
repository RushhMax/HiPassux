from flask import Blueprint, request, jsonify
from app.models.user import db, User  # importante tienes que poner el directorio del modelo de tu tabla
from datetime import datetime
from app.domain.services.update_profile import UserService
from werkzeug.security import generate_password_hash, check_password_hash
routes = Blueprint('routes', __name__)

@routes.route('/registrar_usuario<int:user_id>', methods=['POST'])
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
@routes.route('/actualizar_usuario', methods=['PUT'])
def actualizar_usuario(user_id):
    try:
        # Obtener el usuario por ID
        usuario = User.query.get(user_id)
        if not usuario:
            return jsonify({'error': 'Usuario no encontrado.'}), 404

        # Obtener los datos del formulario
        data = request.form
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        birth_date_str = data.get('birth_date')
        phone_number = data.get('phone_number')
        gender = data.get('gender')
        email = data.get('email')
        password = data.get('password')

        # Validar y actualizar datos
        if username:
            usuario.username = username
        if first_name:
            usuario.first_name = first_name
        if last_name:
            usuario.last_name = last_name
        if birth_date_str:
            try:
                usuario.birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
            except ValueError:
                return jsonify({'error': 'Formato de fecha inválido.'}), 400
        if phone_number:
            usuario.phone_number = phone_number
        if gender:
            usuario.gender = gender
        if email:
            usuario.email = email
        if password:
            usuario.password = generate_password_hash(password, method='sha256')

        db.session.commit()

        return jsonify({'message': 'Usuario actualizado exitosamente!'}), 200  # Código de estado 200 para actualización exitosa

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Ocurrió un error: {str(e)}'}), 500  # Mensaje de error con código de estado 500

def init_routes(app):
    app.register_blueprint(routes)
