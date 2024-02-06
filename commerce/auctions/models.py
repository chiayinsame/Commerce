from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    pass


class Listing(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item = models.CharField(max_length=64)
    picture = models.ImageField(upload_to="images/")
    date_created = models.DateTimeField(default=datetime.now())
    # Many Listings to One User relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')

    def __str__(self):
        return self.item
    


class Bid(models.Model):
    price = models.DecimalField(default=1.00, max_digits=12, decimal_places=2)
    # Many Bids to One Listing relationship
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids')
    # Many Bids to One User relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')


class Comment(models.Model):
    content = models.CharField(default="Comment", max_length=400)
    # Many Comments to One Listing relationship
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')
    # Many Comment to One User relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')