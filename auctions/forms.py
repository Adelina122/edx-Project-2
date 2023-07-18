from django import forms
from .models import *

class ListingForm(forms.Form):
    # model = Listing
    title = forms.CharField(label='Title', max_length=128)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    start_bid = forms.IntegerField(label='Start bid', min_value=0)
    # category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    category = forms.Select(choices=CATEGORIES)
    image = forms.URLField(label='URL for an Image', required=False)