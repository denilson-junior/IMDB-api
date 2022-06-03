from django.urls import path
from watchlist.api.views import WatchList, WatchDetail, StreamPlatformList, StreamPlatformDetail, ReviewDetail, ReviewList

urlpatterns = [
    path('list/', WatchList.as_view(), name='watchlist-list'),
    path('<int:pk>', WatchDetail.as_view(), name='watchlist-detail'),
    path('stream/', StreamPlatformList.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetail.as_view(), name='stream-detail'),

    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]
