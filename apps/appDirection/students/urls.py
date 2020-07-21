from django.urls import path
from apps.appDirection.students.views import StudentCreate, StudentList, StudentUpdate, StudentDelete, StudentShow, search

studentpatterns = ([
    path('new/', StudentCreate.as_view(), name='student_create'),
    path('list/', StudentList.as_view(), name='student_list'),
    path('update/<int:pk>/', StudentUpdate.as_view(), name='student_update'),
    path('delete/<int:pk>/', StudentDelete.as_view(), name='student_delete'),
    path('show/<int:pk>/', StudentShow.as_view(), name='student_show'),
    path('search/', search, name='student_search'),
], 'students')