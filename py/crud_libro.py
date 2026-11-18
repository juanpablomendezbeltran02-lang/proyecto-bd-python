import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="biblioteca")
cursor = conexion.cursor()

cursor.execute("INSERT INTO libro (titulo, autor, isbn, editorial, anio_publicacion, categoria) VALUES (%s, %s, %s, %s, %s, %s)",
               ("Libro de prueba", "Autor de prueba", "978-958-00-0099-9", "Editorial de prueba", 2026, "Prueba"))
conexion.commit()
nuevo = cursor.lastrowid
print("Agregado, libro_id:", nuevo)

cursor.execute("UPDATE libro SET titulo = %s WHERE libro_id = %s", ("Libro de prueba cambiado", nuevo))
conexion.commit()
print("Cambiado")

cursor.execute("DELETE FROM libro WHERE libro_id = %s", (nuevo,))
conexion.commit()
print("Borrado")

conexion.close()
