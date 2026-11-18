import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="biblioteca")
cursor = conexion.cursor()

print("--- Libros disponibles ---")
cursor.execute("SELECT libro_id, titulo, autor FROM libro WHERE estado = 'Disponible' ORDER BY titulo")
for fila in cursor.fetchall():
    print(fila)

print("--- Préstamos pendientes (usuario y libro) ---")
cursor.execute("SELECT p.prestamo_id, u.nombre, l.titulo, p.fecha_devolucion FROM prestamo p JOIN usuario u ON u.usuario_id = p.usuario_id JOIN libro l ON l.libro_id = p.libro_id WHERE p.estado = 'Pendiente'")
for fila in cursor.fetchall():
    print(fila)

print("--- Libros por categoría ---")
cursor.execute("SELECT categoria, COUNT(*) AS total_libros FROM libro GROUP BY categoria")
for fila in cursor.fetchall():
    print(fila)

print("--- Multas pendientes por usuario ---")
cursor.execute("SELECT u.nombre, SUM(m.monto) AS total_pendiente FROM multa m JOIN usuario u ON u.usuario_id = m.usuario_id WHERE m.estado = 'Pendiente' GROUP BY u.nombre")
for fila in cursor.fetchall():
    print(fila)

conexion.close()
