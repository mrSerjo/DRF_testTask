from rest_framework import generics
from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict


class ArticleAPIView(APIView):
    def get(self, request):
        art_list = Article.objects.all().values()
        return Response({'posts': ArticleSerializer(art_list, many=True).data})

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': 'Метод PUT не определен'})

        try:
            instance = Article.objects.get(pk=pk)
        except:
            return Response({'error': 'Объект не найден'})

        serializer = ArticleSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': 'Метод PUT не определен'})
        snippet = Article.objects.get(pk=pk)
        snippet.delete()
        return Response({"post": 'Удалить статью ' + str(pk)})