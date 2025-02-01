from django.db import models

class ModelNews(models.Model):
    title   = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
