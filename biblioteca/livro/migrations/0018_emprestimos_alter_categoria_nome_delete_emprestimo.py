# Generated by Django 4.2 on 2023-07-25 17:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_ativo'),
        ('livro', '0017_alter_emprestimo_data_emprestimo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_emprestado_anonimo', models.CharField(blank=True, max_length=30, null=True)),
                ('data_emprestimo', models.DateTimeField(default=datetime.datetime(2023, 7, 25, 14, 57, 55, 404779))),
                ('data_devolucao', models.DateTimeField(blank=True, null=True)),
                ('avaliacao', models.CharField(blank=True, choices=[('P', 'Péssimo'), ('R', 'Ruim'), ('B', 'Bom'), ('O', 'Ótimo')], max_length=1, null=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='livro.livros')),
                ('nome_emprestado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario')),
            ],
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Emprestimo',
        ),
    ]