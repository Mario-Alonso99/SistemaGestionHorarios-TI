from django.urls import path
from apps.appDirection.places.views import PlaceCreate, PlaceList, PlaceUpdate, PlaceDelete, PlaceShow, search, PlaceReport

placepatterns = ([
    path('new/', PlaceCreate.as_view(), name='place_create'),
    path('list/', PlaceList.as_view(), name='place_list'),
    path('update/<int:pk>/', PlaceUpdate.as_view(), name='place_update'),
    path('delete/<int:pk>/', PlaceDelete.as_view(), name='place_delete'),
    path('show/<int:pk>/', PlaceShow.as_view(), name='place_show'),
    path('search/', search, name='place_search'),
    path('report/', PlaceReport.as_view(), name='report'),
], 'places')