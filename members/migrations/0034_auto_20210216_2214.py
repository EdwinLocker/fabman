# Generated by Django 3.1.5 on 2021-02-16 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0033_auto_20210212_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='visa',
            field=models.CharField(blank=True, default=None, max_length=3, null=True, unique=True),
        ),
    ]