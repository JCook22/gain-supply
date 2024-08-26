from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    """
    Adds products to admin panel
    """
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "rating",
        "image",
    )

    ordering = ("sku",)


class CategoryAdmin(admin.ModelAdmin):
    """
    Adds Categories to admin panel
    """
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
