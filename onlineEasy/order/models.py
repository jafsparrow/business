from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


from mainusers.models import Retail
from product.models import Product
# Create your models here.
class Retail_order(models.Model):
    user = models.ForeignKey(User)
    retail = models.ForeignKey(Retail)
    total_cost = models.DecimalField(max_digits=6, decimal_places=2)
    order_date = models.DateField(default=timezone.now)

    STATUS_CHOICES=(('DFT', 'Draft'),
                    ('CNF', 'Confirmed'),
                    ('INP','In Progress'),
                    ('DIS','Dispatched'),
                    ('DLV', 'Delivered'),
                    )

    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    class Meta:
        ordering = ['-order_date']

    def __str__(self):
        return str(self.id)


class Order_details(models.Model):
    retail_order = models.ForeignKey(Retail_order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()


    class Meta:
        ordering = ['-retail_order', 'product']
