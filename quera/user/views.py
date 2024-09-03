from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import Teacher, Student, Student_answer
from django.shortcuts import render
import json
from django.db import IntegrityError
from .models import Question, Class, Bootcamp
from django.contrib.auth.hashers import make_password
from .serializers import StudentRegisterSerializer, TeacherRegisterSerializer, StudentAnswerSerializer, StudentSerializer, TeacherSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass
class TeachersListView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RetrieveTeacherView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class RetrieveStudentView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer




class CreatStudentAnswer(CreateAPIView):
    queryset = Student_answer.objects.all()
    serializer_class = StudentAnswerSerializer
    permission_classes = [IsAuthenticated]

class OwnStudentAnswer(ListAPIView):
    queryset = Student_answer.objects.all()
    serializer_class = StudentAnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Student_answer.objects.filter(student=self.request.user.student)


@csrf_exempt
def add_student_to_class(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student = Student.objects.get(email=data['student_email'])
            class_id = data['class_id']
            class_to_add = Class.objects.get(id=class_id)
            student.classes.add(class_to_add)
            student.save()
            return JsonResponse({'message': 'student added to class successfully'}, safe=False)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'student does not exist'}, safe=False)
        except Class.DoesNotExist:
            return JsonResponse({'error': 'class does not exist'}, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, safe=False)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Post request required'}, status=405)
@csrf_exempt
def add_student_to_bootcamp(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student = Student.objects.get(email=data['student_email'])
            bootcamp_id = data['bootcamp_id']
            bootcamp_to_add = Bootcamp.objects.get(id=bootcamp_id)
            student.bootcamps.add(bootcamp_to_add)
            student.save()
            return JsonResponse({'message': 'student added to bootcamp successfully'}, safe=False)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'student does not exist'}, safe=False)
        except Bootcamp.DoesNotExist:
            return JsonResponse({'error': 'bootcamp does not exist'}, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, safe=False)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Post request required'}, status=405)
@csrf_exempt
def add_teacher_to_class(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            teacher = Teacher.objects.get(email=data['teacher_email'])
            class_id = data['class_id']
            class_to_add = Class.objects.get(id=class_id)
            teacher.classes.add(class_to_add)
            teacher.save()
            return JsonResponse({'message': 'teacher added to class successfully'}, safe=False)
        except Teacher.DoesNotExist:
            return JsonResponse({'error': 'teacher does not exist'}, safe=False)
        except Class.DoesNotExist:
            return JsonResponse({'error': 'class does not exist'}, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, safe=False)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Post request required'}, status=405)
@csrf_exempt
def add_teacher_to_bootcamp(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            teacher = Teacher.objects.get(email=data['teacher_email'])
            bootcamp_id = data['bootcamp_id']
            bootcamp_to_add = Bootcamp.objects.get(id=bootcamp_id)
            teacher.bootcamps.add(bootcamp_to_add)
            teacher.save()
            return JsonResponse({'message': 'teacher added to bootcamp successfully'}, safe=False)
        except Teacher.DoesNotExist:
            return JsonResponse({'error': 'teacher does not exist'}, safe=False)
        except Bootcamp.DoesNotExist:
            return JsonResponse({'error': 'bootcamp does not exist'}, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, safe=False)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
class StudentRegisterationView(APIView):
    def post(self, request):
        serializer = StudentRegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TeacherRegistrationView(APIView):
    def post(self, request):
        serilizer = TeacherRegisterSerializer(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
    

