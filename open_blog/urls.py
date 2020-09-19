"""Определяет схемы URL для open_blog"""

from django.urls import path
from . import views


app_name = 'open_blog'
urlpatterns = [
    # вывод всех постов
    path('', views.all_posts, name='posts'),
    # страница отдельного поста
    path('post/<int:pk>', views.post, name='post'),
    # страница для добавления нового поста
    path('new_post/', views.new_post, name='new_post'),
    # страница для добавления комментариев
    path('post/<int:pk>/comment/', views.comment, name='comment'),
]