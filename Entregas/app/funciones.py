#from dotenv import load_dotenv
import os
from langchain.chains import AnalyzeDocumentChain
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from datetime import datetime

def chat_gpt(api_key,question, file):

    llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key)

    qa_chain = load_qa_chain(llm, chain_type="map_reduce")
    print(qa_chain)
    qa_document_chain = AnalyzeDocumentChain(combine_docs_chain=qa_chain)
    print(qa_document_chain)
    """with open("./pregunta.txt") as f:
        file = f.read()"""


    # Obtener la fecha y hora actuales
    fecha_hora_actual = datetime.now()
    fecha_hora_formateada = fecha_hora_actual.strftime('%Y-%m-%d %H:%M:%S')

    
    response = qa_document_chain.run(
        input_document=file,
        question=question,
    )
    

    print(response)

    # Crear un registro con la pregunta, respuesta y fecha y hora
    registro = {
        "pregunta": question,
        "respuesta": response,
        "fecha_hora": fecha_hora_formateada
    }
    # Imprimir el registro
    return registro



   

"""def leer_archivo(ruta_archivo):
    try:
        with open(ruta_archivo) as f:
            return f.read()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None"""

def obtener_fecha_hora_actual():
    try:
        fecha_hora_actual = datetime.now()
        return fecha_hora_actual.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        print(f"Error al obtener la fecha y hora: {e}")
        return fecha_hora_actual

def procesar_documento(api_key, ruta_archivo, question):
    try:
        llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key)
        qa_chain = load_qa_chain(llm, chain_type="map_reduce")
        qa_document_chain = AnalyzeDocumentChain(combine_docs_chain=qa_chain)

        documento = leer_archivo(ruta_archivo)
        if documento is None:
            return None

        response = qa_document_chain.run(input_document=documento, question=question)
        return response
    except Exception as e:
        print(f"Error al procesar el documento: {e}")
        return None