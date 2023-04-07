from django.urls import path
from .views import HomePage

app_name = 'clubs_app'

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),

]
