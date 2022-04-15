import io
from rest_framework import serializers
from .models import *
from rest_framework_recursive.fields import RecursiveField


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    #parent_id = serializers.ListField(child=RecursiveField())
    class Meta:
        model = Comment
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'