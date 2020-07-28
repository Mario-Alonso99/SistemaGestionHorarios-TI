from django.urls import path

#Importamos el decorar que nos ayuda a establecer un Login Requerido para acceder a las Urls
from django.contrib.auth.decorators import login_required

#Importamos las vistas que fueron creadas (views.py)
from apps.appDirection.students.views import StudentCreate, StudentList, StudentUpdate, StudentDelete, StudentShow, search, StudentReport

#Importamos la vista de importar (views.py)
from .views import importar

studentpatterns = ([
    path('new/', login_required (StudentCreate.as_view()), name='student_create'),
    path('list/', login_required (StudentList.as_view()), name='student_list'),
    path('update/<int:pk>/', login_required (StudentUpdate.as_view()), name='student_update'),
    path('delete/<int:pk>/', login_required (StudentDelete.as_view()), name='student_delete'),
    path('show/<int:pk>/', login_required (StudentShow.as_view()), name='student_show'),
    path('search/', login_required (search), name='student_search'),
    path('report/', login_required (StudentReport.as_view()), name='report'),
    path('import/', login_required (importar), name="student_import"),

], 'students')