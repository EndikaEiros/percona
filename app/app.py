from flask import Flask, render_template
import database

app = Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    lista_db = database.getDBList()
    if len(lista_db)==0:
        lista_db.append('VACIO algo ta mal')
    return render_template('index.html',perconabd=lista_db)

# @app.route('/buscar',methods=['GET'])
# def buscar():
#     return render_template('buscar.html')

# @app.route('/agregar',methods=['GET'])
# def agregar():
#     return render_template('agregar.html')

# @app.route('/borrar',methods=['GET'])
# def borrar():
#     return render_template('borrar.html')

# @app.route('/comandolibre',methods=['GET'])
# def libre():
#     return render_template('libre.html')

