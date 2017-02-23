from django.contrib import admin
from product.models import Product, PriceList
# Register your models here.
admin.site.register(Product)
admin.site.register(PriceList)
