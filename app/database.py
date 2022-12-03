import mysql.connector as percona

import random
import string


def getDBList():
    _db = percona.connect(host = 'db', user = 'root', password = 'root', port = 3306)
    _c = _db.cursor()

    _c.execute('show databases;')
    result = [x for x in _c.fetchall()]

    result = ["".join([char for char in r if char not in "(,)'"]) for r in result]
    DBList = []
    for r in result:
        tablas=[]
        if r not in ['information_schema','mysql','performance_schema','sys']:
            tablas = getTableList(r)
        DBList.append((r,tablas))
        print(r)
        print(tablas)
    _db.close()

    return DBList
    
   
def getTableList(DB):
    _db = percona.connect(host = 'db', user = 'root', password = 'root', port = 3306, database=DB)
    _c = _db.cursor()

    _c.execute('show tables;')

    result = [x for x in _c.fetchall()]

    result = ["".join([char for char in r if char not in "(,)'"]) for r in result]
    _db.close()

    return result


def selectAllTable(DB,table):
    _db = percona.connect(host = 'db', user = 'root', password = 'root', port = 3306, database=DB)
    _c = _db.cursor()

   
    _c.execute("Select * from '{}';".format(str(table)))
    result = [x for x in _c.fetchall()]
    
    _db.close()

    
    return result

def ejecutarComando(DB,comando):
    _db = percona.connect(host = 'db', user = 'root', password = 'root', port = 3306, database=DB)
    _c = _db.cursor()
    
    print(DB)
    print(comando)
    _c.execute("'{}';".format(str(comando)))
    _db.commit()
    _db.close()
    return 0

def get_random_string(length):
    
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str

def flaskTest():
    _db = percona.connect(host = 'db', user = 'root', password = 'root', port = 3306)
    _c = _db.cursor()

    _c.execute("DROP DATABASE IF EXISTS flask_db;")
    _c.execute("CREATE DATABASE IF NOT EXISTS flask_db;")
    _db.close()

    _db = percona.connect(host = 'db', user = 'root', password = 'root', port = 3306, database='flask_db')
    _c = _db.cursor()
    _c.execute("CREATE TABLE test_flask (id INT, nombre VARCHAR(20));")
    
    for i in range(100):
        nombre = get_random_string(5)
        _c.execute("INSERT INTO test_flask (id, nombre) VALUES ({},'{}');".format(i, nombre))
    
    _db.commit()
    _db.close()
    return 0