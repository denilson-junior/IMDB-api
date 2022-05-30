from django.contrib import admin
from watchlist.models import Watchlist, StreamPlatform


admin.site.register([Watchlist, StreamPlatform])