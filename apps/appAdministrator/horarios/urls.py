from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.appAdministrator.horarios.views import HorarioCreate, HorarioList, HorarioShow, HorarioUpdate, HorarioDelete

horariospatterns = ([
    path('new/', HorarioCreate.as_view(), name='horario_create'),
    path('list/', HorarioList.as_view(), name='horario_list'),
    path('show/<int:pk>/', HorarioShow.as_view(), name='horario_show'),
    path('update/<int:pk>/', HorarioUpdate.as_view(), name='horario_update'),
    path('delete/<int:pk>/', HorarioDelete.as_view(), name='horario_delete'),

], 'horarios')