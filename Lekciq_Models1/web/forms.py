from django import forms
from .models import Person


class ToDoForm(forms.Form):
    text = forms.CharField()
    is_done = forms.BooleanField(
        required=False,
    )


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('username', 'age', 'pets')


class RegisterForms(forms.Form):
    GENDERS = (
        ('1', 'Male'),
        ('2', 'Female'),
    )
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))

    gender = forms.ChoiceField(choices=GENDERS)


class LoginForms(forms.Form):
    username = forms.CharField(label="Username", max_length=50,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))

    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))