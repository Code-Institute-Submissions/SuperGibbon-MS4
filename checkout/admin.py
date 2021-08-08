from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = (
        'order_number',
        'date',
        'order_total',)

    fields = (
        'order_number',
        'user_profile',
        'full_name',
        'email',
        'date',
        'order_total')

    list_display = (
        'order_number',
        'full_name',
        'email',
        'date',
        'order_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
