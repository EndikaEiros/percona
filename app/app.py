from flask import Flask, render_template
import database

app = Flask(__name__)


@app.route('/')
def index():
    # database.getDBList()
    lista_db = []
    if len(lista_db)==0:
        lista_db.append('VACIO algo ta mal')
    return render_template('index.html',perconabd=lista_db)

@app.route('/buscar')
def buscar():
    return render_template('buscar.html')

@app.route('/agregar')
def agregar():
    return render_template('agregar.html')

@app.route('/borrar')
def borrar():
    return render_template('borrar.html')

@app.route('/comandolibre')
def libre():
    return render_template('libre.html')

