from django import forms
from .models import Products
from .choices import *
from django.forms.widgets import NumberInput, TextInput,DateInput,FileInput,Select

class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput(attrs={'class':'userna common','placeholder': 'Name'}))
    weight = forms.CharField(widget=TextInput(attrs={'class':'userna common','placeholder': 'Weights'}))
    color = forms.ChoiceField(widget=Select(attrs={'class':'userna common'}),choices=CATEGORY_COLORS)
   
    class Meta:
        model = Products
        fields = ('name', 'weight', 'color', 'price', 'category', 'stock', 'description', 'images',)
