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

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue los siguientes pasos para contribuir:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadida nueva característica'`).
4. Empuja tus cambios (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).