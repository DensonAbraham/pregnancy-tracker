from django.db import models

# Create your models here.
class User_Data(models.Model):
    name = models.CharField(max_length=2550)
    password = models.CharField( null=True, max_length=50)
    phone_number = models.IntegerField( null=True, blank=True)
    weight = models.IntegerField( null=True, blank=True)
    last_menstural_date = models.DateField(null=True)