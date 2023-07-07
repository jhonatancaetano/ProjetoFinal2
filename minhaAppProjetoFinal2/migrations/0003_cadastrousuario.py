# Generated by Django 2.2.4 on 2023-06-16 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minhaAppProjetoFinal2', '0002_postagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='cadastroUsuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nomeUsuario', models.TextField()),
                ('telUsuario', models.IntegerField()),
                ('emailUsuario', models.EmailField(max_length=254)),
                ('senhaUsuario', models.TextField()),
                ('donoRestautanteUsuario', models.BooleanField()),
            ],
        ),
    ]
