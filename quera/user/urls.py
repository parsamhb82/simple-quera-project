from django.urls import path
from user.views import teacher_list, student_list, teacher_detail, student_detail

urlpatterns = [
    path('teacher/', teacher_list),
    path('student/', student_list),
    path('teacher/<str:input_email>/', teacher_detail),
    path('student/<str:input_email>/', student_detail),
]