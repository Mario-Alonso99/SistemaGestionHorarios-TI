# Generated by Django 3.0.6 on 2020-07-27 20:15

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('matricula', models.TextField(max_length=15, verbose_name='Matrícula')),
                ('especialidad', models.TextField(choices=[('Área Entornos Virtuales y Negocios Digitales', 'Área Entornos Virtuales y Negocios Digitales'), ('Área Infraestructura de Redes Digitales', 'Área Infraestructura de Redes Digitales'), ('Área Desarrollo de Software Multiplataforma', 'Área Desarrollo de Software Multiplataforma')], default='Área Entornos Virtuales y Negocios Digitales')),
                ('cuatrimestre', models.TextField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11')], default='1')),
                ('grupo', models.TextField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='A')),
                ('estatus', models.TextField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo')),
                ('tipo', models.TextField(default='Estudiante', max_length=20, verbose_name='Tipo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
