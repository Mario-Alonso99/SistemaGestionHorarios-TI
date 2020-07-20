from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.appDirection.students.models import Student
from apps.appDirection.students.forms import StudentForm

# Create your views here.
class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_formCreate.html'
    success_url = reverse_lazy('students:student_list')