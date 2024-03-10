from django.db import models
from users.models import User
from products.models import Product


# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    selected_for_purchase = models.BooleanField(default=True)