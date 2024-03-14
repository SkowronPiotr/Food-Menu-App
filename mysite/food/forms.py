from django import forms
from .models import Item


class ItemCreationForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
