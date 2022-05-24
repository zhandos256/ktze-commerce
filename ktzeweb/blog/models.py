from django.db import models
from django.forms import ImageField, SlugField


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    pub_date = models.DateField()
    mail = models.EmailField(max_length=150, default='')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    
    def __str__(self) -> str:
        return self.title