# Generated by Django 4.2 on 2023-07-07 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='ativo',
            field=models.BooleanField(default=False),
        ),
    ]
