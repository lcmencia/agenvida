from django.contrib import admin
from .models import Purpose

# Register your models here.

class PurposeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'creado','fecha_inicio', 'fecha_fin', 'meta']
    list_filter = ['creado', 'fecha_inicio','fecha_fin']
    search_fields =['nombre', 'descripcion']
    class Meta:
        model = Purpose
        
admin.site.register(Purpose, PurposeAdmin)
