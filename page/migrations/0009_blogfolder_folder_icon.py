# Generated by Django 3.0.3 on 2020-04-24 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
        ('page', '0008_auto_20200416_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogfolder',
            name='folder_icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='image.CustomImage'),
        ),
    ]
