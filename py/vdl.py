import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="biblioteca")
cursor = conexion.cursor()

cursor.execute("CREATE OR REPLACE VIEW v_prestamos_detalle AS SELECT p.prestamo_id, u.nombre AS usuario, l.titulo AS libro, p.fecha_prestamo, p.fecha_devolucion AS fecha_limite, p.estado FROM prestamo p JOIN usuario u ON u.usuario_id = p.usuario_id JOIN libro l ON l.libro_id = p.libro_id")
print("Vista v_prestamos_detalle creada")

print("--- Consulta de la vista ---")
cursor.execute("SELECT * FROM v_prestamos_detalle")
for fila in cursor.fetchall():
    print(fila)

cursor.execute("CREATE OR REPLACE VIEW v_multas_detalle AS SELECT m.multa_id, u.nombre AS usuario, l.titulo AS libro, m.monto, m.fecha_multa, m.estado, m.motivo FROM multa m JOIN usuario u ON u.usuario_id = m.usuario_id JOIN prestamo p ON p.prestamo_id = m.prestamo_id JOIN libro l ON l.libro_id = p.libro_id")
print("Vista v_multas_detalle creada")

print("--- Consulta de la vista ---")
cursor.execute("SELECT * FROM v_multas_detalle")
for fila in cursor.fetchall():
    print(fila)

conexion.close()
