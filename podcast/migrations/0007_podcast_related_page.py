# Generated by Django 3.0.3 on 2020-05-05 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0018_blogpage_header_video'),
        ('podcast', '0006_podcast_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='related_page',
            field=models.ForeignKey(blank=True, help_text='The associated announcement post for this episode.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='page.BlogPage'),
        ),
    ]
