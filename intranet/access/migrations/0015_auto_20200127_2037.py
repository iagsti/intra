# Generated by Django 3.0.2 on 2020-01-27 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0014_access_weekdays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='weekdays',
            field=models.CharField(choices=[(0, 'Segunda'), (1, 'Terça'), (2, 'Quarta'), (3, 'Quinta'), (4, 'Sexta'), (5, 'Sábado'), (6, 'Domingo')], max_length=20, null=True, verbose_name='dia da semana'),
        ),
    ]
