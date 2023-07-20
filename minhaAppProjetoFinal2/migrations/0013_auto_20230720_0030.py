# Generated by Django 2.2.4 on 2023-07-20 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minhaAppProjetoFinal2', '0012_auto_20230720_0010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='associacaofilialeventoexterno',
            old_name='Evento',
            new_name='nomeEvento',
        ),
        migrations.RenameField(
            model_name='associacaofilialeventoexterno',
            old_name='Filial',
            new_name='nomeFilial',
        ),
        migrations.RenameField(
            model_name='associacaoitemdeconsumorecomendacao',
            old_name='Item',
            new_name='nomeItem',
        ),
        migrations.RenameField(
            model_name='associacaoitemdeconsumorecomendacao',
            old_name='Recomendacao',
            new_name='nomeRecomendacao',
        ),
        migrations.RenameField(
            model_name='associacaorestauranteusuario',
            old_name='Restaurante',
            new_name='nomeRestaurante',
        ),
        migrations.RenameField(
            model_name='associacaorestauranteusuario',
            old_name='Usuario',
            new_name='nomeUsuario',
        ),
        migrations.RenameField(
            model_name='associacaousuariousuario',
            old_name='TipoRelacionamento',
            new_name='nomeTipoRelacionamento',
        ),
        migrations.RenameField(
            model_name='associacaousuariousuario',
            old_name='UsuarioSecundario',
            new_name='nomeUsuarioSecundario',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='Item',
            new_name='nomeItem',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='Usuario',
            new_name='nomeUsuario',
        ),
        migrations.RenameField(
            model_name='eventoexterno',
            old_name='Usuario',
            new_name='nomeUsuario',
        ),
        migrations.RenameField(
            model_name='filial',
            old_name='Restaurante',
            new_name='nomeRestaurante',
        ),
        migrations.RenameField(
            model_name='gerente',
            old_name='Usuario',
            new_name='nomeUsuario',
        ),
        migrations.RenameField(
            model_name='incidenteinterno',
            old_name='Filial',
            new_name='nomeFilial',
        ),
        migrations.RenameField(
            model_name='incidenteinterno',
            old_name='TipoDeIncidente',
            new_name='nomeTipoDeIncidente',
        ),
        migrations.RenameField(
            model_name='incidenteinterno',
            old_name='Usuario',
            new_name='nomeUsuario',
        ),
        migrations.RenameField(
            model_name='itensdeconsumo',
            old_name='Classificacao',
            new_name='nomeClassificacao',
        ),
        migrations.RenameField(
            model_name='itensdeconsumo',
            old_name='Filial',
            new_name='nomeFilial',
        ),
        migrations.RenameField(
            model_name='itensdeconsumo',
            old_name='Usuario',
            new_name='nomeUsuario',
        ),
        migrations.RenameField(
            model_name='lotacao',
            old_name='Filial',
            new_name='nomeFilial',
        ),
        migrations.RenameField(
            model_name='lotacao',
            old_name='Nivel',
            new_name='nomeNivel',
        ),
        migrations.RenameField(
            model_name='lotacao',
            old_name='Usuario',
            new_name='nomeUsuario',
        ),
        migrations.RenameField(
            model_name='recomendacao',
            old_name='Filial',
            new_name='nomeFilial',
        ),
        migrations.RenameField(
            model_name='recomendacao',
            old_name='Usuario',
            new_name='nomeUsuario',
        ),
        migrations.RenameField(
            model_name='relacionamento',
            old_name='TipoRelacionamento',
            new_name='nomeTipoRelacionamento',
        ),
    ]
