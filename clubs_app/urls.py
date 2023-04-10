from django.urls import path
from .views import HomePage, CreateClubView, DashboardView

app_name = 'clubs_app'

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('create_club/', CreateClubView.as_view(), name='create_club'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
