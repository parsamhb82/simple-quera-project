from rest_framework.serializers import ModelSerializer
from .models import Class, Bootcamp


class ClassSerializer(ModelSerializer):

    class Meta:
        model = Class
        fields = '__all__'

class BootcampSerializer(ModelSerializer):

    class Meta:
        model = Bootcamp
        fields = '__all__'
