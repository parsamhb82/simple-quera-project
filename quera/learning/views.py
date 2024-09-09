from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user.models import Teacher, Student, Student_answer
from rest_framework.views import APIView
from django.shortcuts import render
import json
from rest_framework.response import Response
from bank.models import Question,  Lesson
from learning.models import Class ,Bootcamp
from django.db import IntegrityError
from .serializers import ClassSerializer, BootcampSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from user.permissions import IsSuperUser, IsTeacher, IsStudent


def bootcamp_list(request):
    bootcamps = Bootcamp.objects.all()
    data = []
    for bootcamp in bootcamps:
        data.append({
            'name' : bootcamp.name,
            'start_date' : bootcamp.start_date,
            'price' : bootcamp.price
        })
    return JsonResponse(data, safe=False)
def classes_list(request):
    classes = Class.objects.all()
    data = []
    for class_ in classes:
        data.append({
            'name' : class_.name,
            'assignments' : [assignmet.name for assignmet in class_.assingment.all()],
            'lessons' : [lesson.subject for lesson in class_.lesson.all()],
        })
    return JsonResponse(data, safe=False)
@csrf_exempt
def creat_class(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            class_name = data['class_name']

            teacher_id = data['teacher_id']
            teacher = Teacher.objects.get(id=teacher_id)
            teacher : Teacher
            class_ = Class.objects.create(name=class_name)
            class_.save()
            teacher.classes.add(class_)
            teacher.save()
            return JsonResponse({'message': 'class created successfully and teacher was assigned to it'}, safe=False)
        except Teacher.DoesNotExist:
            return JsonResponse({'error': 'teacher does not exist'}, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, safe=False)
    else:
        return JsonResponse({'error': 'Post request required'}, status=405)
@csrf_exempt
def add_assignmet_to_class(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            class_id = data['class_id']
            class_to_add = Class.objects.get(id=class_id)
            assignmet_id = data['assignmet_id']
            assignmet_to_add = Question.objects.get(id=assignmet_id)
            class_to_add.assingment.add(assignmet_to_add)
            class_to_add.save()
            return JsonResponse({'message': 'assignmet added to class successfully'}, safe=False)
        except Class.DoesNotExist:
            return JsonResponse({'error': 'class does not exist'}, safe=False)
        except Lesson.DoesNotExist:
            return JsonResponse({'error': 'assignmet does not exist'}, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, safe=False)
    else:
        return JsonResponse({'error': 'Post request required'}, status=405)
@csrf_exempt
def add_lesson_to_class(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            class_id = data['class_id']
            class_to_add = Class.objects.get(id=class_id)
            lesson_id = data['lesson_id']
            lesson_to_add = Lesson.objects.get(id=lesson_id)
            class_to_add.lesson.add(lesson_to_add)
            class_to_add.save()
            return JsonResponse({'message': 'lesson added to class successfully'}, safe=False)
        except Class.DoesNotExist:
            return JsonResponse({'error': 'class does not exist'}, safe=False)
        except Lesson.DoesNotExist:
            return JsonResponse({'error': 'lesson does not exist'}, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, safe=False)
    else:
        return JsonResponse({'error': 'Post request required'}, status=405)
@csrf_exempt
def add_bootcamp(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            bootcamp_name = data['bootcamp_name']
            start_date = data['start_date']
            price = data['price']
            bootcamp = Bootcamp.objects.create(name=bootcamp_name, start_date=start_date, price=price)
            teacher_id = data['teacher_id']
            teacher = Teacher.objects.get(id=teacher_id)
            teacher : Teacher
            teacher.bootcamps.add(bootcamp)
            teacher.save()
            bootcamp.save()
            return JsonResponse({'message': 'bootcamp created successfully and teacher was assigned to it'}, safe=False)
        except Bootcamp.DoesNotExist:
            return JsonResponse({'error': 'bootcamp not created'}, safe=False)
        except Teacher.DoesNotExist:
            return JsonResponse({'error': 'teacher does not exist'}, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error' : 'incorrect json data'}, safe=False)
        except Exception as e :
            return JsonResponse({'error': str(e)}, safe=False)
    else:
        return JsonResponse({'error': 'Post request required'}, status=405)

def get_class(request, class_id):
    try:
        class_ = Class.objects.get(id=class_id)
        return JsonResponse({
            'class_name' : class_.name,
            'lessons' : [lesson.subject for lesson in class_.lesson.all()],
            'assingments' : [assignmet.name for assignmet in class_.assingment.all()],
        }, safe=False)
    
    except Class.DoesNotExist:
        return JsonResponse({'error': 'class does not exist'}, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False)

def get_bootcamp(request, bootcamp_id):
    try:
        bootcamp = Bootcamp.objects.get(id=bootcamp_id)
        return JsonResponse({
            'bootcamp_name' : bootcamp.name,
            'bootcamp_price' : bootcamp.price,
            'bootcamp_start_date' : bootcamp.start_date,
            'bootcamp_duration' : bootcamp.duration

        }, safe=False)

    except Bootcamp.DoesNotExist:
        return JsonResponse({'error': 'bootcamp does not exist'}, safe=False)
    except Exception as e:
        return JsonResponse({'error' : f'error {str(e)}'})

class BootcampListView(ListAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Bootcamp.objects.all()
    serializer_class = BootcampSerializer

class ClassListView(ListAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class RetrieveBootcampView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Bootcamp.objects.all()
    serializer_class = BootcampSerializer

class RetrieveClassView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class CreatClass(CreateAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class CreatBootcamp(CreateAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Bootcamp.objects.all()
    serializer_class = BootcampSerializer

from .serializers import AddAssignmentSerializer
class AddAssignmentToClassView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]
    def post(self, request, class_id):
        serializer = AddAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            class_id = serializer.validated_data['class_id']
            assignmet_id = serializer.validated_data['assignmet_id']
            try:
                class_to_add = Class.objects.get(id=class_id)
                if request.user.teacher.id != class_to_add.teacher.id:
                    return Response({'error': 'You are not allowed to add assignment to this class'}, status=status.HTTP_403_FORBIDDEN)
                assignmet_to_add = Question.objects.get(id=assignmet_id)
                class_to_add.assingment.add(assignmet_to_add)
                class_to_add.save()
                return Response({'message': 'Assignment added to class successfully'}, status=status.HTTP_200_OK)
            except Class.DoesNotExist:
                return Response({'error': 'Class does not exist'}, status=status.HTTP_404_NOT_FOUND)
            except Question.DoesNotExist:
                return Response({'error': 'Assignment does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from .serializers import AddLessonSerializer

class AddLessonSerilizer(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]
    def post(self, request, class_id):
        serializer = AddLessonSerializer(data=request.data)
        if serializer.is_valid():
            class_id = serializer.validated_data['class_id']
            lesson_id = serializer.validated_data['lesson_id']
            try:
                class_to_add = Class.objects.get(id=class_id)
                if request.user.teacher.id != class_to_add.teacher.id:
                    return Response({'error': 'You are not allowed to add lesson to this class'}, status=status.HTTP_403_FORBIDDEN)
                lesson_to_add = Lesson.objects.get(id=lesson_id)
                class_to_add.lesson.add(lesson_to_add)
                class_to_add.save()
                return Response({'message': 'Lesson added to class successfully'}, status=status.HTTP_200_OK)
            except Class.DoesNotExist:
                return Response({'error': 'Class does not exist'}, status=status.HTTP_404_NOT_FOUND)
            except Lesson.DoesNotExist:
                return Response({'error': 'Lesson does not exist'}, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

