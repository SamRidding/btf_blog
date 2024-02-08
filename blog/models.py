from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from taggit.managers import TaggableManager


class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, unique=True, default="")
    image = models.ImageField(
        upload_to='images/', blank=False
    )
    content = models.TextField(blank=False)
    audio_one = EmbedVideoField(blank=True)
    content_two = models.TextField(blank=True)
    audio_two = EmbedVideoField(blank=True)
    content_three = models.TextField(blank=True)
    audio_three = EmbedVideoField(blank=True)
    content_four = models.TextField(blank=True)
    audio_four = EmbedVideoField(blank=True)
    content_five = models.TextField(blank=True)
    audio_five = EmbedVideoField(blank=True)
    mix = models.BooleanField()
    posted_on = models.DateField(auto_now_add=True)
    edited_at = models.DateField(auto_now_add=True)

    tags = TaggableManager()

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return f'{self.id} {self.title}'
