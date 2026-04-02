from django.contrib import admin
from .models import Manufacturer, ArrowShaft, Vane, Nock, Insert, Broadhead


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'website']
    search_fields = ['name']


@admin.register(ArrowShaft)
class ArrowShaftAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'model_name', 'spine', 'gpi', 'inner_diameter', 'status', 'submitted_by']
    list_filter = ['status', 'manufacturer']
    list_editable = ['status']
    search_fields = ['model_name', 'manufacturer__name']


@admin.register(Vane)
class VaneAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'model_name', 'length_inches', 'height_inches', 'weight_grains', 'status']
    list_filter = ['status', 'manufacturer']
    list_editable = ['status']
    search_fields = ['model_name', 'manufacturer__name']


@admin.register(Nock)
class NockAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'model_name', 'nock_type', 'weight_grains', 'compatible_diameter', 'status']
    list_filter = ['status', 'manufacturer', 'nock_type']
    list_editable = ['status']
    search_fields = ['model_name', 'manufacturer__name']


@admin.register(Insert)
class InsertAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'model_name', 'insert_type', 'weight_grains', 'material', 'status']
    list_filter = ['status', 'manufacturer', 'insert_type']
    list_editable = ['status']
    search_fields = ['model_name', 'manufacturer__name']


@admin.register(Broadhead)
class BroadheadAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'model_name', 'broadhead_type', 'weight_grains', 'cutting_diameter', 'status']
    list_filter = ['status', 'manufacturer', 'broadhead_type']
    list_editable = ['status']
    search_fields = ['model_name', 'manufacturer__name']