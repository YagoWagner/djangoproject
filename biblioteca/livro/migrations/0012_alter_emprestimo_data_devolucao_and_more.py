# Generated by Django 4.2 on 2023-07-14 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0011_alter_emprestimo_nome_emprestado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(blank=True, null=True),
        ),
    ]
