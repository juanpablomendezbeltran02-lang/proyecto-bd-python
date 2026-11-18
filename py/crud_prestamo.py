import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="biblioteca")
cursor = conexion.cursor()

# Se presta el libro 2 (disponible) al usuario 1 (activo).
# Los triggers cambian el estado del libro: Prestado al prestar y Disponible al devolver.
cursor.execute("INSERT INTO prestamo (libro_id, usuario_id, fecha_prestamo, fecha_devolucion) VALUES (2, 1, %s, %s)",
               ("2026-11-01", "2026-11-15"))
conexion.commit()
nuevo = cursor.lastrowid
print("Agregado, prestamo_id:", nuevo)

cursor.execute("UPDATE prestamo SET estado = %s WHERE prestamo_id = %s", ("Devuelto", nuevo))
conexion.commit()
print("Cambiado: el préstamo quedó Devuelto")

cursor.execute("DELETE FROM prestamo WHERE prestamo_id = %s", (nuevo,))
conexion.commit()
print("Borrado")

conexion.close()
