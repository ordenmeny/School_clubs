from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *



def index(request):
    clubs_cat = CatClubModel.objects.all()
    context = {
        'clubs_cat': clubs_cat,
    }
    return render(request, template_name='clubs_app/index.html', context=context)


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


@login_required
def list_club(request):
    club_model = ClubModel.objects.all()
    context = {
        'club_model': club_model,
    }
    return render(request, template_name='clubs_app/list_club.html', context=context)


def join_club(request, club_id):
    # №1
    # club = ClubModel.objects.get(pk=club_id)
    # club.member.set([request.user.pk])

    # №2
    club = ClubModel.objects.get(pk=club_id)  # получить экземпляр класса
    club.member.add(request.user.id)

    messages.success(request, f'Вы вступили в клуб {club.title_club}')
    return redirect('clubs_app:home_page')
