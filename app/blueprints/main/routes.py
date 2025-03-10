# app/blueprints/main/routes.py

from flask import Blueprint, jsonify

# 1. Crear el Blueprint
main_bp = Blueprint('main', __name__)

# 2. Definir una ruta sencilla para verificar que el servidor está activo
@main_bp.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({
        "status": "OK",
        "message": "Server is up and running!"
    }), 200
