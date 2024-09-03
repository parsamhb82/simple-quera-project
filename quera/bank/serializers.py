from rest_framework.serializers import ModelSerializer
from .models import Question , Lesson

class QuestionSerializer(ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'

class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
