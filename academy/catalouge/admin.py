from django.contrib import admin
from .models import Category, Brand, Product, ProductAttributeValue, ProductType


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")
    search_fields = ('name',)


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "upc", "description", "product_type")
    search_fields = ('title',)


class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = ("product_attribute", "value", "product")
    search_fields = ('product_attribute',)


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("title", "created_time")
    search_fields = ("title",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductAttributeValue, ProductAttributeValueAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
