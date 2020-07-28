from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.appDirection.students.views import StudentCreate, StudentList, StudentUpdate, StudentDelete, StudentShow, search, StudentReport, RegistroUsuario
from .views import importar 

studentpatterns = ([
    path('new/', StudentCreate.as_view(), name='student_create'),
    path('list/',StudentList.as_view(), name='student_list'),
    path('update/<int:pk>/', login_required (StudentUpdate.as_view()), name='student_update'),
    path('delete/<int:pk>/', login_required (StudentDelete.as_view()), name='student_delete'),
    path('show/<int:pk>/', login_required (StudentShow.as_view()), name='student_show'),
    path('search/', login_required (search), name='student_search'),
    path('report/', login_required (StudentReport.as_view()), name='report'),
    path('import/', login_required (importar), name="student_import"),

    path('registrar/', login_required (RegistroUsuario.as_view()), name='registrar')
], 'students')