from django import forms
from django.forms.widgets import DateInput

from login.models import Product


class CustomDateInput(DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'
    input_formats = ['%Y-%m-%d']


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'prod_name', 
            'prod_new', 
            'permuta', 
            'prod_price', 
            'prod_description',
            'prod_affinitie1', 
            'prod_affinitie2',
            'prod_photo1', 
            'prod_photo2', 
            'prod_photo3', 
            'prod_photo4', 
            'prod_photo5'
        ]
