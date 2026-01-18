from django.urls import path  # Здесь include для подключения URL-ов приложения
from  .views import home, post_detail, add_post, delete_post
urlpatterns = [
    path('', home, name='home'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('add_post/', add_post, name='add_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
]