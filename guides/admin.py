from django.contrib import admin
from .models import Guide, Category


class GuideAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'rating',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Guide, GuideAdmin)
admin.site.register(Category, CategoryAdmin)
