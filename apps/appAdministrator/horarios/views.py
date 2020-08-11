from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Importamos el Módelo de la Aplicación Students (models.py)
from apps.appAdministrator.horarios.models import Cabecera, Contenido, SecondContenido, ThirdContenido

#Importamos el Formulario de la Aplicación Students para el registro y actualización (forms.py)
from apps.appAdministrator.horarios.forms import HorarioFormHead, HorarioFormBody1, HorarioFormBody2, HorarioFormBody3, HorarioFormBody4, HorarioFormBody5, HorarioFormBody6, HorarioFormBody7, HorarioFormBody8, HorarioFormBody9

#Importamos el filtro de la Aplicación Horarios (filters.py)
from apps.appAdministrator.horarios.filters import HorarioFilter

# Create your views here.

#Clase de Creación de Registros
class HorarioCreate(CreateView):
    model = Contenido
    template_name = 'horarios/registrar.html'

    form_class = HorarioFormHead

    second_form_class = HorarioFormBody1
    third_form_class = HorarioFormBody2
    four_form_class = HorarioFormBody3

    five_form_class = HorarioFormBody4
    six_form_class = HorarioFormBody5
    seven_form_class = HorarioFormBody6
    
    eight_form_class = HorarioFormBody7
    nine_form_class = HorarioFormBody8
    ten_form_class = HorarioFormBody9

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

        
        if 'form5' not in context:
            context['form5'] = self.five_form_class(self.request.GET)
        if 'form6' not in context:
            context['form6'] = self.six_form_class(self.request.GET)
        if 'form7' not in context:
            context['form7'] = self.seven_form_class(self.request.GET)

        
        if 'form8' not in context:
            context['form8'] = self.eight_form_class(self.request.GET)
        if 'form9' not in context:
            context['form9'] = self.nine_form_class(self.request.GET)
        if 'form10' not in context:
            context['form10'] = self.ten_form_class(self.request.GET)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)

        form2 = self.second_form_class(request.POST)
        form3 = self.third_form_class(request.POST)
        form4 = self.four_form_class(request.POST)

        form5 = self.five_form_class(request.POST)
        form6 = self.six_form_class(request.POST)
        form7 = self.seven_form_class(request.POST)

        form8 = self.eight_form_class(request.POST)
        form9 = self.nine_form_class(request.POST)
        form10 = self.ten_form_class(request.POST)
        
        if form.is_valid and form2.is_valid and form3.is_valid and form4.is_valid and form5.is_valid and form6.is_valid and form7.is_valid and form8.is_valid and form9.is_valid and form10.is_valid():
            contenido = form2.save()
            contenido.cabecera1 = form.save()
            contenido.save()

            contenido2 = form3.save()
            contenido2.cabecera2 = form.save()
            contenido2.save()

            contenido3 = form4.save()
            contenido3.cabecera3 = form.save()
            contenido3.save()


            contenido4 = form5.save()
            contenido4.cabecera4 = form.save()
            contenido4.save()

            contenido5 = form6.save()
            contenido5.cabecera5 = form.save()
            contenido5.save()

            contenido6 = form7.save()
            contenido6.cabecera6 = form.save()
            contenido6.save()


            contenido7 = form8.save()
            contenido7.cabecera7 = form.save()
            contenido7.save()

            contenido8 = form9.save()
            contenido8.cabecera8 = form.save()
            contenido8.save()

            contenido9 = form10.save()
            contenido9.cabecera9 = form.save()
            contenido9.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, form7=form7, form8=form8, form9=form9, form10=form10))

#Clase de Listado de Registros
class HorarioList(ListView):
    queryset = Cabecera.objects.order_by('especialidad', 'cuatrimestre', 'grupo')
    template_name = 'horarios/horario_list.html'
    paginate_by = 5

