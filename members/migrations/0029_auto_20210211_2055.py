# Generated by Django 3.1.5 on 2021-02-11 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0028_member_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='civility',
            field=models.CharField(choices=[('no member', 'no member'), ('M', 'Monsieur'), ('Mme', 'Madame'), ('Non souhaitée', 'Non souhaitée'), ('Association', 'Association'), ('Entreprise', 'Entreprise')], default='no member', max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='mail',
            field=models.EmailField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='npa',
            field=models.IntegerField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.IntegerField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.CharField(choices=[('no member', 'no member'), ('member', 'member'), ('staff', 'staff'), ('committee', 'committee')], default='no member', max_length=10),
        ),
    ]
