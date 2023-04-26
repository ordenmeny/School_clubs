from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from clubs_app.models import ClubModel


def check_user_club(request, slug_club):
    if request.user == ClubModel.objects.get(slug_club=slug_club).manager:
        return True


@login_required
def index(request, slug_club):
    if check_user_club(request, slug_club):
        return render(request, template_name='dashboard_app/index.html')
    else:
        return redirect('clubs_app:home_page')

