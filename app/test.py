# import mysql.connector as percona


# _db = percona.connect(host = 'db', user = 'root', password = 'root', port = 3306)
# _c = _db.cursor()

# _c.execute('show tables;')

# result = [x for x in _c.fetchall()]

# for i in range(len(result)):
#     for char in str(result[i]):
#         if char in "(,)'":
#             result[i]= str(result[i]).replace(char,'')
#             print(result[i])

# _db.close()
import random
import string


def get_random_string(length):
    
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str


for i in range(100):
    nombre = get_random_string(5)
    print("INSERT INTO test_flask (id, nombre) VALUES ('{}', '{}');".format(i, nombre))
