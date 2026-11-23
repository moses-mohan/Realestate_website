from django.contrib import admin
from .models import Property, Booking, Inquiry


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'price')
    search_fields = ('title', 'city')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'property', 'created')
    list_filter = ('property',)


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email', 'city', 'created')
    search_fields = ('name', 'mobile', 'email')