# Generated by Django 2.2.4 on 2023-07-17 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minhaAppProjetoFinal2', '0006_comentario_iditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='idItem',
            new_name='Item',
        ),
    ]
