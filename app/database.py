import mysql.connector

def get_questions():
    _db = mysql.connector.connect(
        host = 'db', user = 'root', password = 'root', port = 3306)
    _c = _db.cursor()

    _c.execute('show databases;')
    result = [x for x in _c.fetchall()]
    
    _db.close()

    
    return result
    
   

