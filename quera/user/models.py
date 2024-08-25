from django.db import models
from learning.models import Class ,Bootcamp
from bank.models import Question


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    classes = models.ManyToManyField(Class ,related_name="teacher_classes")
    bootcamps = models.ManyToManyField(Bootcamp ,related_name="teacher_bootcamps")

    def __str__(self) -> str:  
        return self.email
    
class Student(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    classes = models.ManyToManyField(Class ,related_name="student_classes")
    bootcamps = models.ManyToManyField(Bootcamp ,related_name="student_bootcamps")

    def __str__(self) -> str:  
        return self.email

class Student_answer(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE ,related_name="student")
    question = models.ForeignKey(Question , on_delete=models.CASCADE ,related_name="question")
    answer = models.TextField()
    true_percentange = models.IntegerField()
    def __str__(self) -> str:
        return f"{self.student}, {self.question}, {self.answer}"

