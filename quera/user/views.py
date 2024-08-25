from django.http import JsonResponse
from .models import Teacher, Student

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

def techer_detail():
    pass