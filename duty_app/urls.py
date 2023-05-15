from django.urls import include, path
from .views import *

app_name = 'duty_app'

urlpatterns = [
    path('', home, name='home'),
    path('action_duty/<str:type_action>/<int:id_person>/', action_duty, name='action_duty'),
    # path('is_duty/', home, name='is_duty'),
]