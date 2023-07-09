from django import forms
# from .models import Category

class ListingForm(forms.Form):
    title = forms.CharField(label='Title', max_length=128)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    start_bid = forms.IntegerField(label='Start bid', min_value=0)
    category = forms.CharField(label='Category', max_length=64, required=False)
    image = forms.URLField(label='URL for an Image', required=False)