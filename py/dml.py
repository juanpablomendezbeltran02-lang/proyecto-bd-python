import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="biblioteca")
cursor = conexion.cursor()

cursor.execute("INSERT INTO usuario (nombre, tipo_usuario, direccion, telefono, email) VALUES (%s, %s, %s, %s, %s)",
               ("Laura Gómez", "Profesor", "Calle 50 # 20-30", "3011122334", "laura.gomez@example.com"))
conexion.commit()
laura = cursor.lastrowid
print("Usuario agregado")

# Laura reserva "Pedro Páramo" (libro 4, que está prestado)
cursor.execute("INSERT INTO reserva (libro_id, usuario_id, fecha_reserva) VALUES (4, %s, %s)", (laura, "2026-11-02"))
conexion.commit()
print("Reserva agregada")

cursor.execute("UPDATE usuario SET telefono = %s WHERE usuario_id = %s", ("3109998877", laura))
conexion.commit()
print("Teléfono cambiado")

cursor.execute("DELETE FROM reserva WHERE usuario_id = %s", (laura,))
conexion.commit()
print("Reserva borrada")

cursor.execute("DELETE FROM usuario WHERE usuario_id = %s", (laura,))
conexion.commit()
print("Usuario borrado")

conexion.close()
