# Generated by Django 4.2.3 on 2023-07-30 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estudiante',
            new_name='Alumno',
        ),
        migrations.RenameModel(
            old_name='Curso',
            new_name='Clases',
        ),
        migrations.RenameModel(
            old_name='Profesor',
            new_name='Instructores',
        ),
        migrations.RenameField(
            model_name='clases',
            old_name='comision',
            new_name='codigo',
        ),
    ]