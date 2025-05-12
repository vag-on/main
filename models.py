from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Содержание')
    image = models.ImageField('Изображение', upload_to='news_images/', blank=True, null=True)
    date_created = models.DateTimeField('Дата публикации', default=timezone.now)
    is_published = models.BooleanField('Опубликовано', default=False)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date_created']

    def __str__(self):
        return self.title

class Review(models.Model):
    author_name = models.CharField('Имя автора', max_length=100)
    content = models.TextField('Текст отзыва')
    date_created = models.DateTimeField('Дата создания', default=timezone.now)
    is_approved = models.BooleanField('Одобрено', default=False)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-date_created']

    def __str__(self):
        return f'Отзыв от {self.author_name}'

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments', verbose_name='Новость')
    author_name = models.CharField('Имя автора', max_length=100)
    content = models.TextField('Текст комментария')
    date_created = models.DateTimeField('Дата создания', default=timezone.now)
    is_approved = models.BooleanField('Одобрено', default=False)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-date_created']

    def __str__(self):
        return f'Комментарий от {self.author_name} к новости {self.news.title}'
