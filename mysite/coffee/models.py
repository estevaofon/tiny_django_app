from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField(max_length = 1000)

    def __str__(self):
            return self.title
