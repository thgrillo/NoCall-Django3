# Generated by Django 3.1.3 on 2020-11-26 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thcore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='inorout',
            field=models.CharField(default='', max_length=10),
        ),
    ]
