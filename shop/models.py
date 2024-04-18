from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from pytils.translit import slugify as pytils_slugify
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    slug = models.SlugField(max_length=255, blank=True)
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='категория')
    description = models.TextField(verbose_name='описание')
    # price = models.PositiveIntegerField(null=False, verbose_name='цена')
    # brand = models.CharField()
    # arti = models.CharField()
    # photo = models.ImageField()
    # axis = models.CharField
    # weight = models.CharField()
    # material = models.CharField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def save(self, *args, **kwargs):
        self.slug = slugify(pytils_slugify(self.title))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('put', kwargs={'slug': self.slug})


class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    parent = TreeForeignKey(
        'self', on_delete=models.PROTECT, null=True, blank=True, related_name='children', db_index=True, verbose_name='Родительская категория'
    )
    slug = models.SlugField(max_length=100)

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('post-by-category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
