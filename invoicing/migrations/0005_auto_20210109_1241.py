# Generated by Django 3.1.4 on 2021-01-09 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0004_auto_20210109_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountentry',
            name='amount_cash',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='accountentry',
            name='amount_machine',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
