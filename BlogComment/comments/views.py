from rest_framework import generics
from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer


class ArticleAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer