from django.db import models


class News(models.Model):
    title = models.CharField(max_length=500)
    time = models.CharField(max_length=500)
    text = models.TextField()

    def __str__(self):
        return self.title