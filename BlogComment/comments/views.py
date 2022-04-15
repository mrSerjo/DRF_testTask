from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(methods=['get'], detail=False)
    def comment_list(self, request):
        com_list = Comment.objects.all()
        return Response({'comment_list': com_list})

    def get_queryset(self):
        return Article.objects.order_by('-time_create')


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer