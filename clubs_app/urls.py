from django.urls import path
from .views import *

app_name = 'clubs_app'

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('create_club/', create_club, name='create_club')
]