from django.contrib import admin
from .models import AnimalThreshold


@admin.register(AnimalThreshold)
class AnimalThresholdAdmin(admin.ModelAdmin):
    list_display = ['name', 'min_kinetic_energy', 'min_momentum', 'sort_order']
    list_editable = ['min_kinetic_energy', 'min_momentum', 'sort_order']