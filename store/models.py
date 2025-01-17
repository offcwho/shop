from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название категории")
    slug = models.CharField(max_length=200, verbose_name="URL-адрес", unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    title = models.CharField(max_length=200, verbose_name="Название продукта")
    slug = models.CharField(max_length=200, verbose_name="URL-адрес", unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Отображать на сайте")
    description = models.TextField(verbose_name="Описание продукта", blank=False)
    image = models.ImageField(upload_to="shop/", verbose_name="Изображения продукта", blank=False, null=False)
    price = models.IntegerField(verbose_name="Стоимость")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title

