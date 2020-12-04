from django.contrib import admin
from .models import Order,OrderItem,Item,Payment,Address
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'payment',
                    'billing_adresss',
                    'shipping_adresss'
                    ]
    list_display_links = [
        'user',
        'shipping_adresss',
        'billing_adresss',
        'payment',
    ]
    
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'appartment_address',
        'country',
        'zipcode',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'appartment_address', 'zipcode']

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Item)
admin.site.register(Payment)
admin.site.register(Address,AddressAdmin)