from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title