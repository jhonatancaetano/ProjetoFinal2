# Generated by Django 2.2.4 on 2023-07-19 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minhaAppProjetoFinal2', '0010_auto_20230719_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventoexterno',
            name='idGerente',
        ),
        migrations.RemoveField(
            model_name='incidenteinterno',
            name='idGerente',
        ),
        migrations.RemoveField(
            model_name='itensdeconsumo',
            name='idGerente',
        ),
        migrations.RemoveField(
            model_name='lotacao',
            name='idGerente',
        ),
        migrations.AddField(
            model_name='gerente',
            name='idUsuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Usuario'),
            preserve_default=False,
        ),
    ]