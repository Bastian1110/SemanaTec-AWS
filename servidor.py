from flask import Flask, request, jsonify, render_template

#Generar el ervidor en flask

servidorWeb = Flask(__name__)

@servidorWeb.route("/test", methods=['GET'])
def formulario():
    return render_template('pagina.html')

if __name__ == "__main__":
    servidorWeb.run(debug=False, host='0.0.0.0', port='8080')
