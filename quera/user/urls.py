from django.urls import path
from user.views import TeachersListView, StudentListView, RetrieveStudentView, RetrieveTeacherView, add_teacher_to_class, add_teacher_to_bootcamp, CreatStudentAnswer, add_student_to_bootcamp,add_student_to_class,StudentRegisterationView, TeacherRegistrationView, OwnStudentAnswer
from user.views import Login, Refresh, AddStudentToClass, AddTeacherToClass, AddStudentToBootcamp, AddTeacherToBootcamp, OwnStudentAnswer
urlpatterns = [
    path('teacher/', TeachersListView.as_view()),
    path('student/', StudentListView.as_view()),
    path('teacher/<int:pk>/', RetrieveTeacherView.as_view()),
    path('student/<int:pk>/', RetrieveStudentView.as_view()),
    path('add_student_answer/', CreatStudentAnswer.as_view()),
    path('register_new_student/',StudentRegisterationView.as_view()),
    path('register_new_teacher/',TeacherRegistrationView.as_view()),
    path('student_answer/', OwnStudentAnswer.as_view()),
    path('login/', Login.as_view()),
    path('refresh/', Refresh.as_view()),
    path('add_student_to_class/', AddStudentToClass.as_view()),
    path('add_teacher_to_class/', AddTeacherToClass.as_view()),
    path('add_student_to_bootcamp/', AddStudentToBootcamp.as_view()),
    path('add_teacher_to_bootcamp/', AddTeacherToBootcamp.as_view()),
    path('student_answer/', OwnStudentAnswer.as_view()),
]