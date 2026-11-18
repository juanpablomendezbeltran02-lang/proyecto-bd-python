import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="biblioteca")
cursor = conexion.cursor()

# El préstamo 1 todavía no tiene multa (un préstamo tiene como máximo una).
cursor.execute("INSERT INTO multa (prestamo_id, usuario_id, monto, fecha_multa, motivo) VALUES (1, 1, 2000, %s, %s)",
               ("2026-11-01", "Multa de prueba"))
conexion.commit()
nuevo = cursor.lastrowid
print("Agregado, multa_id:", nuevo)

cursor.execute("UPDATE multa SET estado = %s WHERE multa_id = %s", ("Pagada", nuevo))
conexion.commit()
print("Cambiado: la multa quedó Pagada")

cursor.execute("DELETE FROM multa WHERE multa_id = %s", (nuevo,))
conexion.commit()
print("Borrado")

conexion.close()
