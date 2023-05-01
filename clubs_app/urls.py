from django.urls import path
from .views import *

app_name = 'clubs_app'

urlpatterns = [
    path('', index, name='home_page'),
    path('create_club/', create_club, name='create_club'),
    path('list_club/<slug:cat_slug>', list_club, name='list_club'),
    path('join_club/<int:club_id>', join_club, name='join_club'),
    path('my_clubs/', my_clubs, name='my_clubs'),
]
