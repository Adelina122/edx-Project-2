from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Bids(models.Model):
    start_bid = models.IntegerField()
    step = models.IntegerField(default=1)

    def __str__(self):
        return f"Start: {self.start_bid}"
    

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auctions")
    title = models.CharField(max_length=128)
    description = models.TextField()
    start_bid = models.IntegerKey()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="active_listings")
    image = models.URLField()

    def __str__(self):
        return f"{self.id}: {self.title} - {self.description}"

class Comments(models.Model):
    listings = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment = models.ManyToManyField(Listing, blank=True, related_name="listing")

    def __str__(self):
        return f"{self.listings}: {self.comment}"

