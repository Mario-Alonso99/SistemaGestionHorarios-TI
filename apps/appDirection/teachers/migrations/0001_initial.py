# Generated by Django 3.0.6 on 2020-07-29 21:40

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
            name='Teacher',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('matricula', models.TextField(max_length=15, verbose_name='Matrícula')),
                ('grado_academico', models.TextField(default='', max_length=200, verbose_name='Grado academico')),
                ('tjornada', models.TextField(choices=[('AP', 'AP'), ('TCP', 'TCP')], default='AP')),
                ('numero_empleado', models.TextField(max_length=200, verbose_name='Número de empleado')),
                ('estatus', models.TextField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo')),
                ('tipo', models.TextField(default='Docente', max_length=20, verbose_name='Tipo')),
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
