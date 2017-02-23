from django.db import models
from order.models import Retail_order
# Create your models here.
class Invoice(models.Model):
    retail_order = models.ForeignKey(Retail_order)
    invoice_date = models.DateField(null=True)
    payment = models.BooleanField(default=False)
    due_date = models.DateField(null=True)


    def __str__(self):
        return str(self.retail_order)
