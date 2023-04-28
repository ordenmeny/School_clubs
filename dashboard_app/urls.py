from django.urls import path, include
from .views import index, members

app_name = 'dashboard_app'
urlpatterns = [
    path('<slug:slug_club>/profile/', index, name='profile'),
    path('<slug:slug_club>/members/', members, name='members'),

]
