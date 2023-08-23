from rest_framework import serializers
from .models import *
from django.utils import timezone


class TaskSerializer(serializers.ModelSerializer):

    def validate_deadline(self, value):
        if value and value <= timezone.now():
            raise serializers.ValidationError("Deadline must be in the future.")
        return value
    class Meta:
        model = Task
        fields = "__all__"

    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"