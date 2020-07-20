from django.urls import path
from apps.appDirection.students.views import StudentCreate, StudentList

studentpatterns = ([
    path('new/', StudentCreate.as_view(), name='student_create'),
    path('list/', StudentList.as_view(), name='student_list'),
], 'students')