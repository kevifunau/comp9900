from django.forms import Textarea,NumberInput
from django import forms
from Property.models import Property,  Images
from django.contrib.auth.forms import ReadOnlyPasswordHashField
import datetime

class PropertyForm(forms.ModelForm):
    """
    添加房屋表单
    """
    # image = forms.ImageField(required=False)
    class Meta:
        model = Property
        field = exclude = ['user_ID','created_at', 'updated_at', 'longitude', 'latitude']
        labels = {
            'user_ID': 'Your email',
            'province': 'Country / Region',
            'address': 'Street Address',
            'postcode': 'Post code',
            'capacity': 'Guests',
            'status': 'Release now?',
            'num_bathrooms': 'Number of Bathroom',
            'num_bedrooms': 'Number of Bedroom',
            'num_double_bed': 'Number of Double Bed',
            'num_single_bed': 'Number of Single Bed',
            'num_sofa_bed': 'Number of Sofa Bed',
            'ac': 'Air Conditioner',
            'tv': 'TV',
            'wifi': 'WIFI',
        }

        widgets = {
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'types_property': forms.Select(attrs={'class': 'form-control'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'postcode': forms.NumberInput(attrs={'class': 'form-control'}),

            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_bathrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_bedrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_double_bed': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_single_bed': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_sofa_bed': forms.NumberInput(attrs={'class': 'form-control'}),
            'area': forms.NumberInput(attrs={'class': 'form-control'}),

            'kitchen': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'in_unit_washer': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'wifi': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'elevator': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'heating': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'ac': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'tv': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'blower': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'bathtub': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'parking': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'gyms': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'swimming_pool': forms.CheckboxInput(attrs={'class': 'form-control'}),

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
class ImageForm(forms.ModelForm):
    """
    添加图片表单
    """
    class Meta:
        model = Images
        fields = ('image',)

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }



class AddReviewForm(forms.Form):

    pid =  forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    trip_id = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    position_review = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    comfort_review = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    price_review= forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    quality_review = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    comment_content = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))



