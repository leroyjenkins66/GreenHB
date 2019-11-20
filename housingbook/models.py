from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    society = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        if not self.society:
            return self.first_name + " " + self.name;
        else:
            return self.society;

class Tenant(models.Model):
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.name;

class Apartment(models.Model):
    code = models.CharField(max_length=200)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    
    def __str__(self):
        return "Apartment " + self.code

class Consumption(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    reading_date = models.DateTimeField('Reading Date')
    reading_value = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.apartment) + ": " + str(self.reading_value) + " on " + self.reading_date.strftime("%d.%m.%Y") #%H %M %S
