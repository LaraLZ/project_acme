# Generated by Django 4.2.1 on 2023-05-17 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_delete_teste_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresas',
            name='status',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True),
        ),
        migrations.AlterField(
            model_name='empresas_afiliacao',
            name='status',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True),
        ),
    ]