from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from .models import UserProfile

from accounts.forms import SignUpForm


class LoginViewCustom(LoginView):
    template_name ='accounts/login.html'



class SignUp(CreateView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:login')
    form_class = SignUpForm

class ProfileView(ListView):
    template_name = 'accounts/profile.html'
    model = UserProfile
    context_object_name = 'profile'





