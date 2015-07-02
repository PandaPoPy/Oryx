from django.contrib import admin

# Register your models here.
from .models import IMAPEndpoint, Migration


class IMAPEndpointAdmin(admin.ModelAdmin):
    list_display = ('email_imap', 'password_imap', 'host_imap','port_imap', 'encryption_imap','path')

class MigrationAdmin(admin.ModelAdmin):
    list_display = ('origin', 'target', 'creation_date','processing_date', 'completion_date')


admin.site.register(IMAPEndpoint, IMAPEndpointAdmin)
admin.site.register(Migration, MigrationAdmin)