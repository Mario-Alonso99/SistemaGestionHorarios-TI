# Generated by Django 3.0.6 on 2020-07-30 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=200, verbose_name='Nombre')),
                ('especialidad', models.TextField(choices=[('Área Entornos Virtuales y Negocios Digitales', 'Área Entornos Virtuales y Negocios Digitales'), ('Área Infraestructura de Redes Digitales', 'Área Infraestructura de Redes Digitales'), ('Área Desarrollo de Software Multiplataforma', 'Área Desarrollo de Software Multiplataforma')], default='Área Entornos Virtuales y Negocios Digitales')),
                ('cuatrimestre', models.TextField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11')], default='1')),
            ],
            options={
                'verbose_name': 'Asignatura',
                'verbose_name_plural': 'Asignaturas',
                'ordering': ['especialidad', 'cuatrimestre'],
            },
        ),
    ]
