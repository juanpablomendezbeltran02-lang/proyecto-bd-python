import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="biblioteca")
cursor = conexion.cursor()

# Solo se puede reservar un libro que esté prestado (el libro 4 lo está).
cursor.execute("INSERT INTO reserva (libro_id, usuario_id, fecha_reserva) VALUES (4, 2, %s)", ("2026-11-01",))
conexion.commit()
nuevo = cursor.lastrowid
print("Agregado, reserva_id:", nuevo)

cursor.execute("UPDATE reserva SET estado = %s WHERE reserva_id = %s", ("Cancelada", nuevo))
conexion.commit()
print("Cambiado: la reserva quedó Cancelada")

cursor.execute("DELETE FROM reserva WHERE reserva_id = %s", (nuevo,))
conexion.commit()
print("Borrado")

conexion.close()
