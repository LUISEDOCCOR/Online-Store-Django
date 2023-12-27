from django import forms
from django.core import validators

class FormEditAdd (forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
            'class': 'name',
        }
        ),
        validators=[
            validators.MaxLengthValidator(255, 'Too much text')
        ]
    )
    price = forms.IntegerField(
        label='Price',
        widget=forms.NumberInput(
            attrs={
            'class': 'price'
        }
        )
    )
    available = forms.BooleanField(
        label='Available',
        widget=forms.CheckboxInput(
            attrs={
            'class': 'available'
        }
        ),
        required=False
    )
    text = forms.CharField(
        label='Description',
        widget=forms.Textarea(
             attrs={
            'class': 'description'
        } 
        )
    )

    img = forms.ImageField(
        label='Cover image',
        required=True   
    )

    def set_values (self, name, price, available, text):
        self['name'].initial = name
        self['price'].initial = price
        self['available'].initial = available
        self['text'].initial = text    


    def edit (self):    
        del self.fields['img']
        return self