from django.urls import path
from watchlist.api.views import WatchList, WatchDetail, StreamPlatformList, StreamPlatformDetail

urlpatterns = [
    path('list/', WatchList.as_view(), name='watchlist-list'),
    path('<int:pk>', WatchDetail.as_view(), name='watchlist-detail'),
    path('stream/', StreamPlatformList.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetail.as_view(), name='stream-detail'),
]
