from django.db import models

class Hymn(models.Model):
    hymn = models.TextField()
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
