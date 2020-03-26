# Generated by Django 3.0.3 on 2020-02-13 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMateria', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('carrera', models.CharField(max_length=254)),
                ('edad', models.IntegerField()),
                ('direccion', models.CharField(max_length=254)),
                ('genero', models.CharField(max_length=254)),
                ('matricula', models.CharField(max_length=254)),
                ('Materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumno.Materia')),
            ],
        ),
    ]