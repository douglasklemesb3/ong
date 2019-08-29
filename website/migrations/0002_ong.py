# Generated by Django 2.2.4 on 2019-08-29 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_responsavel', models.CharField(max_length=50, verbose_name='Responsavel')),
                ('nome_ong', models.CharField(max_length=50, verbose_name='Nome da ong')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('telefone', models.CharField(max_length=10, verbose_name='telefone')),
                ('horario_atendimento', models.CharField(blank=True, max_length=50, null=True, verbose_name='horario de atendimento')),
                ('observacoes', models.CharField(max_length=50, verbose_name='observacoes')),
            ],
        ),
    ]