#Clase de Actualización de Registros
class HorarioUpdate(UpdateView):
    model = Cabecera
    second_model = Contenido
    third_model = SecondContenido
    four_model = ThirdContenido
    
    template_name = 'horarios/registrar.html'
    
    form_class = HorarioFormHead
    second_form_class = HorarioFormBody1
    third_form_class = HorarioFormBody2
    four_form_class = HorarioFormBody3

    five_form_class = HorarioFormBody4
    six_form_class = HorarioFormBody5
    seven_form_class = HorarioFormBody6
    
    eight_form_class = HorarioFormBody7
    nine_form_class = HorarioFormBody8
    ten_form_class = HorarioFormBody9

    success_url = reverse_lazy('horarios:horario_list')

    def get_context_data(self, **kwargs):
        context = super(HorarioUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        cabecera = self.model.objects.get(id=pk)
        
        contenido = self.second_model.objects.get(cabecera1=cabecera.id)
        contenido2 = self.second_model.objects.get(cabecera2=cabecera.id)
        contenido3 = self.second_model.objects.get(cabecera3=cabecera.id)

        contenido4 = self.third_model.objects.get(cabecera4=cabecera.id)
        contenido5 = self.third_model.objects.get(cabecera5=cabecera.id)
        contenido6 = self.third_model.objects.get(cabecera6=cabecera.id)

        contenido7 = self.four_model.objects.get(cabecera7=cabecera.id)
        contenido8 = self.four_model.objects.get(cabecera8=cabecera.id)
        contenido9 = self.four_model.objects.get(cabecera9=cabecera.id)

        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=contenido)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(instance=contenido2)
        if 'form4' not in context:
            context['form4'] = self.four_form_class(instance=contenido3)


        if 'form5' not in context:
            context['form5'] = self.five_form_class(instance=contenido4)
        if 'form6' not in context:
            context['form6'] = self.six_form_class(instance=contenido5)
        if 'form7' not in context:
            context['form7'] = self.seven_form_class(instance=contenido6)


        if 'form8' not in context:
            context['form8'] = self.eight_form_class(instance=contenido7)
        if 'form9' not in context:
            context['form9'] = self.nine_form_class(instance=contenido8)
        if 'form10' not in context:
            context['form10'] = self.ten_form_class(instance=contenido9)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
		
        pk = kwargs['pk']
        cabecera = self.model.objects.get(id=pk)

        contenido = self.second_model.objects.get(cabecera1=cabecera.id)
        contenido2 = self.second_model.objects.get(cabecera2=cabecera.id)
        contenido3 = self.second_model.objects.get(cabecera3=cabecera.id)

        contenido4 = self.third_model.objects.get(cabecera4=cabecera.id)
        contenido5 = self.third_model.objects.get(cabecera5=cabecera.id)
        contenido6 = self.third_model.objects.get(cabecera6=cabecera.id)

        contenido7 = self.four_model.objects.get(cabecera7=cabecera.id)
        contenido8 = self.four_model.objects.get(cabecera8=cabecera.id)
        contenido9 = self.four_model.objects.get(cabecera9=cabecera.id)

        form = self.form_class(request.POST, instance=cabecera)

        form2 = self.second_form_class(request.POST, instance=contenido)
        form3 = self.third_form_class(request.POST, instance=contenido2)
        form4 = self.four_form_class(request.POST, instance=contenido3)

        form5 = self.five_form_class(request.POST, instance=contenido4)
        form6 = self.six_form_class(request.POST, instance=contenido5)
        form7 = self.seven_form_class(request.POST, instance=contenido6)

        form8 = self.eight_form_class(request.POST, instance=contenido7)
        form9 = self.nine_form_class(request.POST, instance=contenido8)
        form10 = self.ten_form_class(request.POST, instance=contenido9)
        
        if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid() and form7.is_valid() and form8.is_valid() and form9.is_valid() and form10.is_valid():
            form.save()

            form2.save()
            form3.save()
            form4.save()

            form5.save()
            form6.save()
            form7.save()

            form8.save()
            form9.save()
            form10.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

#Clase de Eliminación de Registros
class HorarioDelete(DeleteView):
	model = Cabecera
	template_name = 'horarios/horario_delete.html'
	success_url = reverse_lazy('horarios:horario_list')

#Clase de Busqueda de Registros
def search(request):
    horario_list = Cabecera.objects.all()
    horario_list = Cabecera.objects.order_by('especialidad', 'cuatrimestre', 'grupo')
    horario_filter = HorarioFilter(request.GET, queryset=horario_list)
    return render(request, 'horarios/horario_search.html', {'filter': horario_filter})