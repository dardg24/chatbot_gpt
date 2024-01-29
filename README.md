# Flask Project with Docker

<img src="app/img/chatbot_gpt.png" width="700">

This project consists of a web application developed using Flask and deployed in a Docker container, with a database hosted on AWS.

## Authors
- Ana Fernandez
- Adrián Nieto
- Daniel Gouveia
- Daniel Manso
- Guillermo Pereda


## Features
- Flask application to answer questions using GPT.
- Use of Docker to containerize and deploy the application.
- Connection to a MySQL database for data storage.
- Database hosting on AWS.

## Usage

To run the application in a Docker container, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/dardg24/chatbot_gpt
   ```
   
2. Download the Docker image:
   ```bash
   docker pull dardg24/mi-app-flask:v2
   ```

3. Ensure the port you want to use is free.
- Use the docker run command with appropriate port mapping. For example:
     ```bash
     docker run -p 5000:3306 dardg24/mi-app-flask:v2

4. Access the application through http://localhost:5000 in your browser.

Deployment in Docker
The Dockerfile included in this repository is used to build the Docker image of the application. The configuration is as follows:

Base image of Python 3.8-slim.
Installation of dependencies from requirements.txt.
Exposure of port 5000.
Use of Gunicorn as a web server.
License
This project is under the MIT License. For more details, see the LICENSE file.


## Spanish

# Proyecto Flask con Docker

<img src="app/img/chatbot_gpt.png" width="700">

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

- Imagen base de Python 3.8-slim.
- Instalación de dependencias desde `requirements.txt`.
- Exposición del puerto 5000.
- Uso de Gunicorn como servidor web.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, ver el archivo `LICENSE`.

---
