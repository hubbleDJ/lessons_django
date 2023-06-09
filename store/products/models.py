from django.db import models
from users.models import User


# Create your models here.
# Модели == таблицы


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to="products_image")
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self) -> str:
        return f'''{self.name}'''


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum([basket.sum() for basket in self])
    
    def total_quantity(self):
        return sum([basket.quantity for basket in self])


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self) -> str:
        return f'''Корзина для {self.user.email} | Продукт {self.product.name}'''
    
    def sum(self):
        return self.quantity * self.product.price