from django.contrib.admin import register, ModelAdmin
from user.models import Teacher, Student, Student_answer

@register(Teacher)
class TeacherAdmin(ModelAdmin):
    list_display = [
        "name",
        "last_name",
        "email",
    ]
@register(Student)
class StudentAdmin(ModelAdmin):
    list_display = [
        "name",
        "last_name",
        "email",
    ]
@register(Student_answer)
class Student_answerAdmin(ModelAdmin):
    list_display = [
        'student',
        'question',
        'answer',
        'true_percentange'
    ]