# Generated by Django 3.0.2 on 2020-01-27 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0013_auto_20191212_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='access',
            name='weekdays',
            field=models.CharField(max_length=20, null=True, verbose_name='dia da semana'),
        ),
    ]
