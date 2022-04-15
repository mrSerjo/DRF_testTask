from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.RESTRICT)
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    parrent_comment = models.ForeignKey('self', default=None, blank=True, null=True, on_delete=models.RESTRICT)
