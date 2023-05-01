from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from clubs_app.models import ClubModel
from .forms import ChangeClubData
from django.contrib import messages
from django.http import HttpResponse


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
    }

    return render(request, template_name='dashboard_app/index.html', context=context)


def delete_member(request, slug_club, id_member):
    club = ClubModel.objects.get(slug_club=slug_club)
    member_club = club.member.get(id=id_member)

    club.member.remove(member_club)

    return redirect('dashboard_app:members', slug_club=slug_club)




