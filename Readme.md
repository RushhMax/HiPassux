# PASSUX

## Descripción

Esta es una aplicación web desarrollada con Flask, utilizando un enfoque de **Domain-Driven Design (DDD)** y **Model-View-Controller (MVC)**. La aplicación está configurada para trabajar con una base de datos MySQL utilizando `PyMySQL` y `Flask-Migrate` para manejar las migraciones.

## Estructura del Proyecto
    ```
    my_flask_app/
    │
    ├── app/
    │   ├── __init__.py
    │   ├── controllers/
    │   │   ├── __init__.py
    │   │   ├── user_controller.py  # Controladores para rutas web
    │   │   └── ... (otros controladores)
    │   ├── api/
    │   │   ├── __init__.py
    │   │   ├── user_api.py  # Controladores para rutas API
    │   │   └── ... (otros controladores de API)
    │   ├── domain/
    │   │   ├── __init__.py
    │   │   ├── entities/
    │   │   │   ├── __init__.py
    │   │   │   ├── user.py
    │   │   │   └── ... (otras entidades)
    │   │   ├── repositories/
    │   │   │   ├── __init__.py
    │   │   │   ├── user_repository.py
    │   │   │   └── ... (otros repositorios)
    │   │   ├── services/
    │   │   │   ├── __init__.py
    │   │   │   ├── user_service.py
    │   │   │   └── ... (otros servicios)
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── index.html
    │   │   └── ... (otras plantillas)
    │   ├── static/
    │   │   ├── css/
    │   │   │   └── ... (archivos CSS)
    │   │   ├── js/
    │   │   │   └── ... (archivos JavaScript)
    │   │   └── img/
    │   │       └── ... (imágenes)
    │   ├── viewmodels/
    │   │   ├── __init__.py
    │   │   ├── user_viewmodel.py
    │   │   └── ... (otros viewmodels)
    │   ├── config.py
    │   ├── routes.py
    │   ├── extensions.py
    │   ├── api_routes.py  # Definición de rutas API
    │
    ├── tests/
    │   ├── __init__.py
    │   ├── test_user.py
    │   ├── test_user_api.py  # Pruebas para la API
    │   └── ... (otros tests)
    │
    ├── migrations/
    │   └── ... (archivos de migración)
    │
    ├── venv/
    │   └── ... (entorno virtual)
    │
    ├── .env
    ├── .gitignore
    ├── requirements.txt
    ├── run.py
    └── README.md
    ```


## Instalación

1. **Clona el repositorio**:

    ```bash
    git clone <url-del-repositorio>
    ```

2. **Crea y activa un entorno virtual**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configura las variables de entorno**:

    Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

    ```plaintext
    DATABASE_URL=mysql+pymysql://root:PASSWORD@localhost/DATABASENAME!
    ```

5. **Inicializa la base de datos**:
    Necesario haber creado la DATABASE, las relaciones se crean por medio de estos comandos!

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

## Uso

1. **Ejecuta la aplicación**:

    ```bash
    flask run
    ```

2. **Exporta la aplicación Flask (si es necesario)**:

    ```bash
    export FLASK_APP=run.py
    ```

## Estructura del Código

- **`app/controllers/`**: Controladores que manejan la lógica de las rutas.
- **`app/domain/`**: Dominio de la aplicación, incluyendo entidades, repositorios y servicios.
- **`app/templates/`**: Plantillas HTML para renderizar vistas.
- **`app/static/`**: Archivos estáticos como CSS, JavaScript e imágenes.
- **`app/viewmodels/`**: ViewModels para la lógica de presentación.
- **`tests/`**: Pruebas unitarias y de integración.
- **`migrations/`**: Archivos de migración de la base de datos.


