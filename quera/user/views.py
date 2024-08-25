from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Teacher, Student
from django.shortcuts import render
from django.http import get_object_or_404
import json

def teacher_list(request):
    teachers = Teacher.objects.all()
    data = []
    for teacher in teachers:
        data.append({
            'name' : teacher.name, 
            'last_name' : teacher.last_name,
            'email' : teacher.email,
            'classes' : list(teacher.classes.values('name')),
            'bootcamps' : list(teacher.bootcamps.values('name'))
        })
    return JsonResponse(data, safe=False)

def student_list(request):
    students = Student.objects.all()
    data = []
    for student in students:
        data.append({
            'name' : student.name,
            'last_name' : student.last_name,
            'email' : student.email,
            'classes' : list(student.classes.values('name')),
            'bootcamps' : list(student.bootcamps.values('name'))
        })
    return JsonResponse(data, safe=False)

@csrf_exempt
def techer_detail(request):
    if request.method == 'POST':
        try:
            data.json.loads(request.body)
            teacher_id = data.get(teacher_id)
            teacher = get_object_or_404(Teacher, pk=teacher_id)
            response_data = {
                'name': teacher.name,
                'last_name': teacher.last_name,
                'email': teacher.email,
                'classes': list(teacher.classes.values('name')),
                'bootcamps': list(teacher.bootcamps.values('name')),
            }
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'POST request required'}, status=405)


@csrf_exempt
def student_detail(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  
            student_id = data.get('student_id')

            student = get_object_or_404(Student, pk=student_id)
            response_data = {
                'name': student.name,
                'last_name': student.last_name,
                'email': student.email,
                'classes': list(student.classes.values('name')),
                'bootcamps': list(student.bootcamps.values('name')),
            }
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'POST request required'}, status=405)
