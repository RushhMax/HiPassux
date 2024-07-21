from app import create_app
from flask import render_template

app = create_app()

## ESTA ES SOLO UNA RUTA TEST !! NO AGREGAR MAS RUTAS, agregar desde los controladores
@app.route('/')
def test_route():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)