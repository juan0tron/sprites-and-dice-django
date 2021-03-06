# Generated by Django 3.0.3 on 2020-05-02 02:48

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0016_auto_20200502_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='content',
            field=wagtail.core.fields.StreamField([('Image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'], required=False))])), ('Rich_Text', wagtail.core.blocks.RichTextBlock()), ('Podcast', wagtail.core.blocks.StructBlock([('podcast', wagtail.snippets.blocks.SnippetChooserBlock('podcast.Podcast'))], icon='fa-headphones')), ('Game', wagtail.core.blocks.StructBlock([('game', wagtail.snippets.blocks.SnippetChooserBlock('game.Game'))], icon='fa-pencil'))], blank=True),
        ),
    ]
