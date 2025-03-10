# app/utils/config.py
import os

# Ejemplo de configuración mínima
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
DEBUG = True
