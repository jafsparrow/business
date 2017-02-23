from django.db import models
from django.utils import timezone

from mainusers.models import Producer


# Product Model managers
class ActiveProducts(models.Manager):
    def get_queryset(self):
        return super(ActiveProducts, self).get_queryset().filter(active=True)

# Create your models here.
class Product(models.Model):
    producer = models.ForeignKey(Producer)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10, null=True)
    barcode = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=300, null=True)
    add_date = models.DateField(default= timezone.now())
    active = models.BooleanField(default= True)
    cost_price = models.IntegerField()
    discount_allowed = models.BooleanField(default=True)

    # Model Managers
    objects = models.Manager()
    products = ActiveProducts()

    def __str__(self):
        return self.name


class PriceList(models.Model):
        DIST_CLASS_CHOICES = (
            ('STAR', 'Star'),
            ('THREESTAR', '3 Star'),
            ('FIVESTAR', '5 Star'),

          )

        class_division = models.CharField(max_length=10,choices=DIST_CLASS_CHOICES)
        product = models.ForeignKey(Product)
        unit_price = models.IntegerField()
        valid_till = models.DateField(null=True)
        add_date = models.DateField(default=timezone.now())

        class Meta:
            unique_together = (("product", "class_division"),)

        def __str__(self):
            self.product.name
