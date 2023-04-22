from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *


class HomePage(TemplateView):
    template_name = 'clubs_app/index.html'


@login_required
def create_club(request):
    if request.method == 'POST':
        form = FormClubModel(request.POST)
        if form.is_valid():
            form.instance.manager = request.user
            form.save()
            messages.success(request, 'Клуб создан')
            return redirect('clubs_app:home_page')
    else:
        form = FormClubModel()

    context = {
        'form': form,
    }
    return render(request, template_name='clubs_app/create_club.html', context=context)
