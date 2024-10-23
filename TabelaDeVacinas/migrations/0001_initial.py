# migrations/0001_initial.py

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='UBS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_ubs', models.CharField(max_length=22)),
            ],
            options={
                'db_table': 'ubs',  # Nome da tabela para UBS
            },
        ),
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_vacina', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'vacina',  # Nome da tabela para Vacina
            },
        ),
        migrations.CreateModel(
            name='UBSVacina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(
                    max_length=15,
                    choices=[
                        ('Disponível', 'Disponível'),
                        ('Não Disponível', 'Não Disponível'),
                    ],
                    default='Não Disponível',
                )),
                ('ubs', models.ForeignKey(on_delete=models.CASCADE, to='nome_do_app.ubs')),  # Substitua 'nome_do_app' pelo nome do seu app
                ('vacina', models.ForeignKey(on_delete=models.CASCADE, to='nome_do_app.vacina')),
            ],
            options={
                'db_table': 'ubsvacina',  # Nome da tabela para UBSVacina
            },
        ),
        migrations.CreateModel(
            name='TabelaFuncionamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_abertura', models.TimeField()),
                ('horario_fechamento', models.TimeField()),
                ('ubs', models.ForeignKey(on_delete=models.CASCADE, to='nome_do_app.ubs')),  # Substitua 'nome_do_app' pelo nome do seu app
            ],
            options={
                'db_table': 'tabela_funcionamento',  # Nome da tabela para TabelaFuncionamento
            },
        ),
    ]
