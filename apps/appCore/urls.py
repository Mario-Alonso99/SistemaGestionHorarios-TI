from django.urls import path
from .views import HomePageView

corepatterns = [
    path('', HomePageView.as_view(), name="home"),
]