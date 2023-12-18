
# Proyecto Flask con Docker

Este proyecto consiste en una aplicación web desarrollada con Flask y desplegada en un contenedor Docker, con una base de datos alojada en AWS.

## Autores

- Ana Fernandez
- Adrián Nieto
- Daniel Gouveia
- Daniel Manso
- Guillermo Pereda

## Características

- Aplicación Flask para responder preguntas utilizando GPT.
- Uso de Docker para contenerizar y desplegar la aplicación.
- Conexión a base de datos MySQL para almacenamiento de datos.
- Alojamiento de la base de datos en AWS.

## Uso

Para ejecutar la aplicación en un contenedor Docker, sigue estos pasos:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/dardg24/chatbot_gpt
   ```

2. Descarga la imagen Docker:
   ```bash
   docker pull dardg24/mi-app-flask:v2
   ```

3. Ejecuta la imagen en un contenedor:
   - Asegúrate de que el puerto que deseas usar esté libre.
   - Utiliza el comando `docker run` con el mapeo de puertos apropiado. Por ejemplo:
     ```bash
     docker run -p 5000:3306 dardg24/mi-app-flask:v2
     ```

4. Accede a la aplicación a través de `http://localhost:5000` en tu navegador.

## Despliegue en Docker

El `Dockerfile` incluido en este repositorio se utiliza para construir la imagen de Docker de la aplicación. La configuración es la siguiente:

- Imagen base de Python 3.9-slim.
- Instalación de dependencias desde `requirements.txt`.
- Exposición del puerto 5000.
- Uso de Gunicorn como servidor web.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, ver el archivo `LICENSE`.

---
