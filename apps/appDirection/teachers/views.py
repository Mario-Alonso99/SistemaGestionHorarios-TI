from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, TemplateView
from django.urls import reverse_lazy

from apps.appDirection.teachers.models import Teacher
from apps.appDirection.teachers.forms import TeacherForm
from apps.appDirection.teachers.filters import TeacherFilter

from openpyxl import Workbook
from django.http.response import HttpResponse
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

from tablib import Dataset
from .resources import TeacherResource
from .models import Teacher

# Create your views here.

class TeacherCreate(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/teacher_formCreate.html'
    success_url = reverse_lazy('teachers:teacher_list')

class TeacherList(ListView):
    queryset = Teacher.objects.order_by('grado_academico', 'tipo')
    template_name = 'teachers/teachers_list.html'
    paginate_by = 5

class TeacherUpdate(UpdateView):
	model = Teacher
	form_class = TeacherForm
	template_name = 'teachers/teacher_formCreate.html'
	success_url = reverse_lazy('teachers:teacher_list')

class TeacherDelete(DeleteView):
	model = Teacher
	template_name = 'teachers/teacher_delete.html'
	success_url = reverse_lazy('teachers:teacher_list')

class TeacherShow(DetailView):
    model = Teacher
    template_name = 'teachers/teacher_show.html'

def search(request):
    teacher_list = Teacher.objects.all()
    teacher_filter = TeacherFilter(request.GET, queryset=teacher_list)
    return render(request, 'teachers/teacher_search.html', {'filter': teacher_filter})

class TeacherReport(TemplateView):
    def get(self, request, *args, **kwargs):
        teachers = Teacher.objects.all()
        teachers = Teacher.objects.order_by('grado_academico','tipo')

        wb = Workbook()
        ws = wb.active
        ws['B1'].alignment = Alignment(horizontal="center", vertical="center")
        ws['B1'].border = Border(left= Side(border_style = "thin"), right = Side(border_style = "thin"), top = Side(border_style="thin"), bottom = Side(border_style="thin"))
        ws['B1'].fill = PatternFill(start_color='66FFCC', end_color='66FFCC', fill_type = "solid")
        ws['B1'].font = Font(name='Arial', size=16, bold= True)
        ws['B1'] = 'Reporte de docentes'
        
        nameHoja = 1
        ws.title = 'Hoja'+str(nameHoja)
        controlatorDatos = 4
        controlatorDatos +=1
        #Combinar Celdas
        ws.merge_cells('B1:F1')
        #Cambiar el Ancho de las Columnas
        ws.column_dimensions['B'].width = 20
        ws.column_dimensions['C'].width = 35
        ws.column_dimensions['D'].width = 40
        ws.column_dimensions['E'].width = 25
        ws.column_dimensions['F'].width = 40


        #Modificar el tamaño de las filas
        ws.row_dimensions[1].height = 25
        
        ws['B3'].alignment = Alignment(horizontal="center", vertical="center")
        ws['B3'].border = Border(left= Side(border_style = "thin"), right = Side(border_style = "thin"), top = Side(border_style="thin"), bottom = Side(border_style="thin"))
        ws['B3'].font = Font(name='Arial', size=14, bold= True)
        ws['B3']= 'Matrícula'
        
        ws['C3'].alignment = Alignment(horizontal="center", vertical="center")
        ws['C3'].border = Border(left= Side(border_style = "thin"), right = Side(border_style = "thin"), top = Side(border_style="thin"), bottom = Side(border_style="thin"))
        ws['C3'].font = Font(name='Arial', size=14, bold= True)
        ws['C3']= 'Nombre'
        
        ws['D3'].alignment = Alignment(horizontal="center", vertical="center")
        ws['D3'].border = Border(left= Side(border_style = "thin"), right = Side(border_style = "thin"), top = Side(border_style="thin"), bottom = Side(border_style="thin"))
        ws['D3'].font = Font(name='Arial', size=14, bold= True)
        ws['D3']= 'Grado academico'

        ws['E3'].alignment = Alignment(horizontal="center", vertical="center")
        ws['E3'].border = Border(left= Side(border_style = "thin"), right = Side(border_style = "thin"), top = Side(border_style="thin"), bottom = Side(border_style="thin"))
        ws['E3'].font = Font(name='Arial', size=14, bold= True)
        ws['E3']= 'Tipo'

        ws['F3'].alignment = Alignment(horizontal="center", vertical="center")
        ws['F3'].border = Border(left= Side(border_style = "thin"), right = Side(border_style = "thin"), top = Side(border_style="thin"), bottom = Side(border_style="thin"))
        ws['F3'].font = Font(name='Arial', size=14, bold= True)
        ws['F3']= 'Número de profesor'



        #Diseño de resultados en el reporte y consulta de datos
        cont = 4
        for teacher in teachers:
            ws.cell(row = cont, column = 2).value = teacher.matricula
            ws.cell(row = cont, column = 2).alignment = Alignment(horizontal="center", vertical="center")
            ws.cell(row = cont, column = 2).font = Font(name='Arial', size=10)


            ws.cell(row = cont, column = 3).value = teacher.nombre
            ws.cell(row = cont, column = 3).font = Font(name='Arial', size=10)

            ws.cell(row = cont, column = 4).value = teacher.grado_academico
            ws.cell(row = cont, column = 4).font = Font(name='Arial', size=10)


            ws.cell(row = cont, column = 5).value = teacher.tipo
            ws.cell(row = cont, column = 5).font = Font(name='Arial', size=10)

            ws.cell(row = cont, column = 6).value = teacher.numero_empleado
            ws.cell(row = cont, column = 6).alignment = Alignment(horizontal="center", vertical="center")
            ws.cell(row = cont, column = 6).font = Font(name='Arial', size=10)

            cont +=1

        name_archivo = "ReporteDocentes.xlsx"
        response = HttpResponse(content_type = "application/ms-excel")
        content = "attachment; filename = {0}".format(name_archivo)
        response['Content-Disposition'] = content
        wb.save(response)
        return response

#Agregando codigo para la carga masiva
def importar(request):  
    if request.method == 'POST':  
        teacher_resource = TeacherResource()  
        dataset = Dataset()  
        #print(dataset)  
        new_teachers = request.FILES['xlsfile']  
        #print(new_teachers)  
        imported_data = dataset.load(new_teachers.read())  
        #print(dataset)  
        result = teacher_resource.import_data(dataset, dry_run=True) # Test the data import  
        #print(result.has_errors())  
        if not result.has_errors():  
            teacher_resource.import_data(dataset, dry_run=False) # Actually import now
            return redirect(reverse_lazy('teachers:teacher_list'))
    return render(request, 'teachers/teacher_import.html')