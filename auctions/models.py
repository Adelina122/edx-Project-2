from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Bids(models.Model):
    start_bid = models.IntegerField()
    step = models.IntegerField(default=1)

    def __str__(self):
        return f"Start: {self.start_bid}"
    

CATEGORIES = [
        ('Appliances', 'Appliances'),
        ('Tech', 'Tech'), 
        ('Gaming', 'Gaming'), 
        ('Fashion', 'Fashion'), 
        ('Sports and Fitness','Sports and Fitness'), 
        ('Other','Other'),
        ("Hygiene and Medicine","Hygiene and Medicine"), 
        ("Stationery","Stationery"),
        ('Decor', 'Decor'), 
        ('Furniture','Furniture'), 
        ('Cars and Mechanical Things','Cars and Mechanical Things'), 
        ("Tools","Tools")
    ]

class Category(models.Model):
    # name = models.CharField(max_length=64)
    name = models.CharField(choices=CATEGORIES, max_length=35, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Listing(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auctions")
    title = models.CharField(max_length=128)
    description = models.TextField()
    start_bid = models.IntegerField()
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="active_listings")
    category = models.CharField(choices=CATEGORIES, max_length=35, null=True, blank=True)
    # category = models.CharField(max_length=64)
    image = models.URLField()

    def __str__(self):
        return f"{self.id}: {self.title}"

class Comments(models.Model):
    listings = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment = models.ManyToManyField(Listing, blank=True, related_name="listing")

    def __str__(self):
        return f"{self.listings}: {self.comment}"

