from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import User, Category, Listing


def index(request):
    return render(request, "auctions/index.html", {
        'listings': Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def categories(request):
    categories = Category.objects.all()
    return render(request, "auctions/categories.html", {
        "categories": categories
    })

@login_required(login_url='/login')
def watchlist(request):
    return render(request, "auctions/watchlist.html")

@login_required(login_url='/login')
def create(request):
    form = ListingForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            item = Listing()
            item.title = form.cleaned_data['title']
            item.description = form.cleaned_data['description']
            item.start_bid = form.cleaned_data['start_bid']
            item.category = form.cleaned_data['category']
            if(item.image is not None):
                item.image = form.cleaned_data['image']
            item.save()
            listing = Listing.objects.all()
            return redirect("index")
    else:
        return render(request, "auctions/create.html", {
            "form": form
        })

def viewlisting(request, listing_id):
    return render(request, "auctions/viewlisting.html")