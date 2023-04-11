from django.urls import path
from .views import HomePage, CreateClubView, dashboard_with_pk_view
from . import views

app_name = 'clubs_app'

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('create_club/', CreateClubView.as_view(), name='create_club'),
    path('dashboard/<int:pk>/', views.dashboard_with_pk_view, name='dashboard_with_pk'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
