# Generated by Django 2.2.4 on 2023-07-17 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minhaAppProjetoFinal2', '0013_remove_relacionamento_idusuario1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='idRelacionamento',
        ),
    ]
