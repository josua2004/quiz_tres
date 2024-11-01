# API_Reservaciones_Hotel

## Creamos el modelo Cliente:

-Definimos una clase llamada Cliente que hereda de models.Model para representar a un cliente.
-Agregamos campos como nombre_cliente, apellido_cliente, fecha_nacimiento, email, telefono, creado, y actualizado para almacenar la información del cliente.
-Definimos un método __str__ para mostrar una representación legible del cliente.
-Implementamos un método edad para calcular la edad del cliente en función de la fecha de nacimiento.


## Desarrollamos el modelo Habitacion:

-Creamos una clase Habitacion para representar una habitación en el hotel.

-Incluimos campos como numero_habitacion, tipo, capacidad, precio_por_noche, descripcion, y disponible.
-Usamos choices en el campo tipo para especificar opciones como "simple", "doble", "suite" y "deluxe".
-Agregamos métodos reservar y liberar para manejar el estado de disponibilidad de la habitación.
-Definimos el método __str__ para proporcionar una representación de la habitación que incluya el número y tipo.


## Definimos el modelo Reserva:

-Creamos la clase Reserva para representar una reserva en el sistema.
-Incluimos campos como fecha_entrada, fecha_salida, estado_reserva, numero_personas, costo_total, y referencias a los modelos Habitacion y Cliente usando llaves foráneas.
-Definiste el método __str__ para mostrar una representación legible de la reserva.


## Creamos el modelo Servicio:

-Definimos la clase Servicio para representar servicios adicionales que ofrece el hotel.
-Incluiste campos como nombre, descripcion, y precio.
-Agregamos el método __str__ para que se muestre el nombre del servicio en representaciones de cadena.


## Desarrollamos el modelo Factura:

-Creamos la clase Factura para gestionar la facturación de las reservas.
-Agregamos campos como fecha_emision, total, pagado, y una relación con el modelo Reserva.
-Definimos el método __str__ para mostrar una representación legible de la factura.


## Desarrollamos el ClienteSerializer:

-Definimos un serializador para el modelo Cliente heredando de serializers.ModelSerializer.
-Especificamos el modelo y los campos a serializar (fields = '__all__').
-Implementamos varias validaciones:
-validate_fecha_nacimiento: para asegurarnos de que la fecha de nacimiento sea anterior a la fecha actual.
-validate_telefono: para verificar que el número de teléfono solo contenga números.
-validate_nombre_cliente y validate_apellido_cliente: para evitar nombres y apellidos vacíos.
-validate: para validar que el cliente tenga al menos 18 años.


## Creamos el HabitacionSerializer:

.Implementamos un serializador para el modelo Habitacion.

-Añadimos validaciones para los campos:
-validate_precio_por_noche: asegurándonos de que el precio sea mayor que cero.
-validate_capacidad: verificando que la capacidad sea un número positivo.
-validate_numero_habitacion y validate_tipo: para evitar campos vacíos.


## Implementamos el ReservaSerializer:

.Definimos un serializador para el modelo Reserva.

-Incluimos validaciones específicas:
-validate_cliente y validate_habitacion: para comprobar la existencia del cliente y la habitación en la base de datos.
-validate: para verificar que la fecha de salida sea posterior a la de entrada, y que no existan otras -reservas confirmadas para la misma habitación en el rango de fechas seleccionado.
-Validación de la duración de la reserva para asegurarnos de que sea mayor a cero noches.
-validate_fecha_salida: verificando que la fecha de salida sea posterior a la fecha de entrada.
-validate_numero_personas: comprobando que el número de personas sea mayor que cero.
-validate_estado_reserva: para evitar estados vacíos.


## Creamos el ServicioSerializer:

.Implementamos un serializador para el modelo Servicio.

-Incluimos validaciones para:
-validate_precio: asegurándonos de que el precio no sea negativo.
-validate_nombre y validate_descripcion: para evitar valores vacíos en estos campos.


## Desarrollamos el FacturaSerializer:

.Creamos un serializador para el modelo Factura.

-Definimos validaciones específicas:
-validate_total: asegurándonos de que el total no sea negativo.
-validate_reserva: verificando que la reserva asociada no esté vacía.


## Ejecutar el Proyecto

1. Inicia el servidor de desarrollo:

    
    __python manage.py runserver__
    

2. Visita `http://127.0.0.1:8000/api/` para acceder a la API.

## Endpoints de la API

- **Cliente**
    - GET `/api/cliente/` - Lista de todos los clientes.
    - POST `/api/cliente/` - Crear un nuevo cliente.
    - PUT `/api/cliente/<id>/` - Actualizar un cliente existente.
    - DELETE `/api/cliente/<id>/` - Eliminar un cliente.

- **Habitacion**
    - GET `/api/habitacion/` - Lista de todas las habitaciones.
    - POST `/api/habitacion/` - Crear una nueva habitación.
    - PUT `/api/habitacion/<id>/` - Actualizar una habitación existente.
    - DELETE `/api/habitacion/<id>/` - Eliminar una habitación.

- **Reserva**
    - GET `/api/reserva/` - Lista de todas las reservas.
    - POST `/api/reserva/` - Crear una nueva reserva.
    - PUT `/api/reserva/<id>/` - Actualizar una reserva existente.
    - DELETE `/api/reserva/<id>/` - Eliminar una reserva.

- **Servicio**
    - GET `/api/servicio/` - Lista de todos los servicios.
    - POST `/api/servicio/` - Crear un nuevo servicio.
    - PUT `/api/servicio/<id>/` - Actualizar un servicio existente.
    - DELETE `/api/servicio/<id>/` - Eliminar un servicio.

- **Factura**
    - GET `/api/factura/` - Lista de todas las facturas.
    - POST `/api/factura/` - Crear una nueva factura.
    - PUT `/api/factura/<id>/` - Actualizar una factura existente.
    - DELETE `/api/factura/<id>/` - Eliminar una factura.