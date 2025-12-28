from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)  # Заголовок поста
    content = models.TextField()  # Содержимое поста
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего обновления

    def __str__(self):
        return self.title

# Create your models here.
