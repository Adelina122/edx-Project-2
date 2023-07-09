from django import forms
from .models import Category

class ListingForm(forms.Form):
    title = forms.TextInput(label='Title', max_length=128)
    description = forms.TextInput(label='Description', widget=forms.Textarea)
    start_bid = forms.NumberInput(label='Start bid', min_value=0)
    category = forms.Select(label='Category', choices=Category.obgects.all(), required=False)
    image = forms.URLField(required=False)