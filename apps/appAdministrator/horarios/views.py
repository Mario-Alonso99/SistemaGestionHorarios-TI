from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Importamos el Módelo de la Aplicación Students (models.py)
from apps.appAdministrator.horarios.models import Cabecera, Contenido

#Importamos el Formulario de la Aplicación Students para el registro y actualización (forms.py)
from apps.appAdministrator.horarios.forms import HorarioFormHead, HorarioFormBody1, HorarioFormBody2, HorarioFormBody3

# Create your views here.

#Clase de Creación de Registro
class HorarioCreate(CreateView):
    model = Contenido
    template_name = 'horarios/registrar.html'
    form_class = HorarioFormHead
    second_form_class = HorarioFormBody1
    third_form_class = HorarioFormBody2
    four_form_class = HorarioFormBody3
    success_url = reverse_lazy('horarios:horario_list')

    def get_context_data(self, **kwargs):
        context = super(HorarioCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(self.request.GET)
        if 'form4' not in context:
            context['form4'] = self.four_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form3 = self.third_form_class(request.POST)
        form4 = self.four_form_class(request.POST)
        
        if form.is_valid and form2.is_valid and form3.is_valid and form4.is_valid():
            contenido = form2.save()
            contenido.cabecera1 = form.save()
            contenido.save()

            contenido2 = form3.save()
            contenido2.cabecera2 = form.save()
            contenido2.save()

            contenido3 = form4.save()
            contenido3.cabecera3 = form.save()
            contenido3.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4))

#Clase de Listado de Registros
class HorarioList(ListView):
    queryset = Cabecera.objects.order_by('especialidad', 'cuatrimestre', 'grupo')
    template_name = 'horarios/horario_list.html'
    paginate_by = 30

#Clase de Detalles de Registros
class HorarioShow(DetailView):
    model = Cabecera
    second_model = Contenido
    template_name = 'horarios/horario_show.html'
    form_class = HorarioFormHead
    second_form_class = HorarioFormBody1
    third_form_class = HorarioFormBody2
    four_form_class = HorarioFormBody3
    success_url = reverse_lazy('horarios:horario_list')

    def get_context_data(self, **kwargs):
        context = super(HorarioShow, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        cabecera = self.model.objects.get(id=pk)
        contenido = self.second_model.objects.get(cabecera1=cabecera.id)
        contenido2 = self.second_model.objects.get(cabecera2=cabecera.id)
        contenido3 = self.second_model.objects.get(cabecera3=cabecera.id)

        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=contenido)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(instance=contenido2)
        if 'form4' not in context:
            context['form4'] = self.four_form_class(instance=contenido3)
        return context




class HorarioUpdate(UpdateView):
    model = Cabecera
    second_model = Contenido
    template_name = 'horarios/registrar.html'
    form_class = HorarioFormHead
    second_form_class = HorarioFormBody1
    third_form_class = HorarioFormBody2
    four_form_class = HorarioFormBody3
    success_url = reverse_lazy('horarios:horario_list')

    def get_context_data(self, **kwargs):
        context = super(HorarioUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        cabecera = self.model.objects.get(id=pk)
        contenido = self.second_model.objects.get(cabecera1=cabecera.id)
        contenido2 = self.second_model.objects.get(cabecera2=cabecera.id)
        contenido3 = self.second_model.objects.get(cabecera3=cabecera.id)

        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=contenido)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(instance=contenido2)
        if 'form4' not in context:
            context['form4'] = self.four_form_class(instance=contenido3)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
		
        pk = kwargs['pk']
        cabecera = self.model.objects.get(id=pk)
        contenido = self.second_model.objects.get(cabecera1=cabecera.id)
        contenido2 = self.second_model.objects.get(cabecera2=cabecera.id)
        contenido3 = self.second_model.objects.get(cabecera3=cabecera.id)

        form = self.form_class(request.POST, instance=cabecera)
        form2 = self.second_form_class(request.POST, instance=contenido)
        form3 = self.third_form_class(request.POST, instance=contenido2)
        form4 = self.four_form_class(request.POST, instance=contenido3)
        
        if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            form.save()
            form2.save()
            form3.save()
            form4.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class HorarioDelete(DeleteView):
	model = Cabecera
	template_name = 'horarios/horario_delete.html'
	success_url = reverse_lazy('horarios:horario_list')