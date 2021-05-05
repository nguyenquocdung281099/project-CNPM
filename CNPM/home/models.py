from django.db import models

# Create your models here.
from django.conf import settings

class GetProfileDonate(models.Model):
    LastName = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    Date = models.DateField(blank=True, null=True)
    Email = models.EmailField(max_length = 250)
    Phone = models.CharField(max_length=30)
    Country = models.CharField(max_length=100)
    TypeBlood = models.CharField(max_length=3)
class FeedBacks(models.Model):
    FullName = models.CharField(max_length=200)
    Email = models.EmailField(max_length = 250)
    Phone = models.CharField(max_length=30)
    Message = models.TextField()