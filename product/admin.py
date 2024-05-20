from django.contrib import admin
from django.template.defaultfilters import slugify

from .models import Product, SubCategory,Review
from import_export.admin import ImportExportModelAdmin
import uuid


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', "name", "price", "max_count", "data_added")
    list_display_links = ('id', "name", "price", "max_count")
    prepopulated_fields = {"slug": ("name", )}
    search_fields = ("id", "name")
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('id', 'name')

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.name + f'{uuid.uuid4()}')
        super().save_model(request, obj, form, change)


@admin.register(SubCategory)
class SubCategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ('id', 'name', 'image')
    search_fields = ("name", )
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('id', )


@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    list_display = ('user', 'product', 'text', 'rating')
    list_display_link = ('user', 'product', 'text', 'rating')
    search_fields = ("text", "product", "user")
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('id',)
