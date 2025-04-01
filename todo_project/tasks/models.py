from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)  # название задачи
    description = models.TextField(blank=True)  # описание (необязательно)
    completed = models.BooleanField(default=False)  # статус выполнения
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания

    def __str__(self):
        return self.title