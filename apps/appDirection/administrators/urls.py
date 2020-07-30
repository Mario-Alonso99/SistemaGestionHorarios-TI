from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.appDirection.administrators.views import AdministratorCreate, AdministratorList, AdministratorUpdate, AdministratorDelete, AdministratorShow, search, AdministratorReport


administratorpatterns = ([
    path('new/', AdministratorCreate.as_view(), name='administrator_create'),
    path('list/', AdministratorList.as_view(), name='administrator_list'),
    path('update/<int:pk>/', AdministratorUpdate.as_view(), name='administrator_update'),
    path('delete/<int:pk>/', AdministratorDelete.as_view(), name='administrator_delete'),
    path('show/<int:pk>/', AdministratorShow.as_view(), name='administrator_show'),
    path('search/', search, name='administrator_search'),
    path('report/', AdministratorReport.as_view(), name='report'),
    
], 'administrators')
