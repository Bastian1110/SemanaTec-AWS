from flask import Flask, request, jsonify, render_template
from fileinput import filename
from werkzeug.utils import secure_filename
import numpy as np
from joblib import load
import os

servidorWeb = Flask(__name__)

@servidorWeb.route("/test", methods=['GET'])
def formulario():
    return render_template('pagina.html')

@servidorWeb.route('/modeloIA', methods=['POST'])
def modeloForm():
    contenido = request.form
    print(contenido)
    return jsonify({"Resultado" : "Datos recibidos"})

@servidorWeb.route('/modeloFile', methods=['POST'])
def modeloFile():
    f = request.files['file']
    filename = secure_filename(f.filename)
    path = os.path.join(os.getcwd(), 'files', filename)
    f.save(path)
    file = open(path, 'r')
    for line in file:
        print(line)
    return jsonify({"Resultado" : "Datos recibidos"})

if __name__ == "__main__":
    servidorWeb.run(debug=False, host='0.0.0.0', port='8080')
