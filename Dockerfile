# Declaracion de la imagen base
FROM python:3.10

# Directorio dentro del contenedor donde se alamcenara la app
WORKDIR /app

# Copio el contenido de la aplicacion en /app
COPY . /app

# Instalacion de las dependencias
RUN pip install -r requirements.txt


# Expongo el puerto que utilizare
EXPOSE 5000

# Lanzo la app
CMD ["python","main.py"]