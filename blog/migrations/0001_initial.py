# Generated by Django 4.2.10 on 2024-02-08 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='', max_length=200, unique=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('content', models.TextField()),
                ('audio_one', embed_video.fields.EmbedVideoField(blank=True)),
                ('content_two', models.TextField(blank=True)),
                ('audio_two', embed_video.fields.EmbedVideoField(blank=True)),
                ('content_three', models.TextField(blank=True)),
                ('audio_three', embed_video.fields.EmbedVideoField(blank=True)),
                ('content_four', models.TextField(blank=True)),
                ('audio_four', embed_video.fields.EmbedVideoField(blank=True)),
                ('content_five', models.TextField(blank=True)),
                ('audio_five', embed_video.fields.EmbedVideoField(blank=True)),
                ('mix', models.BooleanField()),
                ('posted_on', models.DateField(auto_now_add=True)),
                ('edited_at', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-posted_on'],
            },
        ),
    ]
