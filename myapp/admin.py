from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomerModelAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'mobileno', 'gender')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('dob', 'gender', 'mobileno', 'address', 'photo')
        }),
    )

admin.site.register(customer_model, CustomerModelAdmin)
admin.site.register(per_km_price_model)
admin.site.register(city_model)
admin.site.register(starting_ending_km_model)
admin.site.register(booking_details_model)
admin.site.register(cancel_booking_model)