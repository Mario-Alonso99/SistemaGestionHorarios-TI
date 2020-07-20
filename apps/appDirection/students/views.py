from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy

from apps.appDirection.students.models import Student
from apps.appDirection.students.forms import StudentForm

# Create your views here.
class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_formCreate.html'
    success_url = reverse_lazy('students:student_list')

class StudentList(ListView):
    queryset = Student.objects.order_by('especialidad', 'cuatrimestre', 'grupo')
    template_name = 'students/students_list.html'
    paginate_by = 30

class StudentUpdate(UpdateView):
	model = Student
	form_class = StudentForm
	template_name = 'students/student_formCreate.html'
	success_url = reverse_lazy('students:student_list')

class StudentDelete(DeleteView):
	model = Student
	template_name = 'students/student_delete.html'
	success_url = reverse_lazy('students:student_list')