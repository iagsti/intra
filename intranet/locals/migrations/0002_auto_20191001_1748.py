# Generated by Django 2.2.5 on 2019-10-01 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locals', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locals',
            options={'verbose_name': 'local', 'verbose_name_plural': 'locais'},
        ),
        migrations.AddField(
            model_name='locals',
            name='departament',
            field=models.CharField(default='Astronomia', max_length=128, verbose_name='Departamento'),
        ),
        migrations.AlterField(
            model_name='locals',
            name='build',
            field=models.CharField(max_length=4, verbose_name='Bloco'),
        ),
        migrations.AlterField(
            model_name='locals',
            name='floor',
            field=models.CharField(max_length=50, verbose_name='Pavimento'),
        ),
        migrations.AlterField(
            model_name='locals',
            name='local',
            field=models.CharField(max_length=128, verbose_name='Local'),
        ),
    ]
