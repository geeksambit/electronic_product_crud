# Generated by Django 3.2.9 on 2021-11-13 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211113_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='processor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='ram',
            field=models.CharField(max_length=20),
        ),
    ]