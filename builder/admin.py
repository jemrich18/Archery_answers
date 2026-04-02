from django.contrib import admin
from .models import BowSetup, ArrowBuild


@admin.register(BowSetup)
class BowSetupAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'ibo_speed', 'draw_weight', 'draw_length']
    list_filter = ['draw_weight']
    search_fields = ['name', 'user__username']


@admin.register(ArrowBuild)
class ArrowBuildAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'bow', 'total_arrow_weight', 'arrow_speed', 'kinetic_energy', 'momentum']
    list_filter = ['bow__draw_weight']
    search_fields = ['name', 'user__username']
    readonly_fields = ['total_arrow_weight', 'arrow_speed', 'kinetic_energy', 'momentum']