from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    slug = models.CharField(max_length=150, verbose_name='slug')
    content = models.TextField(max_length=1000, verbose_name='название')
    preview = models.ImageField(verbose_name='изображение')
    date_of_creation = models.DateTimeField(verbose_name='дата создания')
    sign_of_publication = models.CharField(max_length=150, verbose_name='опубликовано')
    number_of_views = models.Count

    def __str__(self):
        return self.title


class Meta:
    verbose_name = 'статья'
    verbose_name_plural = 'статьи'
