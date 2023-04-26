from django.urls import path, include
from .views import index

app_name = 'dashboard_app'
urlpatterns = [
    path('<slug:slug_club>/', index, name='home_page'),
]
