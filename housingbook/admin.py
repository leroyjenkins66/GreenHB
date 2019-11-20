from django.contrib import admin

from .models import Apartment, Owner, Tenant, Consumption

admin.site.register(Apartment)
admin.site.register(Owner)
admin.site.register(Tenant)
admin.site.register(Consumption)