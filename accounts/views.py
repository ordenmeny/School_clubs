from django.views.generic import CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('clubs_app:home_page')


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'

