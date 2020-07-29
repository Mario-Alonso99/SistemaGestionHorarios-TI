from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.appDirection.asignaturas.views import AsignaturaCreate, AsignaturaList, AsignaturaUpdate, AsignaturaDelete, AsignaturaShow, search, AsignaturaReport

asignaturapatterns = ([
    path('new/', login_required (AsignaturaCreate.as_view()), name='asignatura_create'),
    path('list/', login_required (AsignaturaList.as_view()), name='asignatura_list'),
    path('update/<int:pk>/', login_required (AsignaturaUpdate.as_view()), name='asignatura_update'),
    path('delete/<int:pk>/', login_required (AsignaturaDelete.as_view()), name='asignatura_delete'),
    path('show/<int:pk>/', login_required (AsignaturaShow.as_view()), name='asignatura_show'),
    path('search/', login_required (search), name='asignatura_search'),
    path('report/', login_required (AsignaturaReport.as_view()), name='report'),
], 'asignaturas')