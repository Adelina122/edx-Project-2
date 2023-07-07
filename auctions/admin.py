from django.contrib import admin
from .models import Listing, Bids, Comments

admin.site.register(Listing)
admin.site.register(Bids)
admin.site.register(Comments)