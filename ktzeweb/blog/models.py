from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    pub_date = models.DateField()

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
    
    def __str__(self) -> str:
        return self.title


class Request(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()