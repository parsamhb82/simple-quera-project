from django.shortcuts import render
from bank.models import Question , Lesson
from learning.models import Class , Bootcamp
from user.models import Teacher, Student, Student_answer
from django.http import JsonResponse
import json


def questions_list_(request):
    questions = Question.objects.all()
    questions_list = []
    for question in questions:
        questions_list.append({
            "name": question.name,
            "form": question.form,
            "answer": question.answer,
            "publish_date": question.publish_date,
            "level": question.level,
        })
    return JsonResponse(questions_list, safe=False)

def lessons_list_(request):
    lessons = Lesson.objects.all()
    lessons_list = []
    for lesson in lessons:
        lessons_list.append({
            'subject': lesson.subject,
            'text': lesson.text,
        }
        )
    return JsonResponse(lessons_list, safe=False)
def add_question(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question_name = data['name']
        question_form = data['form']
        question_answer = data['answer']
        question_publish_date = data['publish_date']
        question_level = data['level']
        question = Question.objects.create(name = question_name, form = question_form, answer = question_answer, publish_date = question_publish_date, level = question_level)
        question.save()

        return JsonResponse({'message': 'Question added successfully'})
    return JsonResponse({'message': 'Invalid request method'})

def add_lesson(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        lesson_subject = data['subject']
        lesson_text = data['text']
        lesson = Lesson.objects.create(subject = lesson_subject, text = lesson_text)
        lesson.save()
        return JsonResponse({'message': 'Lesson added successfully'})
    return JsonResponse({'message': 'Invalid request method'})
            
