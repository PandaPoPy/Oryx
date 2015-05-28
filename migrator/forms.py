from django import forms


class Local_Endpoint(forms.Form):
    email=forms.EmailField(label='Email :')
    password=forms.CharField(label='Password :', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(Local_Endpoint, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        #Verifie if the datas are ok
        if email and password:
            if password != 'yop' or email != 'contact@example.com':
                raise forms.ValidationError("Email or password failed.")


        return cleaned_data


class Remote_Endpoint(forms.Form):
    host = forms.CharField(label='Your Host :')
    port = forms.IntegerField(label='Your Port :')
    email = forms.EmailField(label='Email :')
    password = forms.CharField(label='Password :', widget=forms.PasswordInput)
    #ssl=forms.ListField(label='Type of your SSL')
    NONE = 'NO'
    SSL_TLS = 'SSL'
    START_TLS = 'START'
    SSL_CHOICES = (
        (NONE, 'None'),
        (SSL_TLS, 'SSL/TLS'),
        (START_TLS, 'STARTTLS'),
    )
    ssl = forms.ChoiceField(choices=SSL_CHOICES)

    def clean(self):
        cleaned_data = super(Remote_Endpoint, self).clean()
        host = cleaned_data.get("host")
        port = cleaned_data.get("port")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        ssl = cleaned_data.get("ssl")
        #Verify if the datas are ok
        if email and password:
            if password != 'yop' or email != 'contact@example.com':
                raise forms.ValidationError("Email or password failed.")


        return cleaned_data