from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_coments(self):
        return Comments.objects.filter(article=self)

class Comments(models.Model):
    article = models.ForeignKey(Article, default=1)
    body = models.TextField()

    def get_shot_body(self):
        return self.body[:100]

    def __str__(self):
        return self.body