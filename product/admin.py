from django.contrib import admin
from django.template.defaultfilters import slugify

from .models import Product
from import_export.admin import ImportExportModelAdmin
import uuid


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', "name", "price", "max_count")
    list_display_links = ('id', "name", "price", "max_count")
    prepopulated_fields = {"slug": ("name", "price", "category")}
    search_fields = ("id", "name")
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('name', 'id')

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.name + '-' + str(obj.price) + '-' + obj.category)
        super().save_model(request, obj, form, change)
