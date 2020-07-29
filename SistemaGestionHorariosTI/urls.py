"""SistemaGestionHorariosTI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Importación de Recursos del Administrador
from django.contrib import admin
from django.urls import path, include






#Importación de los recursos de las Apps (Urls)
from apps.appDirection.students.urls import studentpatterns
from apps.appDirection.places.urls import placepatterns
from apps.appDirection.teachers.urls import teacherpatterns
from apps.appDirection.asignaturas.urls import asignaturapatterns






#Importación de los Recrusos para Login
from apps.appDirection.users.views import Login, logoutUser
from django.contrib.auth.decorators import login_required







#Patters de las Urls
urlpatterns = [
    #Patterns de las Apps
    path('admin/', admin.site.urls),
    path('students/', include (studentpatterns)),
    path('places/', include (placepatterns)),
    path('teachers/', include (teacherpatterns)),
    path('asignaturas/', include (asignaturapatterns)),











    #Patterns de los Inicio de Sesión
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout/',login_required(logoutUser), name='logout'),
]