from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector
import funciones
from pymysql import Error
import os

app = Flask(__name__)
app.secret_key = 'awagga'
key = "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"
#---------------------------------------INDEX-------------------------------------------
@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')

#----------------------------------------------------UPLOAD----------------------------------------------------

@app.route('/upload', methods=['GET'])
def text():

    return render_template('template1.html')

#------------------------------------------------------Cargar archivo--------------------------------------------
@app.route('/cargar', methods=['POST'])
def procesar():

    if 'file' not in request.files:
        return "No se ha seleccionado ningún archivo."

    archivo = request.files['file']

    if archivo.filename == '':
        return "No se ha seleccionado ningún archivo."

    if archivo and archivo.filename.endswith('.txt'):
        # Leer y decodificar el contenido del archivo
        contenido_archivo = archivo.read().decode('utf-8')
        # Guardar el contenido decodificado en la sesión
        session['file'] = contenido_archivo
        return render_template('template2.html')

    return "El archivo no es de tipo TXT."

#--------------------------------------------------------PREGUNTAR A GPT---------------------------------------------

@app.route('/ask', methods=['POST'])
def comando():

    if 'question' not in request.form:
        return "Debes escribir un prompt"
    
    prompt = request.form['question']

    if prompt == '':
        return "No se ha seleccionado ningún archivo."
    else: 
        session['prompt'] = prompt
        return redirect(url_for('consulta'))


#---------------------------------------------Conexion CHATGPT-------------------------------------------------

@app.route('/consulta', methods=['GET'])
def consulta():

    print(type(session["file"]))
    registro = funciones.chat_gpt(key, session["prompt"], session["file"])
    fecha = funciones.obtener_fecha_hora_actual()
    session["registro"] = registro
    session["fecha"] = fecha
    return redirect(url_for('resumen'))

#------------------------------------------------RESUMEN-------------------------------------------------------
    
@app.route('/resumen', methods=['GET'])
def resumen():

    registro = session["registro"]
    
    return render_template('template3.html',fecha=registro["fecha_hora"], prompt=registro["pregunta"], respuesta=registro["respuesta"])



#----------------------------------------------CONEXION AWS----------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)