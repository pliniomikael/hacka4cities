# Generated by Django 4.0.2 on 2022-03-13 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiber', '0005_sensor_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='status',
            field=models.CharField(blank=True, choices=[('Normal', 'NORMAL'), ('Com Vazamento', 'COM VAZAMENTO'), ('Em Manutenção', 'EM MANUTENCAO'), ('Reparo concluído', 'REPARO CONCLUIDO')], max_length=50, null=True, verbose_name='Status'),
        ),
    ]