from django.views.generic import CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('clubs_app:home_page')
