from django.urls import path
from . import views
from .views import article_view, create_article, article_detail, edit_article, edit_comment, delete_comment
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('articulos/', article_view, name='articles'),
    path('crear-articulo/', create_article, name='create'),
    path('articulo/<int:id>', article_detail,  name='article_detail'),
    path('editar-articulo/<int:id>', edit_article, name='edit_article'),
    path('editar-comentario/<int:id>', edit_comment, name='edit_comment'),
    path('articulo/<int:article_id>/comentario/<int:comment_id>',delete_comment, name='delete_comment')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
