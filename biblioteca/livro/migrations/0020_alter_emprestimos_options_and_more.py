# Generated by Django 4.2 on 2023-07-28 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0019_alter_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emprestimos',
            options={'verbose_name': 'Emprestimo'},
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 28, 14, 23, 59, 928716)),
        ),
    ]
