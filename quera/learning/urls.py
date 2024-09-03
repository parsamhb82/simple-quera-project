from django.urls import path
from learning.views import add_assignmet_to_class, add_bootcamp, add_lesson_to_class, bootcamp_list, classes_list, creat_class, get_bootcamp, get_class 
from learning.views import BootcampListView, ClassListView, RetrieveBootcampView, RetrieveClassView, CreatBootcamp, CreatClass
urlpatterns = [
    path('add_assignmet_to_class', add_assignmet_to_class),
    path('add_bootcamp', CreatBootcamp.as_view()),
    path('add_lesson_to_class', add_lesson_to_class),
    path('bootcamp_list', BootcampListView.as_view()),
    path('classes_list', ClassListView.as_view()),
    path('creat_class', CreatClass.as_view()),
    path('get_bootcamp/<int:pk>', RetrieveBootcampView.as_view()),
    path('get_class/<int:pk>', RetrieveClassView.as_view())
]