from django.contrib import admin
from watchlist.models import Watchlist, StreamPlatform, Review


admin.site.register([Watchlist, StreamPlatform, Review])