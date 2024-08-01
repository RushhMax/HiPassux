# PASSUX

## Índice

1. [Descripción](#descripción)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Instalación](#instalación)
4. [Uso](#uso)
5. [Estructura del Código](#estructura-del-código)
6. [Contribuciones](#contribuciones)
7. [Licencia](#licencia)
8. [Buenas Prácticas LAB 09](#buenas-prácticas-lab-09)
   - [Nombres de Variables y Funciones](#nombres-de-variables-y-funciones)
   - [Nombres de Clases](#nombres-de-clases)
   - [Nombres de Constantes](#nombres-de-constantes)
   - [Indentación](#indentación)
   - [Líneas en Blanco](#líneas-en-blanco)
   - [Manejo de Errores](#manejo-de-errores)
   - [Uso de F-Strings](#uso-de-f-strings)
9. [Code Smells](#code-smells)
   - [Código Repetido](#código-repetido)
   - [Funciones Grandes](#funciones-grandes)
10. [Bugs](#bugs)
   - [Errores de Referencia](#errores-de-referencia)
11. [Vulnerabilidades](#vulnerabilidades)
12. [Buenas Prácticas LAB 010 SOLID](#buenas-prácticas-lab-010-solid)
    - [Single Responsibility Principle (SRP)](#single-responsibility-principle-srp)
    - [Open/Closed Principle (OCP)](#openclosed-principle-ocp)
    - [Liskov Substitution Principle (LSP)](#liskov-substitution-principle-lsp)
    - [Dependency Inversion Principle (DIP)](#dependency-inversion-principle-dip)


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

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue los siguientes pasos para contribuir:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadida nueva característica'`).
4. Empuja tus cambios (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).

## Buenas Prácticas LAB 09

### Nombres de Variables y Funciones:

Utiliza snake_case para variables y nombres de funciones:

```python
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
```
### Nombres de Clases:

Utiliza CamelCase para nombres de clases.

```python
from app.extensions import db

class User(db.Model):
    __tablename__ = 'USERS'  # Ensure this matches your table name
```

### Nombres de Constantes:

Utiliza MAYÚSCULAS_CON_GUIONES_BAJOS para constantes

```python
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:PASSWORD@localhost/Passux') #mysql://username:password@host:port/database_name
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True
```

### Indentación

Usa 4 espacios por nivel de indentación (no uses tabuladores).

```python
def to_dict(self):
    return {
        'id': self.user_id,
        'username': self.username,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'birth_date': self.birth_date.isoformat() if self.birth_date else None,
        'phone_number': self.phone_number,
        'gender': self.gender,
        'email': self.email
    }    
```

###  Líneas en Blanco

Utiliza líneas en blanco para separar funciones y clases, así como bloques de código dentro de funciones.

```python
def __repr__(self):
    return f'<User {self.username}>'
    
def to_dict(self):
    return {
        'id': self.user_id,
        'username': self.username,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'birth_date': self.birth_date.isoformat() if self.birth_date else None,
        'phone_number': self.phone_number,
        'gender': self.gender,
        'email': self.email
    }    
```

### Manejo de Errores

Usa bloques try-except para manejar excepciones y proporciona mensajes de error útiles.

```python
if __name__ == '__main__':
    app = create_app()
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error: {e}")
```

### Uso de F-Strings

Utiliza f-strings (en Python 3.6 y posteriores) para la interpolación de cadenas.

```python
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error: {e}")
```

## Code Smells

### Código repetido

Extraer el código repetido en una función separada.

```python
    @user_api.route('/', methods=['GET'])
    def get_users():
        users = UserService.get_all_users()
        return jsonify([user.to_dict() for user in users])

    @user_api.route('/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        user = UserService.get_user_by_id(user_id)
        if user:
            return jsonify(user.to_dict())
        return jsonify({'error': 'User not found'}), 404

    @user_api.route('/', methods=['POST'])
    def create_user():
        data = request.json
        new_user = UserService.create_user(data)
        return jsonify(new_user.to_dict()), 201
```

### Funciones Grandes

Funciones que hacen demasiado y tienen muchas responsabilidades.

```python
    def create_app(config_class=Config):
        app = Flask(__name__)
        app.config.from_object(config_class)

        db.init_app(app)
        migrate.init_app(app, db)
        
        init_routes(app)
        init_api_routes(app)

        return app
```

## Bugs
### Errores de Referencia

Bug: Intentar acceder a una variable que no existe.


```python
from flask import Flask, jsonify
from app.extensions import db, migrate
from app.routes import init_routes
from app.config import Config
from app.api_routes import init_api_routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
        
    init_routes(app)
    init_api_routes(app)

    return app
```

## Vulnerabilities

Ejecutar consultas SQL con entrada no sanitizada.

```python
class UserRepository:

    @staticmethod
    def get_all_users():
        return User.query.all()
    
    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()
```

# Buenas Prácticas LAB 010 SOLID

## Single Responsibility Principle (SRP)

Principio: Una clase o módulo debe tener una sola responsabilidad o motivo para cambiar.
Por ejemplo en nuestro proyecto estamos diviendo a User en:

```python
# models.py
class User(db.Model):
    # Definición de la entidad usuario

# services/user_service.py
class UserService:

    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()

# controllers/user_controller.py
@bp.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    return render_template('users.html', users=users)
```
## Open/Closed Principle (OCP)

Principio: El código debe estar abierto para extensión, pero cerrado para modificación.

```python
# controllers/user_controller.py
from flask import Blueprint, render_template, request , redirect, url_for
from app.domain.services.user_service import UserService
from datetime import datetime

bp = Blueprint('user', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    # Lógica para obtener usuarios

@bp.route('/register', methods=['GET', 'POST'])
def register():
    # Lógica para crear usuario
```

## Liskov Substitution Principle (LSP)

Principio: Los objetos de una clase derivada deben poder reemplazar objetos de la clase base sin alterar el comportamiento esperado del programa.

```python
# domain/repositories/base_repository.py
class BaseRepository:
    def add(self, entity):
        pass

    def remove(self, entity):
        pass

# domain/repositories/user_repository.py
from app.domain.entities.user import db, User
from app.domain.repositories.base_repository import BaseRepository

class UserRepository(BaseRepository):

    @staticmethod
    def get_all_users():
        return User.query.all()
        # Obtiene todos los usuarios de la base de datos.

    def add(self, user):
        db.session.add(user)
        db.session.commit()
        # Añade un usuario a la base de datos y confirma la transacción.

    def remove(self, user):
        db.session.delete(user)
        db.session.commit()
        # Elimina un usuario de la base de datos y confirma la transacción.
```

## Dependency Inversion Principle (DIP)

Principio: Los módulos de alto nivel no deben depender de módulos de bajo nivel, sino de abstracciones.

```python
from app.domain.repositories.user_repository import User,UserRepository

class UserService:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    @staticmethod
    def get_all_users(self):
        return self.UserRepository.get_all_users()

    @staticmethod
    def create_user(self ,username, first_name, last_name, birth_date, phone_number, gender, email, password):
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
        self.UserRepository.add_user(new_user)
```