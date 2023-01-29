from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app_market.models import History
from app_users.forms import RegistrationForm
from app_users.models import Profile


class RegistrationView(generic.edit.CreateView):
    template_name = 'app_users/registration_form.html'
    success_url = reverse_lazy('login')
    form_class = RegistrationForm
    
    def form_valid(self, form):
        form = RegistrationForm(self.request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            History.objects.create(user=user)
            return super(RegistrationView, self).form_valid(form)
            

class Login(LoginView):
    template_name = 'app_users/login_form.html'
    success_url = reverse_lazy('main')

class Logout(LogoutView):
    next_page = '/market/main/'
