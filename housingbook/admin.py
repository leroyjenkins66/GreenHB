from django.contrib import admin

from .models import Apartment, Owner, Tenant, Consumption

class ApartmentAdmin(admin.ModelAdmin):
    fields = ['code', 'owner', 'tenant', 'user']
    list_display = ('code', 'owner', 'tenant')
    ordering = ['code']

class OwnerAdmin(admin.ModelAdmin):
    fields = ['first_name', 'name', 'society']
    list_display = ['first_name', 'name', 'society']
    
class TenantAdmin(admin.ModelAdmin):
    fields = ['first_name', 'name']
    list_display = ['first_name', 'name']
    
class ConsumptiontAdmin(admin.ModelAdmin):
    fields = ['apartment', 'reading_date', 'reading_value']
    list_display = ['apartment', 'reading_date', 'reading_value']
    list_filter = ['apartment']
    ordering = ['apartment']

admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Tenant, TenantAdmin)
admin.site.register(Consumption, ConsumptiontAdmin)