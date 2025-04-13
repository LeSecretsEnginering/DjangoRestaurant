from django.forms import ModelForm
from .models import Menu
from django import forms

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['image', 'name', 'price', 'description']