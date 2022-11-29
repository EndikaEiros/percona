import mysql.connector as percona
import os


def getDBList():
    _db = percona.connect(host = 'db', user = 'root', password = 'root', port = 3306)
    _c = _db.cursor()

    _c.execute('show databases;')
    result = [x for x in _c.fetchall()]

    result = ["".join([char for char in r if char not in "(,)'"]) for r in result]
    DBList = []
    for r in result:
        tablas = getTableList(r)
        DBList.append((r,tablas))
        os.system(r)
        os.system(tablas)
    _db.close()

    return DBList
    
   
def getTableList(DB):
    _db = percona.connect(host = 'db', user = 'root', password = 'root', port = 3306, database=DB)
    _c = _db.cursor()

    _c.execute('show tables;')

    result = [x for x in _c.fetchall()]

    result = ["".join([char for char in r if char not in "(,)'"]) for r in result]
    #os.system(result)
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
    
    _db.close()

    
    return 0