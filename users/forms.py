from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
    
        'placeholder': 'Username',
        'type': 'text',
        'autocomplete': 'off'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
       
        'placeholder': 'Password',
        'type': 'password',
        'autocomplete': 'off'
    }))