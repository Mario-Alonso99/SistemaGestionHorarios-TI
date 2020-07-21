from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, TemplateView
from django.urls import reverse_lazy

from apps.appDirection.places.models import Place
from apps.appDirection.places.forms import PlaceForm
from apps.appDirection.places.filters import PlaceFilter

# Create your views here.
class PlaceCreate(CreateView):
    model = Place
    form_class = PlaceForm
    template_name = 'places/place_formCreate.html'
    success_url = reverse_lazy('places:place_list')

class PlaceList(ListView):
    queryset = Place.objects.order_by('tipo', 'ubicacion', 'encargado')
    template_name = 'places/places_list.html'
    paginate_by = 5

class PlaceUpdate(UpdateView):
	model = Place
	form_class = PlaceForm
	template_name = 'places/place_formCreate.html'
	success_url = reverse_lazy('places:place_list')

class PlaceDelete(DeleteView):
	model = Place
	template_name = 'places/place_delete.html'
	success_url = reverse_lazy('places:place_list')

class PlaceShow(DetailView):
    model = Place
    template_name = 'places/place_show.html'

def search(request):
    place_list = Place.objects.all()
    place_filter = PlaceFilter(request.GET, queryset=place_list)
    return render(request, 'places/place_search.html', {'filter': place_filter})