from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.appDirection.places.views import PlaceCreate, PlaceList, PlaceUpdate, PlaceDelete, PlaceShow, search, PlaceReport

placepatterns = ([
    path('new/', login_required (PlaceCreate.as_view()), name='place_create'),
    path('list/', login_required (PlaceList.as_view()), name='place_list'),
    path('update/<int:pk>/', login_required (PlaceUpdate.as_view()), name='place_update'),
    path('delete/<int:pk>/', login_required (PlaceDelete.as_view()), name='place_delete'),
    path('show/<int:pk>/', login_required (PlaceShow.as_view()), name='place_show'),
    path('search/', login_required (search), name='place_search'),
    path('report/', login_required (PlaceReport.as_view()), name='report'),
], 'places')