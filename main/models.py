# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")
    descr = models.CharField(max_length=255, verbose_name="Описание категории", default="Описание категории")
    alias = models.SlugField(verbose_name="Alias категории")
    #image1 = models.ImageField(upload_to='categories_img', height_field=180, width_field=200)
    image = models.CharField(max_length=255, verbose_name="Путь к картинке категории", \
                                default="category_image_filename")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

        def __str__(self):
            return 'Категория %s' % self.name


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    price = models.IntegerField(default=0, verbose_name="Цена")
    alias = models.SlugField(verbose_name="Alias товара")
    image = models.CharField(max_length=255, verbose_name="Путь к картинке товара", \
                                default="item_image_filename")

    AVAILABLE_CHOICES = (
        ('available','В наличии'),
        ('pre-order', 'По предзаказу'),
    )
    available = models.CharField(max_length=9, choices=AVAILABLE_CHOICES, default='available')


    def __unicode__(self):
        return self.name

    category = models.ForeignKey(Category)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return 'Товар: %s' % self.name
