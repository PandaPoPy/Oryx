from django.forms import ModelForm
from django import forms
from migrator.models import IMAPEndpoint


class LocalEndpointForm(ModelForm):
    class Meta:
        model= IMAPEndpoint
        fields = ['email_imap', 'password_imap']
        widgets = {
        'password_imap': forms.PasswordInput(),
        }


class RemoteEndpointForm(ModelForm):
    class Meta:
        model= IMAPEndpoint
        fields = ['email_imap', 'password_imap','host_imap','port_imap','encryption_imap', 'path']
        widgets = {
        'password_imap': forms.PasswordInput(),
        }