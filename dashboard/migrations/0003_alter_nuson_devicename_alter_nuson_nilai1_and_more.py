# Generated by Django 4.2.6 on 2023-10-23 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_nuson_devicename_alter_nuson_nilai1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nuson',
            name='deviceName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='nuson',
            name='nilai1',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='nuson',
            name='nilai2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='nuson',
            name='nilai3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='nuson',
            name='nilai4',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='nuson',
            name='nilai5',
            field=models.FloatField(),
        ),
    ]
