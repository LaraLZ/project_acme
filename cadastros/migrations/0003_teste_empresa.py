# Generated by Django 4.2.1 on 2023-05-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_alter_empresas_afiliacao_cnpj'),
    ]

    operations = [
        migrations.CreateModel(
            name='teste_empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=40)),
            ],
        ),
    ]
