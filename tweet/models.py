from django.db import models


class Tweet(models.Model):
    message = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
