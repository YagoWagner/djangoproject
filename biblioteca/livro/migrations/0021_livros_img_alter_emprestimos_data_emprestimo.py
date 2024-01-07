# Generated by Django 4.2 on 2023-07-28 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0020_alter_emprestimos_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='capa_livro'),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 28, 14, 57, 53, 498338)),
        ),
    ]
