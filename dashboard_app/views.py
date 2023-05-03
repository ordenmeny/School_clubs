from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ChangeClubData, ArticleClubForm, MessageAddForm
from django.contrib import messages
from clubs_app.models import ArticleClubModel, ClubModel, MessageClub
from pytils.translit import slugify
from datetime import date


def check_user_club(request, slug_club):
    if not (request.user == ClubModel.objects.get(slug_club=slug_club).manager):
        return redirect('clubs_app:home_page')
    else:
        return False


@login_required
def members(request, slug_club):
    if check_user_club(request, slug_club):
        messages.success(request, 'Доступ закрыт')
        return check_user_club(request, slug_club)

    club = ClubModel.objects.get(slug_club=slug_club)
    context = {
        'members': club.member.all(),
        'slug_club': slug_club,
        'club_name': club.title_club,
    }
    return render(request, template_name='dashboard_app/members.html', context=context)


@login_required
def index(request, slug_club):
    if check_user_club(request, slug_club):
        messages.success(request, 'Доступ закрыт')
        return check_user_club(request, slug_club)

    club = ClubModel.objects.get(slug_club=slug_club)

    initial_data = {
        'title_club': club.title_club,
        'cat_club': club.cat_club,
        'info_club': club.info_club,
        'days_event': club.days_event,
        'time_event': club.time_event,
        'price_club': club.price_club,
    }

    if request.method == 'POST':
        form_change_club_data = ChangeClubData(request.POST, initial=initial_data)

        if form_change_club_data.is_valid():
            club.title_club = form_change_club_data.instance.title_club
            club.cat_club = form_change_club_data.instance.cat_club
            club.info_club = form_change_club_data.instance.info_club
            club.days_event = form_change_club_data.instance.days_event
            club.time_event = form_change_club_data.instance.time_event
            club.price_club = form_change_club_data.instance.price_club

            club.save()
            return redirect('dashboard_app:profile', slug_club=slug_club)
    else:
        form_change_club_data = ChangeClubData(initial=initial_data)

    context = {
        'form': form_change_club_data,
        'slug_club': slug_club,
        'club_name': club.title_club,

    }

    return render(request, template_name='dashboard_app/index.html', context=context)


@login_required
def delete_member(request, slug_club, id_member):
    if check_user_club(request, slug_club):
        messages.success(request, 'Доступ закрыт')
        return check_user_club(request, slug_club)
    club = ClubModel.objects.get(slug_club=slug_club)
    member_club = club.member.get(id=id_member)

    club.member.remove(member_club)

    return redirect('dashboard_app:members', slug_club=slug_club)


def content(request):
    pass


@login_required
def add_article(request, slug_club):
    if check_user_club(request, slug_club):
        messages.success(request, 'Доступ закрыт')
        return check_user_club(request, slug_club)

    if request.method == 'POST':
        form_title = ArticleClubForm(request.POST, request.FILES)
        if form_title.is_valid():
            model_article = ArticleClubModel.objects.create(
                title_article=form_title.instance.title_article,
                slug_article=slugify(form_title.instance.title_article),
                author_user=request.user,
                club_contains=ClubModel.objects.get(slug_club=slug_club),
                text_body=form_title.instance.text_body,
                image=form_title.instance.image,
            )
            model_article.save()
            messages.success(request, 'Статья добавлена')
            return redirect('dashboard_app:add_article', slug_club=slug_club)

        else:
            form_title = ArticleClubForm()
            messages.success(request, 'Ошибка')
            redirect('dashboard_app:add_article', slug_club=slug_club)
    else:
        form_title = ArticleClubForm()

    context = {
        'slug_club': slug_club,
        'form_ck': form_title,
        'club_name': ClubModel.objects.get(slug_club=slug_club).title_club,
    }
    return render(request, template_name='dashboard_app/add_article.html', context=context)


@login_required
def message(request, slug_club):
    if check_user_club(request, slug_club):
        messages.success(request, 'Доступ закрыт')
        return check_user_club(request, slug_club)
    if request.method == 'POST':
        form_msg = MessageAddForm(request.POST)

        if form_msg.is_valid():
            model_msg = MessageClub.objects.create(
                sender=request.user,
                sender_club=ClubModel.objects.get(slug_club=slug_club),
                slug_msg=slugify(f'{form_msg.instance.title_msg}{date.today()}'),
                title_msg=form_msg.instance.title_msg,
                body_msg=form_msg.instance.body_msg,
            )
            model_msg.save()
            messages.success(request, 'Сообщение отправлено')
            return redirect('dashboard_app:message', slug_club=slug_club)
        else:
            form_msg = MessageAddForm()
            messages.success(request, 'Ошибка')
            return redirect('dashboard_app:message', slug_club=slug_club)
    else:
        form_msg = MessageAddForm()

    context = {
        'slug_club': slug_club,
        'form_msg': form_msg,
        'club_name': ClubModel.objects.get(slug_club=slug_club).title_club,
    }
    return render(request, template_name='dashboard_app/add_msg.html', context=context)
