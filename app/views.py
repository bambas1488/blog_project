from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm  # Импортируем форму для постов
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all()  # Получаем все посты
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)  # Получаем пост по ID
    return render(request, 'blog/post_detail.html', {'post': post})  # Передаем объект в шаблон

@login_required
def add_post(request):
    # Функция для добавления нового поста
    if request.method == 'POST':
        form = PostForm(request.POST)  # Получаем данные из формы
        if form.is_valid():
            form.save()  # Сохраняем новый пост в базе данных
            return redirect('home')  # После добавления, редиректим на главную
    else:
        form = PostForm()  # Если форма пустая (GET запрос), то создаём пустую форму

    return render(request, 'blog/add_post.html', {'form': form})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect('home')  

    return redirect('post_detail', post_id=post.id)


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  # instance = редактируемый пост
        if form.is_valid():
            form.save()  # сохранит изменения, не создаст новый пост
            return redirect('home')  # после редактирования вернём на главную
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})
