# Generated by Django 2.2.4 on 2023-07-17 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minhaAppProjetoFinal2', '0009_auto_20230717_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='idRelacionamento',
        ),
        migrations.AddField(
            model_name='relacionamento',
            name='idUsuario1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Usuario'),
            preserve_default=False,
        ),
    ]