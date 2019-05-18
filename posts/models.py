from datetime import datetime

from django.db import models

from categories.models import Category


class Post(models.Model):

    title = models.CharField(max_length=150)
    intro = models.CharField(max_length=200)
    body = models.TextField()
    media = models.URLField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(default=datetime.now)
    modification_date = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
