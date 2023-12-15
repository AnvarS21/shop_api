from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from config.tasks import send_notification_task
from product.models import Product

# Create your models here.


User = get_user_model()

STATUS_CHOICES = (
    ('open', 'Открыт'),
    ('in_process', 'В обработке'),
    ('closed', 'Закрыт')
)


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.product.title} -> {self.order}'


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders',
                             on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through=OrderItem)
    address = models.CharField(max_length=150)
    number = models.CharField(max_length=150)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    total_sum = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} -> {self.user}'

@receiver(post_save, sender=Order)
def order_post_save(sender, instance, created, **kwargs):
    send_notification_task.delay(
        instance.user.email, instance.id, instance.total_sum
    )
