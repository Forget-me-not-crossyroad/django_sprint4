from django.contrib.auth import get_user_model
from django.db import models

from core.models import PublishedModel

User = get_user_model()


class Category(PublishedModel):
    """Модель Категории."""
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок',
        help_text='Название категории, не более 256 символов'
    )
    slug = models.SlugField(
        unique=True,
        max_length=64,
        verbose_name='Идентификатор',
        help_text=('Идентификатор страницы для URL; разрешены символы'
                   ' латиницы, цифры, дефис и подчёркивание.')
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание категории, текстовое поле'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(PublishedModel):
    """Модель Местоположения."""
    name = models.CharField(
        max_length=256,
        verbose_name='Название места',
        help_text='Название местоположения, не более 256 символов'
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Post(PublishedModel):
    """Модель Публикации."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
        help_text='Автор поста'
    )
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок',
        help_text='Заголовок поста, не более 256 символов'
    )
    text = models.TextField(
        verbose_name='Текст',
        help_text='Текст поста'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=('Если установить дату и время в будущем'
                   ' — можно делать отложенные публикации.')
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        verbose_name='Категория',
        help_text='Название категории'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name='Местоположение',
        help_text='Название местоположения'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
