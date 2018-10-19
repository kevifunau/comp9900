from django.forms import Textarea,NumberInput
from django import forms
from Property.models import Property,  Images
from django.contrib.auth.forms import ReadOnlyPasswordHashField
import datetime

class PendingForm(forms.ModelForm):
    """
    pending form
    """
    # image = forms.ImageField(required=False)
    class Meta:
        model = Property
        field = fields = ['price','capacity', 'party', 'pet', 'smoking','couple']
        labels = {
            'capacity': 'Guests',
        }

        widgets = {
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),

            'party': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'pet': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'smoking': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'couple': forms.CheckboxInput(attrs={'class': 'form-control'}),

        }
'''
    party = models.BooleanField(default=False)
    pet = models.BooleanField(default=False)
    smoking = models.BooleanField(default=False)
    couple = models.BooleanField(default=False)
'''




