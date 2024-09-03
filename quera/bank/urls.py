from django.urls import path
from bank.views import questions_list , lessons_list , add_question, add_lesson, get_lesson, get_question
from bank.views import QuestionListAPIView, QuestionCreateAPIView, LessonListView, LessonCreateAPIView, LessonDetailView, QuestionDetailView
urlpatterns = [
    path('questions/', QuestionListAPIView.as_view()),
    path('lessons/', LessonListView.as_view()),
    path('add-question/', QuestionCreateAPIView.as_view()),
    path('add-lesson/', LessonCreateAPIView.as_view()),
    path('get-lesson/<int:pk>', LessonDetailView.as_view()),
    path('get-question/<int:pk>', QuestionDetailView.as_view())
]