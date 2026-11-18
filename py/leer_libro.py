import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="biblioteca")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM libro")
for fila in cursor.fetchall():
    print(fila)

conexion.close()
