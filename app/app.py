from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector
import chatbot_gpt.app.src.funciones as funciones
import pymysql
import json
from pymysql import Error
import os


credenciales = {
    "username": "yourusername",
    "password": "youpassword",
    "host": "exampleofhostpage",
    "port": 3306
}


app = Flask(__name__)
app.secret_key = 'youruser'
key = "your_secret_key"
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
    
    #----------------------------------------------CONEXION AWS----------------------------------------------------
    #cargamos credenciales
    registro = session["registro"]
    db = pymysql.connect(host=credenciales["host"],
                     user=credenciales["username"],
                     password=credenciales["password"],
                     port=credenciales["port"],
                     cursorclass=pymysql.cursors.DictCursor)

    cursor = db.cursor()
    use_db = ''' USE bbdd_gpt_2'''
    cursor.execute(use_db)



    create_pregunta_table = """
    CREATE TABLE IF NOT EXISTS Pregunta (
    id_pregunta INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    fecha_pregunta DATE NOT NULL,
    texto_pregunta VARCHAR(255) NOT NULL,
    texto_respuesta VARCHAR(255) NOT NULL);
    """

    cursor.execute(create_pregunta_table)

    """sql_query = "SELECT MAX(id_usuario) FROM Pregunta"

    # Ejecutar la consulta
    cursor.execute(sql_query)

    # Obtener el resultado
    ID = cursor.fetchone()

    if ID == "NULL":
        ID = 0
    """


    sql_insert1 = "INSERT INTO Pregunta (fecha_pregunta, texto_pregunta, texto_respuesta) VALUES (%s, %s, %s)"
    #sql_insert2 = "INSERT INTO Fecha (id_pregunta, fecha_pregunta, fecha_respuesta, id_pregunta) VALUES (%s, %s, %s, %s)"
    #sql_insert3 = "INSERT INTO ******** (id_pregunta, texto_respuesta, id_fecha, id_pregunta, id_fecha) VALUES (%s, %s)"

    cursor.execute(sql_insert1, (registro["fecha_hora"], registro["pregunta"], registro["respuesta"]))
    cursor.connection.commit()

    # Ejecutar la consulta SQL
    query = "SELECT * FROM Pregunta;"
    #df = pd.read_sql_query(query, db)
    cursor.execute(query)
    resultado = cursor.fetchall()
    #retornamos para abrir el HTML
    
    return render_template('template3.html',fecha=registro["fecha_hora"], prompt=registro["pregunta"], respuesta=registro["respuesta"], dataframe=resultado)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3306)
