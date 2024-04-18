import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *


# class ProductModel:
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description



class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    slug = serializers.SlugField(read_only=True)
    category_id = serializers.IntegerField()
    description = serializers.CharField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.category_id = validated_data.get("category_id", instance.category_id)
        instance.save()
        return instance


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    slug = serializers.SlugField(read_only=True)
    tree_id = serializers.IntegerField(read_only=True)
    level = serializers.IntegerField(read_only=True)
    parent_id = serializers.IntegerField(allow_null=True, required=False)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.parent_id = validated_data.get("parent_id", instance.parent_id)
        instance.save()
        return instance

    def create(self, validated_data):
        return Category.objects.create(**validated_data)




