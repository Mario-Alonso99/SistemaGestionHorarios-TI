from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.appDirection.teachers.views import TeacherCreate, TeacherList, TeacherUpdate, TeacherDelete, TeacherShow, search, TeacherReport
from .views import importar 

teacherpatterns = ([
    path('new/', TeacherCreate.as_view(), name='teacher_create'),
    path('list/', TeacherList.as_view(), name='teacher_list'),
    path('update/<int:pk>/', TeacherUpdate.as_view(), name='teacher_update'),
    path('delete/<int:pk>/', TeacherDelete.as_view(), name='teacher_delete'),
    path('show/<int:pk>/', TeacherShow.as_view(), name='teacher_show'),
    path('search/', search, name='teacher_search'),
    path('report/', TeacherReport.as_view(), name='report'),
    path('import/', importar, name="teacher_import")
], 'teachers')