from app import create_app
from app.domain.entities.user import db  # Importa la instancia de SQLAlchemy desde tu modelo

app = create_app()

with app.app_context():
    try:
        db.engine.connect()
        print("Conexión a la base de datos exitosa.")
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")