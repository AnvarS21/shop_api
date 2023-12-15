from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from category.models import Category

User = get_user_model()


class Product(models.Model):
    STATUS_CHOICES = (
        ('in_stock', 'В наличии!'),
        ('out_of_stock', 'Нет в наличии!')
    )
    owner = models.ForeignKey(User, on_delete=models.RESTRICT,
                              related_name='products')
    title = models.CharField(max_length=150)
    description = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True,
                                 related_name='products')
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.CharField(choices=STATUS_CHOICES, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title