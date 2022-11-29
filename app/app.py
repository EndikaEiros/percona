from flask import Flask, render_template, request, redirect, url_for
import database
import flask

app = Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    lista_db = database.getDBList()
    if len(lista_db)==0:
        lista_db.append('VACIO algo ta mal')
    return render_template('index.html',perconabd=lista_db)

@app.route('/ejecutarcomando/', methods=['GET','POST'])
def ejecutarcomando():
    if flask.request.method == 'POST':
        comando = request.form['comando']
        db=request.form['dataB']
        print('DB: {}'.format(str(db)))
        print('Comando: {}'.format(str(comando)))
    else:
        if database.ejecutarComando(db,comando) == 0:
            lista_db = database.getDBList()
            if len(lista_db)==0:
                lista_db.append('No hay ninguna base de datos cargada')
        else:
            lista_db=['Ha ocurrido un error']
        
    return redirect(url_for('index'), code=302)
    

    

