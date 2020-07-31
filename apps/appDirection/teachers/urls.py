from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.appDirection.teachers.views import TeacherCreate, TeacherList, TeacherUpdate, TeacherDelete, TeacherShow, search, TeacherReport
from .views import importar 

teacherpatterns = ([
    path('new/', login_required(TeacherCreate.as_view()), name='teacher_create'),
    path('list/', login_required(TeacherList.as_view()), name='teacher_list'),
    path('update/<int:pk>/', login_required(TeacherUpdate.as_view()), name='teacher_update'),
    path('delete/<int:pk>/', login_required(TeacherDelete.as_view()), name='teacher_delete'),
    path('show/<int:pk>/', login_required(TeacherShow.as_view()), name='teacher_show'),
    path('search/', login_required(search), name='teacher_search'),
    path('report/', login_required(TeacherReport.as_view()), name='report'),
    path('import/', login_required(importar), name='teacher_import')
], 'teachers')