## Reporte SonarLint
- Define a constant instead of duplicating this literal 'User not found' 3 times. [+2 locations]

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue los siguientes pasos para contribuir:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadida nueva característica'`).
4. Empuja tus cambios (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Buenas Practicas 
- Es importante utilizar nombres descriptivos para las variables y parámetros. Esto facilita la comprensión del código y su mantenimiento. Por ejemplo, en la  función update_user, las variables username, first_name, last_name, birth_date, etc., son nombres claros que indican qué datos están siendo manipulados.
- La correcta indentación y la separación de las funciones con líneas en blanco ayudan a mejorar la legibilidad del código. Cada función debe ser        independiente y fácil de identificar, lo cual es vital para el mantenimiento y la colaboración en equipo.
- Los mensajes de error deben ser claros y específicos para facilitar la depuración y resolución de problemas. En el ejemplo proporcionado, 
  los mensajes como  'Usuario no encontrado' y 'Formato de fecha inválido.' ayudan a identificar rápidamente la causa del error.
  ### Ejemplo Funciones implementadas 
    ```python
        @staticmethod
    def update_user(user_id, username, first_name, last_name, birth_date, phone_number, gender, email, password=None):
        try:
            usuario = UserRepository.get_user_by_id(user_id)  # Usar el repositorio para obtener el usuario
            if not usuario:
                return {'error': 'Usuario no encontrado'}

            # Actualizar los campos del usuario
            usuario.username = username
            usuario.first_name = first_name
            usuario.last_name = last_name

            if isinstance(birth_date, str):  # Convertir si es una cadena
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

            UserRepository.update_user(usuario)  # Usar el repositorio para actualizar el usuario
            return usuario
        except Exception as e:
            return {'error': f'Ocurrió un error al actualizar el usuario: {str(e)}'}

    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_user_by_id(user_id)
    ```
    ```python
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
    ```
## Principios solid aplicados 
 ### Single Responsibility Principle (SRP):
 - Cada clase tiene una unica responsabilidad en el codigo los controlladores servicios y operaciones tienen una responsabilidad
    
    ```python
        class UserRepository:
            #Se encarga de las operaciones 
            @staticmethod
                def get_all_users():
                return User.query.all()
        @bp.route('/users', methods=['GET'])
        #Services se encarga de llamar a el servicio UserService maneja las solicitudes HTTP 
        def get_users():
            users = UserService.get_all_users()
            return render_template('users.html', users=users)
            
        # Se encarga de la logica de los usuarios creacion actualizacion 
        class UserService:

            @staticmethod
            def get_all_users():
                return UserRepository.get_all_users()

            @bp.route('/register', methods=['GET', 'POST'])
            @staticmethod
            def update_user(user_id, username, first_name, last_name, birth_date, phone_number, gender, email, password=None):
    
    ```
    
 ### Open/Closed Principle (OCP):
 - Podemos agregar y extender nuestro codigo sin necesidad de cambiar nuestro codigo original 
 ### Ejemplos
 - UserRepository: Podemos agregar nuevos métodos de consulta sin modificar el código existente, simplemente extendiendo la clase.
UserService: Podemos añadir nuevas funcionalidades o servicios relacionados con usuarios sin cambiar los métodos existentes. Si necesitas algo nuevo
solo extendemos la clase con otras funciones.
 ### Laboratorio 11: Estilos de Programación:
 ### Restful:
 - Este estilo se basa en la arquitectura REST , que utiliza métodos HTTP para manipular recursos en la web. En el codigo, los endpoints RESTful permiten realizar operaciones CRUD sobre las solicitudes de amistad.
    ```python
        @bp.route('/friend_requests', methods=['GET'])
        def get_friend_requests():
            friend_requests = FriendRequestService.get_all_friend_requests()
            return render_template('friend_requests.html', friend_requests=friend_requests)

        @bp.route('/friend_requests/send', methods=['POST'])
        def send_friend_request():
            sender_id = request.form.get('sender_id')
            receiver_id = request.form.get('receiver_id')
            result = FriendRequestService.send_friend_request(sender_id, receiver_id)
            return redirect(url_for('friend_request.get_friend_requests', message=result))

        @bp.route('/friend_requests/respond/<int:request_id>', methods=['POST'])
        def respond_to_friend_request(request_id):
            action = request.form.get('action')
            result = FriendRequestService.respond_to_friend_request(request_id, action)
            return redirect(url_for('friend_request.get_friend_requests', message=result)) 
    ```
  ### Error/Exception Handling:
  - Maneja los errores y excepciones para asegurar que el sistema sea robusto y pueda recuperarse de fallos. Esto incluye manejar errores en la lógica de negocio y en las interacciones con la base de datos.
    ```python
    @bp.route('/friend_requests/send', methods=['POST'])
    def send_friend_request():
        try:
            sender_id = request.form.get('sender_id')
            receiver_id = request.form.get('receiver_id')
            result = FriendRequestService.send_friend_request(sender_id, receiver_id)
        except SQLAlchemyError as e:
            return jsonify({'error': str(e)}), 500
        return redirect(url_for('friend_request.get_friend_requests', message=result))    
    
    ```


  ### Pipeline:
  - En este estilo, los datos se procesan a través de una serie de transformaciones o pasos secuenciales. Se aplica en el procesamiento de solicitudes de amistad, donde los datos se pasan a través de varias etapas antes de ser almacenados o utilizados.
    ```python
        class FriendRequestService:

    @staticmethod
    def send_friend_request(sender_id, receiver_id):
        if sender_id == receiver_id:
            return "No puedes enviarte una solicitud a ti mismo."
        
        existing_request = FriendRequestRepository.get_by_sender_and_receiver(sender_id, receiver_id)
        if existing_request:
            return "Ya has enviado una solicitud a este usuario."

        new_request = FriendRequest(sender_id=sender_id, receiver_id=receiver_id)
        FriendRequestRepository.add(new_request)
        return "Solicitud enviada con éxito."

    @staticmethod
    def respond_to_friend_request(request_id, action):
        request = FriendRequestRepository.get_by_id(request_id)
        if not request:
            return "Solicitud no encontrada."
        
        if action == 'accept':
            request.status = RequestStatus.ACCEPTED
        elif action == 'reject':
            request.status = RequestStatus.REJECTED
        else:
            return "Acción inválida."

        FriendRequestRepository.update(request)
        return "Solicitud actualizada con éxito."
    
    ```

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).