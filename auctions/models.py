from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
    
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
    # id = models.IntegerField(auto_created=True)
    # name = models.CharField(max_length=64)
    name = models.CharField(choices=CATEGORIES, max_length=35, null=True, blank=True)


    def __str__(self):
        return f"{self.name}"

class Listing(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auctions")
    title = models.CharField(max_length=128)
    description = models.TextField()
    start_bid = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="active_listings")
    # category = models.CharField(choices=CATEGORIES, max_length=35, null=True, blank=True)
    # category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category_for_the_auction', default='Tech')
    # category = models.CharField(max_length=64)
    image = models.URLField()

    def __str__(self):
        return f"{self.id}: {self.title}"

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auctioner")
    start_bid = models.IntegerField()
    auction = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return f"Start: {self.start_bid}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    listings = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment = models.ManyToManyField(Listing, blank=True, related_name="listing")

    def __str__(self):
        return f"{self.listings}: {self.comment}"

class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_watchlist")
    auctions = models.ManyToManyField(Listing, related_name="auctions_in_watchlist", blank=True)

    def __str__(self):
        return f"WatchList for {self.user}"


