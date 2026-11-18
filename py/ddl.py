import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="biblioteca")
cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS tabla_prueba (tabla_prueba_id INT PRIMARY KEY AUTO_INCREMENT, descripcion VARCHAR(100) NOT NULL)")
print("Tabla tabla_prueba creada")

cursor.execute("ALTER TABLE libro ADD COLUMN IF NOT EXISTS numero_paginas SMALLINT UNSIGNED NULL")
print("Columna numero_paginas revisada en libro")

cursor.execute("ALTER TABLE prestamo ADD COLUMN IF NOT EXISTS observaciones VARCHAR(200) NULL")
print("Columna observaciones revisada en prestamo")

cursor.execute("ALTER TABLE usuario MODIFY COLUMN telefono VARCHAR(25) NOT NULL")
print("Teléfono ampliado a VARCHAR(25) en usuario")

cursor.execute("CREATE INDEX IF NOT EXISTS idx_libro_titulo ON libro (titulo)")
print("Índice idx_libro_titulo revisado")

cursor.execute("DROP TABLE IF EXISTS tabla_prueba")
print("Tabla tabla_prueba borrada")

conexion.close()
