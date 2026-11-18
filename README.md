# Proyecto Bases de Datos - Tercer corte (Python)

Base de datos del Sistema de Gestión de Biblioteca, manejada desde Python con PyMySQL.

## Requisitos
- XAMPP con MySQL encendido
- Python 3.13
- Librería PyMySQL

## Instalación
    python -m pip install -r requirements.txt

## Contenido
- sql/biblioteca.sql : la base de datos completa (tablas y triggers)
- sql/biblioteca_insert.sql : datos de prueba
- sql/commands/ : comandos SQL por tipo (01_DDL a 06_TCL)
- tests/biblioteca_pruebas.sql : pruebas básicas
- docs/ : artículo del diseño, diagramas entidad-relación y diccionario de datos
- py/conexion.py : prueba la conexión
- py/tablas.py : muestra las tablas
- py/ddl.py, dml.py, dql.py, vdl.py, dcl.py, tcl.py : un script por cada archivo de sql/commands
- `py/leer_<tabla>.py` : lee todos los datos de una tabla
- `py/crud_<tabla>.py` : agrega, cambia y borra una fila de prueba en una tabla

Tablas: usuario, libro, prestamo, reserva, multa.

## Cómo ejecutar
1. Encender MySQL en XAMPP.
2. Importar sql/biblioteca.sql y luego sql/biblioteca_insert.sql en phpMyAdmin.
3. Ejecutar los scripts desde la carpeta del proyecto, en este orden:

    python py\conexion.py
    python py\ddl.py
    python py\dml.py
    python py\dql.py
    python py\vdl.py
    python py\dcl.py
    python py\tcl.py

Notas:
- dcl.py se conecta como root, porque crear usuarios y dar permisos requiere una cuenta administradora.
- Los scripts dejan los datos igual que antes de correrlos: lo que agregan, lo borran al final.
- vdl.py deja creadas las vistas v_prestamos_detalle y v_multas_detalle.
- Los triggers revisan las reglas: solo se presta a un usuario activo y un libro disponible, y solo se reservan libros prestados.

## Integrantes
- Yheriam Noelber Diaz Obando
- Johan Stiverson Mendoza Durte
- Juan Pablo Mendez Beltran
- Juan Camilo Romero
