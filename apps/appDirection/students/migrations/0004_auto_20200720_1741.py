# Generated by Django 3.0.6 on 2020-07-20 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20200720_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_cuatrimestre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='student_especialidad',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='student_estatus',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='student_grupo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='cuatrimestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student_cuatrimestre'),
        ),
        migrations.AlterField(
            model_name='student',
            name='especialidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student_especialidad'),
        ),
        migrations.AlterField(
            model_name='student',
            name='estatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student_estatus'),
        ),
        migrations.AlterField(
            model_name='student',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student_grupo'),
        ),
    ]
