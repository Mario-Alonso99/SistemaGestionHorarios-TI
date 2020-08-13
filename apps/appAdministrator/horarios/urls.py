from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.appAdministrator.horarios.views import HorarioCreate, HorarioList, HorarioUpdate, HorarioDelete, search, HorarioShow

horariospatterns = ([
    path('new/', login_required(HorarioCreate.as_view()), name='horario_create'),
    path('list/', login_required(HorarioList.as_view()), name='horario_list'),
    path('update/<int:pk>/', login_required(HorarioUpdate.as_view()), name='horario_update'),
    path('delete/<int:pk>/', login_required(HorarioDelete.as_view()), name='horario_delete'),
    path('show/<int:pk>/', login_required (HorarioShow.as_view()), name='horario_show'),
    path('search/', login_required(search), name='horario_search'),
], 'horarios')