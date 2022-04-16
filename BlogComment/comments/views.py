from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(methods=['get'], detail=False)
    def get_queryset(self):
        articles = Article.objects.order_by('-time_create')

        for article in articles:
            comments = []
            for comment in Comment.objects.all():
                if comment.article.id == article.id:
                    comments.append(comment.content)
            article.comments = comments
        return articles


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer