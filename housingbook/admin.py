from django.contrib import admin

from .models import Apartment, Owner, Tenant

admin.site.register(Apartment)
admin.site.register(Owner)
admin.site.register(Tenant)