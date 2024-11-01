from rest_framework import serializers
from .models import Cliente, Habitacion, Reserva, Servicio, Factura
from datetime import date
from datetime import datetime

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_fecha_nacimiento(self, value):
        if value >= date.today():
            raise serializers.ValidationError("La fecha de nacimiento debe ser anterior a hoy.")
        return value

    def validate_telefono(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("El teléfono solo debe contener números.")
        return value

    def validate_nombre_cliente(self, value):
        if not value.strip():
            raise serializers.ValidationError("El nombre del cliente no puede estar vacío.")
        return value

    def validate_apellido_cliente(self, value):
        if not value.strip():
            raise serializers.ValidationError("El apellido del cliente no puede estar vacío.")
        return value

    def validate(self, data):
        today = date.today()
        age = today.year - data["fecha_nacimiento"].year - (
            (today.month, today.day) < (data['fecha_nacimiento'].month, data['fecha_nacimiento'].day)
        )
        if age < 18:
            raise serializers.ValidationError("El cliente debe tener al menos 18 años.")
        return data


class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__' 

    def validate_precio_por_noche(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio por noche debe ser mayor que cero.")
        return value

    def validate_capacidad(self, value):
        if value <= 0:
            raise serializers.ValidationError("La capacidad debe ser un número positivo.")
        return value

    def validate_numero_habitacion(self, value):
        if not value.strip():
            raise serializers.ValidationError("El número de habitación no puede estar vacío.")
        return value

    def validate_tipo(self, value):
        if not value.strip():
            raise serializers.ValidationError("El tipo de habitación no puede estar vacío.")
        return value


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

    def validate_cliente(self, value):
        if not Cliente.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El cliente especificado no existe.")
        return value

    def validate_habitacion(self, value):
        if not Habitacion.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("La habitación especificada no existe.")
        return value

    def validate(self, attrs):
        if attrs['fecha_salida'] <= attrs['fecha_entrada']:
            raise serializers.ValidationError("La fecha de salida debe ser posterior a la fecha de entrada.")

        reservas_existentes = Reserva.objects.filter(
            habitacion=attrs['habitacion'],
            estado_reserva='confirmada',
            fecha_entrada__lt=attrs['fecha_salida'],
            fecha_salida__gt=attrs['fecha_entrada']
        )
        if reservas_existentes.exists():
            raise serializers.ValidationError("La habitación ya está reservada en estas fechas.")
        
        num_noches = (attrs['fecha_salida'] - attrs['fecha_entrada']).days
        if num_noches <= 0:
            raise serializers.ValidationError("La duración de la reserva debe ser mayor a 0 noches.")

        return attrs

    def validate_fecha_salida(self, value):
        fecha_entrada = self.initial_data.get('fecha_entrada')
        
        if isinstance(fecha_entrada, str):
            fecha_entrada = datetime.strptime(fecha_entrada, "%Y-%m-%d").date()
        
        if value <= fecha_entrada:
            raise serializers.ValidationError("La fecha de salida debe ser posterior a la fecha de entrada.")
        return value

    def validate_numero_personas(self, value):
        if value <= 0:
            raise serializers.ValidationError("El número de personas debe ser mayor que cero.")
        return value

    def validate_estado_reserva(self, value):
        if not value.strip():
            raise serializers.ValidationError("El estado de la reserva no puede estar vacío.")
        return value


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'    

    def validate_precio(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio no puede ser negativo.")
        return value

    def validate_nombre(self, value):
        if not value.strip():
            raise serializers.ValidationError("El nombre del servicio no puede estar vacío.")
        return value

    def validate_descripcion(self, value):
        if not value.strip():
            raise serializers.ValidationError("La descripción no puede estar vacía.")
        return value


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'    
 
    def validate_total(self, value):
        if value < 0:
            raise serializers.ValidationError("El total no puede ser negativo.")
        return value

    def validate_reserva(self, value):
        if not value:
            raise serializers.ValidationError("La reserva asociada no puede estar vacía.")
        return value       
