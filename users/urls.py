from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Выход
    path('logout/', views.logout_view, name='logout'),
    # URL-адреса аутентификации по умолчанию.
    path('', include('django.contrib.auth.urls')),
    # Страница регистрации.
    path('register/', views.register, name='register'),
]