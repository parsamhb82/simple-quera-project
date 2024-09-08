from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Teacher, Student, Student_answer

class StudentRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=32)

    class Meta:
        model = Student
        fields = ['username', 'password', 'name', 'last_name', 'email']

    def validate(self, data):
        if Student.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('email already exists')
        return data
    
    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        user = User.objects.create_user(
            username=username,
            password=password,
            email=validated_data['email'],
            first_name=validated_data['name'],
            last_name=validated_data['last_name']
        )
        student = Student.objects.create(
            user=user,
            name=validated_data['name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        return student
    

class TeacherRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=32)

    class Meta:
        model = Teacher
        fields = ['username', 'password', 'name', 'last_name', 'email']

    def validate(self, data):
        if Teacher.objects.filter(email=data['email']).exists() or Student.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('email already exists')
        return data
    
    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        user = User.objects.create_user(
            username=username,
            password=password,
            email=validated_data['email'],
            first_name=validated_data['name'],
            last_name=validated_data['last_name']
        )
        teacher = Teacher.objects.create(
            user=user,
            name=validated_data['name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        return teacher
        
class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['name', 'last_name', 'email']

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['name', 'last_name', 'email']

class StudentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_answer
        fields = '__all__'

class AddStudentSerializer(serializers.Serializer):
    student_email = serializers.EmailField()
    class_id = serializers.IntegerField(required=False)
    bootcamp_id = serializers.IntegerField(required=False)

class AddTeacherSerializer(serializers.Serializer):
    teacher_email = serializers.EmailField()
    class_id = serializers.IntegerField(required=False)
    bootcamp_id = serializers.IntegerField(required=False)