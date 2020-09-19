from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """Завершает сеанс работы с приложением."""
    logout(request)
    return redirect('open_blog:posts')

def register(request):
    """Регистрация нового пользователя."""
    if request.method != 'POST':
        # Исходный запрос; создается форма регистрации.   
        form = UserCreationForm()
    else:
        # Обработка заполенной формы.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Регистрируем пользователя и перенаправляем на домашнюю страницу.
            login(request, new_user)
            return redirect('open_blog:posts')

    # Показать пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'registration/register.html', context)
