# Generated by Django 3.0.6 on 2020-07-22 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20200720_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='especialidad',
            field=models.TextField(choices=[('Área Entornos Virtuales y Negocios Digitales', 'Área Entornos Virtuales y Negocios Digitales'), ('Área Infraestructura de Redes Digitales', 'Área Infraestructura de Redes Digitales'), ('Área Desarrollo de Software Multiplataforma', 'Área Desarrollo de Software Multiplataforma')], default='Área Entornos Virtuales y Negocios Digitales'),
        ),
    ]
