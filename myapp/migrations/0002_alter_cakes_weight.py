# Generated by Django 4.1.7 on 2023-03-18 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cakes',
            name='weight',
            field=models.CharField(max_length=200),
        ),
    ]
