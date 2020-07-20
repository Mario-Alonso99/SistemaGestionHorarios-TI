from django.urls import path
from apps.appDirection.students.views import StudentCreate

studentpatterns = ([
    path('new/', StudentCreate.as_view(), name='student_create'),
], 'students')