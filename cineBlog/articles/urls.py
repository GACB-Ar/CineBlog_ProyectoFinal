from django.urls import path
from . import views
from .views import article_view, create_article, article_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('articulos/', article_view, name='articles'),
    path('crear-articulo/', create_article, name='create'),
    path('articulo/<int:id>', article_detail,  name='article_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
