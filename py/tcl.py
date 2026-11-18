import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="biblioteca")
cursor = conexion.cursor()

# Transacción 1: se confirma el teléfono, pero se deshace la dirección (SAVEPOINT)
cursor.execute("SELECT telefono FROM usuario WHERE usuario_id = 4")
telefono_original = cursor.fetchone()[0]
print("Teléfono antes:", telefono_original)

cursor.execute("UPDATE usuario SET telefono = %s WHERE usuario_id = 4", ("3004445500",))
cursor.execute("SAVEPOINT despues_del_telefono")
cursor.execute("UPDATE usuario SET direccion = %s WHERE usuario_id = 4", ("Dirección de prueba",))
cursor.execute("ROLLBACK TO SAVEPOINT despues_del_telefono")
conexion.commit()
cursor.execute("SELECT telefono, direccion FROM usuario WHERE usuario_id = 4")
print("Después de COMMIT (cambió el teléfono, la dirección no):", cursor.fetchone())

# Se deja el teléfono como estaba
cursor.execute("UPDATE usuario SET telefono = %s WHERE usuario_id = 4", (telefono_original,))
conexion.commit()
print("Teléfono devuelto a su valor original")

# Transacción 2: se deshace todo con rollback
cursor.execute("SELECT direccion FROM usuario WHERE usuario_id = 1")
print("Dirección antes:", cursor.fetchone()[0])

cursor.execute("UPDATE usuario SET direccion = %s WHERE usuario_id = 1", ("Otra dirección de prueba",))
cursor.execute("SELECT direccion FROM usuario WHERE usuario_id = 1")
print("Dirección durante la transacción:", cursor.fetchone()[0])

conexion.rollback()
cursor.execute("SELECT direccion FROM usuario WHERE usuario_id = 1")
print("Dirección después de ROLLBACK:", cursor.fetchone()[0])

conexion.close()
