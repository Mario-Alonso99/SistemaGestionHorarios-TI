# Generated by Django 3.0.6 on 2020-07-23 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='ubicacion',
            field=models.TextField(blank=True, choices=[('Edificio P Planta Baja', 'Edificio P Planta Baja'), ('Edificio P Planta Alta', 'Edificio P Planta Alta'), ('Biblioteca', 'Biblioteca')], default='Edificio F Planta Baja'),
        ),
    ]