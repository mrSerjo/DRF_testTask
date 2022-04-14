import io
from rest_framework import serializers
from .models import Article
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    comments = serializers.CharField(read_only=True)


    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance