from django.forms import ModelForm
from migrator.models import IMAPEndpoint


class LocalEndpointForm(ModelForm):
    class Meta:
        model= IMAPEndpoint
        fields = ['email', 'password']

    def clean(self):
        cleaned_data = super(LocalEndpointForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        #Verifie if the datas are ok
        if email and password:
            if password != 'yop' or email != 'contact@example.com':
                raise forms.ValidationError("Email or password failed.")

        return cleaned_data


class RemoteEndpointForm(ModelForm):
    class Meta:
        model= IMAPEndpoint
        fields = ['email', 'password','host','port','encryption', 'origin_file']

    def clean(self):
        cleaned_data = super(RemoteEndpointForm, self).clean()
        host = cleaned_data.get("host")
        port = cleaned_data.get("port")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        encryption = cleaned_data.get("enrcryption")
        origin_file = cleaned_data.get("origin_file")
        #Verify if the datas are ok
        if email and password:
            if password != 'yop' or email != 'contact@example.com':
                raise forms.ValidationError("Email or password failed.")

        return cleaned_data