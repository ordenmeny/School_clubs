from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from pytils.translit import slugify
from django.db.models import Q
from django.apps import apps


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
        cat = None
    else:
        cm = CatClubModel.objects.get(slug=cat_slug)
        club_model = ClubModel.objects.filter(cat_club=cm)
        cat = cm.cat

    context = {
        'club_model': club_model,
        'if_all_clubs': ('all_clubs' if cat_slug == 'all_clubs' else False),
        'if_category': ('category' if cat_slug not in ('my_clubs', 'all_clubs') else False),
        'cat': cat,
    }
    return render(request, template_name='clubs_app/list_club.html', context=context)


def join_club(request, club_id):
    club = ClubModel.objects.get(pk=club_id)
    club.member.add(request.user.id)

    messages.success(request, f'Вы вступили в клуб {club.title_club}')
    return redirect('clubs_app:home_page')


@login_required
def my_clubs(request):
    club_model = set(ClubModel.objects.filter(Q(manager=request.user) | Q(member=request.user)))
    context = {
        'club_model': club_model,
        'my_clubs': True,
    }

    return render(request, template_name='clubs_app/list_club.html', context=context)


def show_articles(request, slug_club):
    articles = ArticleClubModel.objects.filter(club_contains=ClubModel.objects.get(slug_club=slug_club))

    context = {
        'slug_club': slug_club,
        'articles': articles,
    }
    return render(request, template_name='clubs_app/show_articles.html', context=context)


def detail_articles(request, slug_article):
    article = ArticleClubModel.objects.get(slug_content=slug_article)

    context = {
        'title_article': article.title_article,
        'text_body': article.text_body,
        'author_user': article.author_user.username,
        'image': article.image,
        'slug_club': article.club_contains.slug_club,
    }
    return render(request, template_name='clubs_app/detail_articles.html', context=context)


def show_messages(request, slug_club):
    context = {
        'slug_club': slug_club,
        'messages': MessageClub.objects.filter(club_contains=ClubModel.objects.get(slug_club=slug_club))
    }

    return render(request, template_name='clubs_app/show_messages.html', context=context)
