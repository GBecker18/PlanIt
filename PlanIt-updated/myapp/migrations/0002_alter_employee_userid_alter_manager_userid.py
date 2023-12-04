# Generated by Django 4.2.5 on 2023-12-02 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='userID',
            field=models.CharField(blank=True, default='54322754', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='userID',
            field=models.CharField(blank=True, default='71474656', max_length=8, unique=True),
        ),
    ]