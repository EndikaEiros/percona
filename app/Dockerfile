FROM python:3.11-alpine
# Construir una imagen de alpine con la imagen de python
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# Declaracion de variables de entorno
RUN python -m pip install --upgrade pip
RUN apk add --no-cache gcc musl-dev linux-headers python3-dev libffi-dev openssl-dev
# Actualizzar el insatlador de componentes de python (pip)
# Intalar unas dependencias necesarias para la aplicación
COPY . /app
WORKDIR /app
# Se copian los archivos de la carpeta actual a la carpeta /app dentro del volumen.
# Se selecciona el directorio /app dentro del volumen como directorio de trabajo
RUN pip install -r requirements.txt
# Se intalan los paquetes necesarios de python para que la aplicacion funcione correctamente.
EXPOSE 5000
# Se abre el purto 5000 en el contenedor (puerto por defecto de flask)
CMD flask run
# se actualiza el comando de arranque del contenedor para que ejecute la pagina web flask