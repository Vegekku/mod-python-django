from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
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
    author = models.ForeignKey(get_user_model(), related_name='posts', on_delete=models.CASCADE)
    # author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
