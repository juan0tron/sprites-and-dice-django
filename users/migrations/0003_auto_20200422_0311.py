# Generated by Django 3.0.3 on 2020-04-22 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200422_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='show_email',
            field=models.BooleanField(default=False),
        ),
    ]
