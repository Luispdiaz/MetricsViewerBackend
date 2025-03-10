# run.py
from flask import Flask
from app.blueprints.main.routes import main_bp

def create_app():
    app = Flask(__name__)

    # (opcional) cargar configuraciones, por ejemplo:
    # app.config.from_object('app.utils.config')

    # Registrar el blueprint principal con un prefijo opcional, por ejemplo "/"
    # Si quieres que el endpoint sea accesible en "/healthcheck", deja el url_prefix vacío.
    app.register_blueprint(main_bp, url_prefix="")

    return app

if __name__ == '__main__':
    my_app = create_app()
    my_app.run(debug=True)
