# Generated by Django 4.2 on 2023-07-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0004_alter_usuario_idade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id_usuario',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]