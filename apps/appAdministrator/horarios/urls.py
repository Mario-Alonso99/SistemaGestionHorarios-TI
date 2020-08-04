from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.appAdministrator.horarios.views import HorarioCreate

horariospatterns = ([
    path('new/', HorarioCreate.as_view(), name='horario_create'),

], 'horarios')