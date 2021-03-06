from django.db import models


# Create your models here.

class Bb(models.Model):
    KINDS = (
        (None, 'Выберите тип публикации'),
        ('b', 'Куплю'),
        ('s', 'Продам'),
        ('c', 'Обменяю')
    )
    title = models.CharField(max_length=50, verbose_name='Товар или услуга')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публицкации')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Тег')
    #kind = models.CharField(max_length=1, choices=KINDS) # TODO

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Тег')

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'
        ordering = ['name']

    def __str__(self):      # Указывает на то, что все теги
        return self.name    # будут называется своим именем
