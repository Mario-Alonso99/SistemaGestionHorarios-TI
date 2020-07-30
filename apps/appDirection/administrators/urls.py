from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.appDirection.administrators.views import AdministratorCreate, AdministratorList, AdministratorUpdate, AdministratorDelete, AdministratorShow, search, AdministratorReport


administratorpatterns = ([
    path('new/', login_required(AdministratorCreate.as_view()), name='administrator_create'),
    path('list/', login_required(AdministratorList.as_view()), name='administrator_list'),
    path('update/<int:pk>/', login_required(AdministratorUpdate.as_view()), name='administrator_update'),
    path('delete/<int:pk>/', login_required(AdministratorDelete.as_view()), name='administrator_delete'),
    path('show/<int:pk>/', login_required(AdministratorShow.as_view()), name='administrator_show'),
    path('search/', login_required(search), name='administrator_search'),
    path('report/', login_required(AdministratorReport.as_view()), name='report'),
    
], 'administrators')
