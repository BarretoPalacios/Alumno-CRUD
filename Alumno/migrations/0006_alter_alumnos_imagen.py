# Generated by Django 4.2.5 on 2023-11-16 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0005_alter_alumnos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
