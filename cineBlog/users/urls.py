from django.urls import path
from .views import user_login, user_logout, register_user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('register/', register_user, name='register')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
