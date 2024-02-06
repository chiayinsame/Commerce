from django.contrib import admin
from .models import User, Listing, Bid, Comment

admin.site.register(User)

admin.site.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('price', 'item', 'picture', 'date_created')

admin.site.register(Bid)

admin.site.register(Comment)


