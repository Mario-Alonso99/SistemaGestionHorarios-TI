from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

#Importamos el Módelo de la Aplicación Students (models.py)
from apps.appAdministrator.horarios.models import Cabecera, Contenido

#Importamos el Formulario de la Aplicación Students para el registro y actualización (forms.py)
from apps.appAdministrator.horarios.forms import HorarioFormHead, HorarioFormBody

# Create your views here.

#Clase de Creación de Registro
class HorarioCreate(CreateView):
    model = Contenido
    template_name = 'horarios/registrar.html'
    form_class = HorarioFormBody
    second_form_class = HorarioFormHead
    success_url = reverse_lazy('horarios:horario_list')

    def get_context_data(self, **kwargs):
        context = super(HorarioCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        
        if form.is_valid and form2.is_valid():
            contenido = form.save(commit=False)
            contenido.cabecera = form2.save()
            contenido.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))