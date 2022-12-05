from flask import Flask, render_template, request, redirect, url_for
import database
import requests
import flask

app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def index():
    lista_db = database.getDBList()

    print(request.method)

    if request.method == 'POST':
        if request.form['submit_button'] == 'Ejecutar Comando':
            comando = request.form['comando']
            print('El comando es: '+ comando)
            db = request.form.get('dataB')
            # db=request.form['dataB']
            print('La base de datos es: ' + str(db))

            database.ejecutarComando(str(db),comando)

            render_template('index.html',perconabd=lista_db)

        elif request.form['submit_button'] == 'Prueba/Test':
            database.flaskTest()

            render_template('index.html',perconabd=lista_db)
        else:
            pass
    elif request.method == 'GET':
        return render_template('index.html',perconabd=lista_db)
    else:
        return render_template('index.html',perconabd=lista_db)
    
    return render_template('index.html',perconabd=lista_db)
    
if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0')
    

