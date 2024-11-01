from django.db import models
from datetime import date

class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=200)
    apellido_cliente = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return f'{self.nombre_cliente} - {self.apellido_cliente}'

    def edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - (
            (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )


class Habitacion(models.Model):
    numero_habitacion = models.CharField(max_length=10, unique=True)
    tipo = models.CharField(max_length=50, choices=[
        ('simple', 'Simple'),
        ('doble', 'Doble'),
        ('suite', 'Suite'),
        ('deluxe', 'Deluxe'),
    ])
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f'Habitación {self.numero_habitacion} - {self.tipo}'

    def reservar(self):
        if not self.disponible:
            raise ValueError("La habitación no está disponible para reservar.")
        self.disponible = False
        self.save()

    def liberar(self):
        self.disponible = True
        self.save()


class Reserva(models.Model):
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    estado_reserva = models.CharField(max_length=20, choices=[
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('pendiente', 'Pendiente')
    ])
    numero_personas = models.IntegerField(default=1)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f'Reserva {self.id} - {self.cliente.nombre_cliente} - {self.cliente.apellido_cliente}'


class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Factura(models.Model):
    fecha_emision = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

    def __str__(self):
        return f'Factura {self.id} - Reserva {self.reserva.id}'