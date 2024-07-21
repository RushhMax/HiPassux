from app import create_app
from flask import Blueprint, render_template

app = create_app()

## ESTA ES SOLO UNA RUTA TEST !! NO AGREGAR MAS RUTAS, agregar desde los controladores
@app.route('/')
def test_route():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    