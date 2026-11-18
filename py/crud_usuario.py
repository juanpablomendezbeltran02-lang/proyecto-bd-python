import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="biblioteca")
cursor = conexion.cursor()

cursor.execute("INSERT INTO usuario (nombre, tipo_usuario, direccion, telefono, email) VALUES (%s, %s, %s, %s, %s)",
               ("Pedro Prueba", "Estudiante", "Calle 1 #2-3", "3001234567", "pedro.prueba@example.com"))
conexion.commit()
nuevo = cursor.lastrowid
print("Agregado, usuario_id:", nuevo)

cursor.execute("UPDATE usuario SET nombre = %s WHERE usuario_id = %s", ("Pedro Cambiado", nuevo))
conexion.commit()
print("Cambiado")

cursor.execute("DELETE FROM usuario WHERE usuario_id = %s", (nuevo,))
conexion.commit()
print("Borrado")

conexion.close()
