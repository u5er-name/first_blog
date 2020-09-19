from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    topic = models.CharField('Тема', max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    entry = models.TextField('Текст')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.topic


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField('Комментарий')
    author = models.CharField(max_length=200)
    #comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.comment
