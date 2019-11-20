from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    society = models.CharField(max_length=200)

class Tenant(models.Model):
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)

class Apartment(models.Model):
    code = models.CharField(max_length=200)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

class Consumption(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    reading_date = models.DateTimeField('Reading Date')
    reading_value = models.IntegerField(default=0)
