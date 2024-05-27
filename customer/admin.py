import uuid

from django.contrib import admin
from django.utils.text import slugify

from .models import Customer, Order, OrderItems, Appeal
from import_export.admin import ImportExportModelAdmin


@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('user', "image")
    list_display_links = ('user', "image")
    search_fields = ("id", "user")
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('user', )


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')
    prepopulated_fields = {"slug": ("user",)}
    search_fields = ("id", "user")
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('id', )

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(f'{uuid.uuid4()}')
        super().save_model(request, obj, form, change)


@admin.register(OrderItems)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'product', "order", 'quantity')
    list_display_links = ('id', 'product', "order", 'quantity')
    search_fields = ("id", )
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('id', )


@admin.register(Appeal)
class AppealAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'message')
    list_display_links = ('id', 'user', 'message')
    search_fields = ('id', 'user')
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('id',)
