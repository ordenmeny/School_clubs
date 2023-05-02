from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'clubs_app'

urlpatterns = [
    path('', index, name='home_page'),
    path('create_club/', create_club, name='create_club'),
    path('list_club/<slug:cat_slug>', list_club, name='list_club'),
    path('join_club/<int:club_id>', join_club, name='join_club'),
    path('my_clubs/', my_clubs, name='my_clubs'),
    path('show_content/<slug:slug_club>/acticles', show_articles, name='show_articles')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
