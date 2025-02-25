# Generated by Django 5.1.2 on 2024-10-24 20:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=200)),
                ('apellido_cliente', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_habitacion', models.CharField(max_length=10, unique=True)),
                ('tipo', models.CharField(choices=[('simple', 'Simple'), ('doble', 'Doble'), ('suite', 'Suite'), ('deluxe', 'Deluxe')], max_length=50)),
                ('capacidad', models.IntegerField()),
                ('precio_por_noche', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrada', models.DateField()),
                ('fecha_salida', models.DateField()),
                ('estado_reserva', models.CharField(choices=[('confirmada', 'Confirmada'), ('cancelada', 'Cancelada'), ('pendiente', 'Pendiente')], max_length=20)),
                ('numero_personas', models.IntegerField(default=1)),
                ('costo_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente')),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.habitacion')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_emision', models.DateField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pagado', models.BooleanField(default=False)),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.reserva')),
            ],
        ),
    ]
