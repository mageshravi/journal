from django.db import models
from tinymce.models import HTMLField
from datetime import datetime


class Post(models.Model):

    title = models.CharField(max_length=128)
    content = HTMLField()
    url = models.CharField(max_length=64)
    is_published = models.BooleanField(default=False)
    published_on = models.DateTimeField(default=datetime.now)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
