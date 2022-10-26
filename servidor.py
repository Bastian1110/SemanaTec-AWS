
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from fileinput import filename
from joblib import load
import numpy as np
import os

#Cargar el modelo
dt = load('modelo.jotlib')

servidorWeb = Flask(__name__)

@servidorWeb.route("/test", methods=['GET'])
def formulario():
    return render_template('pagina.html')

@servidorWeb.route('/modeloIA', methods=['POST'])
def modeloForm():
    contenido = request.form
    datosEntrada = np.array([
         7.7000,0.5600, 0.0800, 2.5000, 0.1140,14.0000,46.0000, 0.9971,
         contenido['pH'],
         contenido["sulfatos"],
         contenido["alcohol"]
    ])
    resultado = dt.predict(datosEntrada.reshape(1,-1))
    return jsonify({"Resultado" : str(resultado[0])})

@servidorWeb.route('/modeloFile', methods=['POST'])
def modeloFile():
    f = request.files['file']
    filename = secure_filename(f.filename)
    if not os.path.exists('files'):
         os.makedirs('files')
    path = os.path.join(os.getcwd(), 'files', filename)
    f.save(path)
    file = open(path, 'r')
    datosEntrada = []
    for line in file:
        print(line)
        values = line.split(',')
        for i in values:
            if i != "\n":
                datosEntrada.append(int(i))
    datosEntrada = np.array(datosEntrada)
    resultado = dt.predict(datosEntrada.reshape(1,-1))
    return jsonify({"Resultado" : str(resultado[0])})

if __name__ == "__main__":
    servidorWeb.run(debug=False, host='0.0.0.0', port='8080')
