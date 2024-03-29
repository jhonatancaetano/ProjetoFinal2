# Generated by Django 2.2.4 on 2023-07-20 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificacaoDoItem',
            fields=[
                ('idClassificacao', models.AutoField(primary_key=True, serialize=False)),
                ('descItem', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('idFilial', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('rua', models.TextField()),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NivelDeLotacao',
            fields=[
                ('idNivel', models.AutoField(primary_key=True, serialize=False)),
                ('descNivel', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RevisaoDeComentario',
            fields=[
                ('idRevisao', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('conteudo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeComida',
            fields=[
                ('idComida', models.AutoField(primary_key=True, serialize=False)),
                ('descComida', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeIncidenteInterno',
            fields=[
                ('idTipoIncidente', models.AutoField(primary_key=True, serialize=False)),
                ('descIncidente', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeRelacionamento',
            fields=[
                ('idTipoRelacionamento', models.AutoField(primary_key=True, serialize=False)),
                ('descTipoRelacionamento', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('numeroTelefone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.TextField()),
                ('cpf', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('idRestaurante', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('Comida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.TipoDeComida')),
            ],
        ),
        migrations.CreateModel(
            name='Relacionamento',
            fields=[
                ('idRelacionamento', models.AutoField(primary_key=True, serialize=False)),
                ('nomeTipoRelacionamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.TipoDeRelacionamento')),
            ],
        ),
        migrations.CreateModel(
            name='Recomendacao',
            fields=[
                ('idRecomendacao', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('texto', models.TextField()),
                ('nomeFilial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Filial')),
                ('nomeUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Lotacao',
            fields=[
                ('idLotacao', models.AutoField(primary_key=True, serialize=False)),
                ('dia', models.DateField()),
                ('hora', models.TimeField()),
                ('nomeFilial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Filial')),
                ('nomeNivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.NivelDeLotacao')),
                ('nomeUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ItensDeConsumo',
            fields=[
                ('idItem', models.AutoField(primary_key=True, serialize=False)),
                ('nomeItem', models.TextField()),
                ('precoItem', models.FloatField()),
                ('nomeClassificacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.ClassificacaoDoItem')),
                ('nomeFilial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Filial')),
                ('nomeUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='IncidenteInterno',
            fields=[
                ('idIncidente', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('descricao', models.TextField()),
                ('nomeFilial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Filial')),
                ('nomeTipoDeIncidente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.TipoDeIncidenteInterno')),
                ('nomeUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('idGerente', models.AutoField(primary_key=True, serialize=False)),
                ('Filial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Filial')),
                ('nomeUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='filial',
            name='nomeRestaurante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Restaurante'),
        ),
        migrations.CreateModel(
            name='EventoExterno',
            fields=[
                ('idEvento', models.AutoField(primary_key=True, serialize=False)),
                ('dataEvento', models.DateField()),
                ('horaEvento', models.TimeField()),
                ('rua', models.TextField()),
                ('numero', models.IntegerField()),
                ('bairro', models.TextField()),
                ('cidade', models.TextField()),
                ('descricao', models.TextField()),
                ('nomeUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('idComentario', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('conteudo', models.TextField()),
                ('nomeItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.ItensDeConsumo')),
                ('nomeUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='AssociacaoUsuarioUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeTipoRelacionamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.TipoDeRelacionamento')),
                ('nomeUsuarioPrincipal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='associacao_usuario1', to='minhaAppProjetoFinal2.Usuario')),
                ('nomeUsuarioSecundario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='associacao_usuario2', to='minhaAppProjetoFinal2.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='AssociacaoRestauranteUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeRestaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Restaurante')),
                ('nomeUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='AssociacaoItemDeConsumoRecomendacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.ItensDeConsumo')),
                ('nomeRecomendacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Recomendacao')),
            ],
        ),
        migrations.CreateModel(
            name='AssociacaoFilialEventoExterno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeEvento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.EventoExterno')),
                ('nomeFilial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minhaAppProjetoFinal2.Filial')),
            ],
        ),
        migrations.AddConstraint(
            model_name='associacaousuariousuario',
            constraint=models.UniqueConstraint(fields=('nomeUsuarioPrincipal', 'nomeUsuarioSecundario', 'nomeTipoRelacionamento'), name='chave_primaria_concatenada'),
        ),
    ]
