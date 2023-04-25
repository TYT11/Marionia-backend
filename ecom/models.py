import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Product(models.Model):
    # title, img, price, stock, id, category
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    CATEGORY_CHOICES = [('SLL', 'Shells'), ('WPN', 'Weapons'),
                        ('MSHRM', 'Mushrooms'), ('MYBX', 'Mystery Boxes')]
    category = models.CharField(
        max_length=10, choices=CATEGORY_CHOICES, default='SLL')
    img = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    # order = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default="")
    phone = models.CharField(max_length=10, default="")
    address = models.CharField(max_length=20, default="")
    created = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(
        choices=[(1, 'Processing'), (2, 'Shipped'), (3, 'Delivered')], default=1)
    total = models.IntegerField()


class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE)
    item = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="item")
    price = models.IntegerField()
    qty = models.IntegerField(default=1)
