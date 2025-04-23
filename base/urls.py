from django.urls import path
from base import views

urlpatterns=[
    path('students',views.students,name='students'),
    path('students/<int:pk>',views.student,name='student'),


    

]