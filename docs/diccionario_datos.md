# Diccionario de datos

| Tabla | Columna | Tipo | Llave | Descripción |
|---|---|---|---|---|
| usuario | usuario_id | INT | PK | Identificador del usuario |
| usuario | nombre | VARCHAR(100) | | Nombre completo |
| usuario | tipo_usuario | ENUM | | Estudiante, Profesor o Externo |
| usuario | direccion | VARCHAR(150) | | Dirección de residencia |
| usuario | telefono | VARCHAR(25) | | Teléfono de contacto (ampliado con ALTER en 01_DDL) |
| usuario | email | VARCHAR(120) | UNIQUE | Correo electrónico |
| usuario | fecha_registro | DATE | | Fecha de inscripción |
| usuario | estado | ENUM | | Activo, Suspendido o Inactivo |
| libro | libro_id | INT | PK | Identificador del libro |
| libro | titulo | VARCHAR(200) | | Título del libro |
| libro | autor | VARCHAR(150) | | Autor o autores |
| libro | isbn | VARCHAR(20) | UNIQUE | Código ISBN |
| libro | editorial | VARCHAR(100) | | Editorial |
| libro | anio_publicacion | SMALLINT | | Año de publicación |
| libro | categoria | VARCHAR(60) | | Categoría o género |
| libro | estado | ENUM | | Disponible, Prestado, Mantenimiento o Perdido |
| libro | numero_paginas | SMALLINT | | Número de páginas (agregada con ALTER en 01_DDL) |
| prestamo | prestamo_id | INT | PK | Identificador del préstamo |
| prestamo | libro_id | INT | FK | Libro prestado (libro.libro_id) |
| prestamo | usuario_id | INT | FK | Usuario que lo recibe (usuario.usuario_id) |
| prestamo | fecha_prestamo | DATE | | Fecha de salida del libro |
| prestamo | fecha_devolucion | DATE | | Fecha límite de devolución |
| prestamo | estado | ENUM | | Pendiente o Devuelto |
| prestamo | observaciones | VARCHAR(200) | | Notas (agregada con ALTER en 01_DDL) |
| reserva | reserva_id | INT | PK | Identificador de la reserva |
| reserva | libro_id | INT | FK | Libro reservado (libro.libro_id) |
| reserva | usuario_id | INT | FK | Usuario que reserva (usuario.usuario_id) |
| reserva | fecha_reserva | DATE | | Fecha de solicitud |
| reserva | estado | ENUM | | Activa, Atendida o Cancelada |
| multa | multa_id | INT | PK | Identificador de la multa |
| multa | prestamo_id | INT | FK, UNIQUE | Préstamo que la originó (prestamo.prestamo_id) |
| multa | usuario_id | INT | FK | Usuario que debe la multa (usuario.usuario_id) |
| multa | monto | DECIMAL(10,2) | | Valor de la multa |
| multa | fecha_multa | DATE | | Fecha en que se genera |
| multa | estado | ENUM | | Pendiente o Pagada |
| multa | motivo | VARCHAR(150) | | Motivo de la multa |

## Triggers

| Trigger | Tabla | Regla |
|---|---|---|
| trg_prestamo_validar | prestamo | Solo se presta a un usuario activo y un libro disponible |
| trg_prestamo_libro_prestado | prestamo | Al prestar, el libro pasa a Prestado |
| trg_prestamo_libro_devuelto | prestamo | Al devolver, el libro vuelve a Disponible |
| trg_reserva_validar | reserva | Solo se reservan libros prestados |
