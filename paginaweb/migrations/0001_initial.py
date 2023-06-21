# Generated by Django 4.2.1 on 2023-06-21 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_solicitud',
            fields=[
                ('id_tipo_solicitud', models.AutoField(db_column='idTipo_solicitud', primary_key=True, serialize=False)),
                ('tipo_solicitud', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Subir',
            fields=[
                ('id_subir', models.AutoField(db_column='idSubir', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('mensaje', models.TextField(max_length=1000)),
                ('fecha', models.DateField()),
                ('telefono', models.CharField(max_length=9)),
                ('categorias', models.CharField(max_length=50)),
                ('seleccionar', models.CharField(max_length=15)),
                ('id_tipo_solicitud', models.ForeignKey(db_column='idTipo_solicitud', on_delete=django.db.models.deletion.CASCADE, to='paginaweb.tipo_solicitud')),
            ],
        ),
    ]
