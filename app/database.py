import mysql.connector as percona

def getDBList():
    _db = percona.connect(host = 'db', user = 'root', password = 'root', port = 3306)
    _c = _db.cursor()

    _c.execute('show databases;')
    result = [x for x in _c.fetchall()]
    
    _db.close()

    
    return result
    
   
def getTableList(DB):
    _db = percona.connect(host = 'db', user = 'root', password = 'root', port = 3306, database=DB)
    _c = _db.cursor()

    _c.execute('show tables;')
    result = [x for x in _c.fetchall()]
    
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

   
    _c.execute("'{}';".format(str(comando)))
    
    _db.close()

    
    return 0