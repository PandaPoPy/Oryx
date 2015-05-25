from django.contrib import admin

# Register your models here.
from .models import IMAPEndpoint, Migration


class IMAPEndpointAdmin(admin.ModelAdmin):
    list_display = ('login', 'password', 'host','port', 'encryption','dossier_racine')

class MigrationAdmin(admin.ModelAdmin):
    fieldsets=[
        ('source', {'fields': ['source']}),
        ('target', {'fields': ['target']}),
        ('creation date', {'fields': ['creation_date']}),
        ('processing date', {'fields': ['processing_date']}),
        ('date de fin', {'fields': ['completion_date']}),
    ]
    list_display = ('source', 'target', 'creation_date','processing_date', 'completion_date')


admin.site.register(IMAPEndpoint, IMAPEndpointAdmin)
admin.site.register(Migration, MigrationAdmin)