from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from clubs_app.models import ClubModel
from .forms import ChangeClubData


def check_user_club(request, slug_club):
    if request.user == ClubModel.objects.get(slug_club=slug_club).manager:
        return True


@login_required
def index(request, slug_club):
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

            form_change_club_data.save()
            return redirect('dashboard:profile')
    else:
        form_change_club_data = ChangeClubData(initial=initial_data)

    context = {
        'form': form_change_club_data,
    }

    if check_user_club(request, slug_club):
        return render(request, template_name='dashboard_app/index.html', context=context)
    else:
        return redirect('clubs_app:profile')
