from django import forms
from django.core import validators


class UserForm(forms.Form):
     name = forms.CharField(
         label='Name',
         widget= forms.TextInput(
             attrs={
                 'class': 'name'  
             }
         )
     )
     email = forms.CharField(
         label='Email',
         widget=forms.EmailInput(
             attrs={
                 'class': 'email'
                 }
             ),
         validators=[validators.EmailValidator()]
     )
     password = forms.CharField(
         label='Password',
         widget=forms.PasswordInput(
             attrs={
                 'class': 'password'
             }
         )
     )
