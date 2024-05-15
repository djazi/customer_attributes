from django.contrib import admin
from loyalty_attributes.models import (
    Customer,
    LoyaltyAttribute,
    CustomerLoyaltyAttribute,
)

# Register your models here.

admin.site.register(Customer)
admin.site.register(LoyaltyAttribute)
admin.site.register(CustomerLoyaltyAttribute)
