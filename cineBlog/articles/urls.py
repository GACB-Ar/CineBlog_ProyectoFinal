from django.urls import path
from . import views
from .views import article_view, create_article
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('article/', article_view, name='article'),
    path('create_article/', create_article, name='create')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
