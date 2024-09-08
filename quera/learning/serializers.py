from rest_framework.serializers import ModelSerializer, Serializer
from .models import Class, Bootcamp


class ClassSerializer(ModelSerializer):

    class Meta:
        model = Class
        fields = '__all__'

class BootcampSerializer(ModelSerializer):

    class Meta:
        model = Bootcamp
        fields = '__all__'

from rest_framework import serializers

class AddAssignmentSerializer(serializers.Serializer):
    class_id = serializers.IntegerField()
    assignmet_id = serializers.IntegerField()

class AddLessonSerializer(serializers.Serializer):
    class_id = serializers.IntegerField()
    Lesson_id = serializers.IntegerField()