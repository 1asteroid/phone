from django.contrib import admin
from .models import Country, City, DeliveryAddress
from import_export.admin import ImportExportModelAdmin


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ("id", "name")
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('id', )


@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ('id', 'country', 'name')
    list_display_links = ('id', 'country', 'name')
    search_fields = ("id", "name")
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('id',)


@admin.register(DeliveryAddress)
class DeliveryAddressAdmin(ImportExportModelAdmin):
    list_display = ('id', 'order', 'city', 'date_added')
    list_display_links = ('id', 'order', 'city', 'date_added')
    search_fields = ("id", "order")
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('id',)