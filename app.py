from flask import Flask, render_template, request, session, redirect, url_for
from openai import OpenAI
import mysql.connector
import langchain

app = Flask(__name__)
app.secret_key = 'awagga'
#---------------------------------------INDEX-------------------------------------------
@app.route('/', methods=['GET'])
def index():

    return 'Bienvenidos a la pagina principal de la GPTAPP'

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
        # Guarda el archivo en la sesión (temporalmente)
        session['file'] = archivo.read()

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
        return redirect(url_for('resumen'))

#------------------------------------------------RESUMEN-------------------------------------------------------
    
@app.route('/resumen', methods=['GET'])
def resumen():

    prompt = session['prompt']
    txt = session['file']

    return render_template('template3.html', prompt=prompt, txt=txt)


#----------------------------------------------CONEXION AWS----------------------------------------------------

@app.route('/consulta', methods=['GET'])
def consulta():
    

    config = {
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'host': 'endpoint_de_tu_base_de_datos_en_aws',
    'database': 'tu_base_de_datos',
    'port': '3306',  # Puerto por defecto para MySQL
    }

    try:
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM tu_tabla")
        resultados = cursor.fetchall()

        """for resultado in resultados:
            print(resultado)"""
        
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")

    finally:
        # Asegurarse de cerrar la conexión, independientemente de si fue exitosa o no
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")  

    #------------------------------------------- CONSULTA CHATGPT----------------------------------
    try:
        client = OpenAI(api_key="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")
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "For the moment this is a test."},
            {"role": "user", "content": "Please, confirm me by saying anything."}
        ]
        )

        return completion.choices[0].message.content
    except:
        return "ha ocurrido un error con chatgpt"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)