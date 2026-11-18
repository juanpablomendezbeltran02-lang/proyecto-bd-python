import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="")
cursor = conexion.cursor()

cursor.execute("CREATE USER IF NOT EXISTS 'biblioteca_reportes'@'localhost' IDENTIFIED BY 'Reportes#2026'")
print("Usuario biblioteca_reportes listo")

cursor.execute("GRANT SELECT ON biblioteca.* TO 'biblioteca_reportes'@'localhost'")
print("Permiso de leer dado")

cursor.execute("CREATE USER IF NOT EXISTS 'biblioteca_mostrador'@'localhost' IDENTIFIED BY 'Mostrador#2026'")
print("Usuario biblioteca_mostrador listo")

cursor.execute("GRANT SELECT, INSERT, UPDATE, DELETE ON biblioteca.* TO 'biblioteca_mostrador'@'localhost'")
print("Permisos dados")

cursor.execute("REVOKE DELETE ON biblioteca.* FROM 'biblioteca_mostrador'@'localhost'")
print("Permiso de borrar quitado")

print("--- Permisos de biblioteca_reportes ---")
cursor.execute("SHOW GRANTS FOR 'biblioteca_reportes'@'localhost'")
for fila in cursor.fetchall():
    print(fila)

print("--- Permisos de biblioteca_mostrador ---")
cursor.execute("SHOW GRANTS FOR 'biblioteca_mostrador'@'localhost'")
for fila in cursor.fetchall():
    print(fila)

conexion.close()
