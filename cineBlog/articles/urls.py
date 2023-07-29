from django.urls import path
from . import views
from .views import article_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('article/', article_view, name='article'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
