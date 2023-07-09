from django.contrib import admin
from .models import *

admin.site.register(Listing)
admin.site.register(Bids)
admin.site.register(Comments)
# admin.site.register(Category)