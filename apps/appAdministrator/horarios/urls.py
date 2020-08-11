from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.appAdministrator.horarios.views import HorarioCreate, HorarioList, HorarioUpdate, HorarioDelete, search

horariospatterns = ([
    path('new/', HorarioCreate.as_view(), name='horario_create'),
    path('list/', HorarioList.as_view(), name='horario_list'),
    path('update/<int:pk>/', HorarioUpdate.as_view(), name='horario_update'),
    path('delete/<int:pk>/', HorarioDelete.as_view(), name='horario_delete'),
    
    path('search/', search, name='horario_search'),
], 'horarios')