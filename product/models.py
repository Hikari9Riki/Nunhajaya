from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Product(models.Model):
    CREAMPUFF = 0
    CHESSETART = 1
    COMBO = 2
    CAKE = 3
    BROWNISH = 4
    CATEGORY =    (
        (CREAMPUFF, _("Creampuff")),
        (CHESSETART, _("Chesse Tart")),
        (COMBO, _("Combo")),
        (CAKE, _("Cake")),
        (BROWNISH, _("Brownish"))  
    )
    name = models.CharField(max_length=100)
    category = models.SmallIntegerField(choices=CATEGORY, default=CREAMPUFF)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField(max_length=255)

class Order(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order')
    value = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def calculate_total_price(self):
        return self.product.price * self.value