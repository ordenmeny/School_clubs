from django.urls import path, include
from .views import index, members, delete_member, content, add_article
from django.conf import settings
from django.conf.urls.static import static

app_name = 'dashboard_app'
urlpatterns = [
    path('<slug:slug_club>/profile/', index, name='profile'),
    path('<slug:slug_club>/members/', members, name='members'),
    path('<slug:slug_club>/<int:id_member>/delete/', delete_member, name='delete_member'),
    path('<slug:slug_club>/content/', content, name='content'),
    path('<slug:slug_club>/content/add_article', add_article, name='add_article'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
