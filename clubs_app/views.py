from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import *


class HomePage(TemplateView):
    template_name = 'clubs_app/index.html'


def create_club(request):
    form = FormClubModel()
    context = {
        'form': form,
    }
    return render(request, template_name='clubs_app/create_club.html', context=context)
