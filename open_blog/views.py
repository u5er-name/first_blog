from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Post, Comment
from .forms import PostForm, CommentForm


def all_posts(request):
    """Вывод всех постов приложения Open Blog"""
    posts = Post.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'open_blog/all_posts.html', context)

def post(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post__pk=pk)
    context = {'post': post, 'comments': comments}
    return render(request, 'open_blog/post.html', context)

def new_post(request):
    """Определяет новый пост"""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = PostForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
        return redirect('open_blog:posts')
    
    context = {'form': form}
    return render(request, 'open_blog/new_post.html', context)

def comment(request, pk):
    """Определяет комментарий пользователя"""
    post = Post.objects.get(pk=pk)
    if request.method != 'POST':
         # Данные не отправлялись; создается пустая форма.
        form = CommentForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
        return redirect('open_blog:post', pk=pk)
    
    context = {'post': post, 'form': form}
    return render(request, 'open_blog/comment.html', context)
