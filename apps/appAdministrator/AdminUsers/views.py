from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .forms import FormLogin

# Create your views here.

class LoginAdmin(FormView):
    template_name = 'loginAdministrador/login.html'
    form_class = FormLogin
    success_url = reverse_lazy('horarios:horario_list')

    @method_decorator(csrf_protect)

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginAdmin,self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request,form.get_user())
        return super(LoginAdmin,self).form_valid(form)

def logoutUserAdmin(request):
    logout(request)
    return HttpResponseRedirect('/administrador/login/')