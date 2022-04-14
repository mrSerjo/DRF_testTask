import io
from rest_framework import serializers
from .models import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"