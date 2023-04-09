from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import ClubModel
from .forms import CreateClubForm


class HomePage(TemplateView):
    template_name = 'clubs_app/index.html'


class CreateClubView(CreateView):
    model = ClubModel
    template_name = 'clubs_app/create_club.html'
    form_class = CreateClubForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
