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
    FASHION = "FN"
    TOYS = "TY"
    ELECTRONICS = "EL"
    HOME = "HM"
    SPORT = "SP"

    CATEGORY_CHOICES = [
        (FASHION, 'Fashion'),
        (TOYS, 'Toys'),
        (ELECTRONICS, 'Electronics'),
        (HOME, 'Home'),
        (SPORT, 'Sport'),
    ]
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=FASHION)

    def __str__(self):
        return self.category

class Listing(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    start_bid = models.ForeignKey(Bids, on_delete=models.CASCADE, related_name="bids")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.URLField()

    def __str__(self):
        return f"{self.id}: {self.title} - {self.description}"

class Comments(models.Model):
    listings = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment = models.ManyToManyField(Listing, blank=True, related_name="listing")

    def __str__(self):
        return f"{self.listings}: {self.comment}"

