from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import ClubModel
from .forms import CreateClubForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class HomePage(TemplateView):
    template_name = 'clubs_app/index.html'


class CreateClubView(LoginRequiredMixin, CreateView):
    model = ClubModel
    template_name = 'clubs_app/create_club.html'
    form_class = CreateClubForm
    success_url = reverse_lazy('clubs_app:home_page')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DashboardView(TemplateView):
    template_name = 'clubs_app/dashboard.html'
