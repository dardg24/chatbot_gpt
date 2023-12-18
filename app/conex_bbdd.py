import pymysql
import os
from dotenv import load_dotenv

load_dotenv(".venv\.env")
os.chdir(os.path.dirname(__file__))

username = "admin"
password = os.environ.get("password")
host = os.environ.get("host")
port = os.environ.get("port")

db = pymysql.connect(host = host,
                     user = username,
                     password = password,
                     cursorclass = pymysql.cursors.DictCursor
)

# Para ejecutar las querys y devuelva los resultados

cursor = db.cursor()
create_db = '''CREATE DATABASE IF NOT EXISTS bbdd_gpt_2'''
cursor.execute(create_db)

cursor.connection.commit()
use_db = ''' USE bbdd_gpt_2'''
cursor.execute(use_db)


create_usuario_table = """
CREATE TABLE IF NOT EXISTS Usuario (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL
);
"""

create_pregunta_table = """
CREATE TABLE IF NOT EXISTS Pregunta (
  id_pregunta INT AUTO_INCREMENT PRIMARY KEY,
  id_usuario INT,
  fecha_pregunta DATE NOT NULL,
  texto_pregunta VARCHAR(255) NOT NULL,
  FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);
"""

create_fecha_table = """
CREATE TABLE IF NOT EXISTS Fecha (
  id_fecha INT AUTO_INCREMENT PRIMARY KEY,
  id_pregunta INT,
  fecha_pregunta DATE NOT NULL,
  fecha_respuesta DATE NOT NULL,
  FOREIGN KEY (id_pregunta) REFERENCES Pregunta(id_pregunta)
);
"""

create_respuesta_table = """
CREATE TABLE IF NOT EXISTS Respuesta (
  id_respuesta INT AUTO_INCREMENT PRIMARY KEY,
  id_pregunta INT,
  texto_respuesta VARCHAR(255) NOT NULL,
  id_fecha INT,
  FOREIGN KEY (id_pregunta) REFERENCES Pregunta(id_pregunta),
  FOREIGN KEY (id_fecha) REFERENCES Fecha(id_fecha)
);
"""

# cursor.execute(create_usuario_table)
# cursor.execute(create_pregunta_table)
# cursor.execute(create_fecha_table)
# cursor.execute(create_respuesta_table)

# cursor.execute("DROP TABLE IF EXISTS Fecha;")
# cursor.connection.commit()
# cursor.execute("DROP TABLE IF EXISTS Respuesta;")
# cursor.connection.commit()
# cursor.execute("DROP TABLE IF EXISTS Pregunta;")
# cursor.connection.commit()
# cursor.execute("DROP TABLE IF EXISTS Usuario;")
# cursor.connection.commit()


# #cursor.connection.commit()
# cursor.close()

# cursor = db.cursor()
# cursor.connection.commit()
# use_db = ''' USE bbdd_gpt'''
# cursor.execute(use_db)
# cursor.execute('''select * from Pregunta''')
# print(cursor.fetchall())

cursor.close()