from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Producer(models.Model):
    name = models.CharField(max_length=500)
    short_code = models.CharField(max_length=10, default='SCD')
    contact = models.IntegerField()
    email = models.CharField(max_length=50, null=True)
    address1 = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True)
    pin = models.IntegerField(default=0000)
    active = models.BooleanField(default=True)
    created_date = models.DateField(default=timezone.now())


    def __str__(self):
        return self.name


class Distributor(models.Model):
    name = models.CharField(max_length=500)
    short_code = models.CharField(max_length=10, default='SCD')
    contact = models.IntegerField()
    email = models.CharField(max_length=50, null=True)
    address1 = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True)
    pin = models.IntegerField(default=0000)
    active = models.BooleanField(default=True)
    created_date = models.DateField(default=timezone.now())

    DIST_CLASS_CHOICES = (
        ('STAR', 'Star'),
        ('THREESTAR', '3 Star'),
        ('FIVESTAR', '5 Star'),

    )

    class_division = models.CharField(max_length=4, choices=DIST_CLASS_CHOICES)

    def __str__(self):
        return self.name


class Retail(models.Model):
    name = models.CharField(max_length=500)
    short_code = models.CharField(max_length=10, default='SCD')
    contact = models.IntegerField()
    email = models.CharField(max_length=50, null=True)
    address1 = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True)
    pin = models.IntegerField(default=0000)
    active = models.BooleanField(default=True)
    created_date = models.DateField(default=timezone.now())


    def __str__(self):
        return self.name
