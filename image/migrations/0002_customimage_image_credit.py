# Generated by Django 3.0.3 on 2020-05-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customimage',
            name='image_credit',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
