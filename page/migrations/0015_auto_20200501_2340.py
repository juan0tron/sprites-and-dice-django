# Generated by Django 3.0.3 on 2020-05-01 23:40

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0014_blogpage_legacy_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='legacy_url',
        ),
        migrations.CreateModel(
            name='LegacyUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('path', models.CharField(max_length=255)),
                ('blogpage', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='legacy_urls', to='page.BlogPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
