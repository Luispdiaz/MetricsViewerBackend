from flask import Flask
from app.blueprints.main.routes import main_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp, url_prefix="")

    return app

if __name__ == '__main__':
    my_app = create_app()
    my_app.run(host="0.0.0.0", port=5000, debug=True)
