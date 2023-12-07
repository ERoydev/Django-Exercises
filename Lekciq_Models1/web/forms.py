from django import forms


class RegisterForms(forms.Form):
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))
