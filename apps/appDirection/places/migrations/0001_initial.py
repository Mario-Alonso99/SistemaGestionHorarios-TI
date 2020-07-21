# Generated by Django 3.0.6 on 2020-07-21 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=200, verbose_name='Nombre')),
                ('tipo', models.TextField(choices=[('Aula', 'Aula'), ('Laboratorio', 'Laboratorio')], default='Aula')),
                ('encargado', models.TextField(choices=[('Julia Gabriela Nieva Paredes', 'Julia Gabriela Nieva Paredes'), ('Rosa María Macias Muñoz', 'Rosa María Macias Muñoz'), ('José Marin Rugerio Atriano', 'José Marin Rugerio Atriano'), ('Blanca Aurelia Jimenez Gomez', 'Blanca Aurelia Jimenez Gomez'), ('Sonia López Rodríguez', 'Sonia López Rodríguez'), ('Margarita Lima Esteban', 'Margarita Lima Esteban'), ('Maricela Gress Roldan', 'Maricela Gress Roldan'), ('Ruth Cervantes Gaspar', 'Ruth Cervantes Gaspar'), ('Arcángel Zamora García', 'Arcángel Zamora García'), ('Elizabeth Cortes Ramos', 'Elizabeth Cortes Ramos'), ('Francisco López Briones', 'Francisco López Briones')], default='Julia Gabriela Nieva Paredes')),
                ('ubicacion', models.TextField(blank=True, choices=[('Edificio F Planta Baja', 'Edificio F Planta Baja'), ('Edificio F Planta Alta', 'Edificio F Planta Alta'), ('Biblioteca', 'Biblioteca')], default='Edificio F Planta Baja')),
            ],
            options={
                'verbose_name': 'Lugar',
                'verbose_name_plural': 'Lugares',
                'ordering': ['tipo', 'ubicacion', 'encargado'],
            },
        ),
    ]
