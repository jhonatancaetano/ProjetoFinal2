# Generated by Django 2.2.4 on 2023-07-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minhaAppProjetoFinal2', '0006_auto_20230709_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lotacao',
            name='idFilial',
        ),
        migrations.RemoveField(
            model_name='lotacao',
            name='idGerente',
        ),
        migrations.RemoveField(
            model_name='lotacao',
            name='idNivel',
        ),
        migrations.RemoveField(
            model_name='lotacao',
            name='idUsuario',
        ),
        migrations.AlterField(
            model_name='lotacao',
            name='dia',
            field=models.DateField(),
        ),
    ]
