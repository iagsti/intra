# Generated by Django 2.2.5 on 2019-10-03 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='access',
            name='status',
            field=models.CharField(choices=[('Autorizado', 'Autorizado'), ('Não autorizado', 'Não autorizado'), ('Para autorização', 'Para autorização')], default='Para autorização', max_length=128, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='access',
            name='enable',
            field=models.BooleanField(default=False, verbose_name='ativar'),
        ),
    ]
