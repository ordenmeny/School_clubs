from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from pytils.translit import slugify
from django.db.models import Q


# @login_required
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
            form.instance.slug_club = slugify(form.instance.title_club)
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
def list_club(request, cat_slug):
    if cat_slug == 'all_clubs':
        club_model = ClubModel.objects.all()
    else:
        club_model = ClubModel.objects.filter(cat_club=CatClubModel.objects.get(slug=cat_slug))
    context = {
        'club_model': club_model,
    }
    return render(request, template_name='clubs_app/list_club.html', context=context)


def join_club(request, club_id):
    club = ClubModel.objects.get(pk=club_id)  # получить экземпляр класса
    club.member.add(request.user.id)

    messages.success(request, f'Вы вступили в клуб {club.title_club}')
    return redirect('clubs_app:home_page')


@login_required
def my_clubs(request):
    # нужно сделать вывод всех клубов, в которых user принимает участие: manager или member
    # club_model = ClubModel.objects.filter(manager=request.user)

    club_model = set(ClubModel.objects.filter(Q(manager=request.user) | Q(member=request.user)))
    context = {
        'club_model': club_model,
        'my_clubs': True,
        # 'my_clubs': ('manager' if ClubModel.manager == request.user else 'member')
    }

    return render(request, template_name='clubs_app/list_club.html', context=context)


def show_articles(request, slug_club):
    articles = ArticleClubModel.objects.filter(club_contains=ClubModel.objects.get(slug_club=slug_club))

    context = {
        'slug_club': slug_club,
        'articles': articles,
    }
    return render(request, template_name='clubs_app/show_articles.html', context=context)
