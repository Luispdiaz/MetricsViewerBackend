# Usamos una imagen base de Python (elige la versión que necesites)
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al contenedor
COPY . .

# Define el comando de entrada. 
# Aquí se asume que tu aplicación se inicia con "python app.py" y escucha en el puerto 5000
CMD ["python", "run.py"]
