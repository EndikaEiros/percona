from flask import Flask, render_template, request, redirect, url_for
import database
import flask

app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def index():
    lista_db = database.getDBList()

    if request.method == 'POST':
        if request.form['submit_button'] == 'Ejecutar Comando':
            comando = request.form['comando']
            db=request.form['dataB']
            print('DB: {}'.format(str(db)))
            print('Comando: {}'.format(str(comando)))
            database.ejecutarComando(db,comando)

            render_template('index.html',perconabd=lista_db)

        elif request.form['submit_button'] == 'Prueba/Test':
            database.flaskTest()

            render_template('index.html',perconabd=lista_db)
        else:
            pass
    elif request.method == 'GET':
        return render_template('index.html',perconabd=lista_db)

    if len(lista_db)==0:
        lista_db.append('VACIO algo ta mal')
    return render_template('index.html',perconabd=lista_db)
    

    

