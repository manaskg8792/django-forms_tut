from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    is_married = models.BooleanField(default=False)
