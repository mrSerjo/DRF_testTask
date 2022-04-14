from rest_framework import generics
from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict


class ArticleAPIView(APIView):
    def get(self, request):
        lst = Article.objects.all().values()
        return Response({'lst': lst})

    def post(self, request):
        post_new = Article.objects.create(
            title=request.data['title'],
            content=request.data['content']
        )
        return Response({'post': model_to_dict(post_new)})


# class ArticleAPIView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer