# Generated by Django 2.2.4 on 2023-07-17 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minhaAppProjetoFinal2', '0002_auto_20230717_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='gerente',
            name='idFilial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Filial'),
            preserve_default=False,
        ),
    ]
