# Generated by Django 4.2.1 on 2023-05-11 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresas_afiliacao',
            name='cnpj',
            field=models.IntegerField(),
        ),
    ]