# urls.py
from django.urls import path
from app1.views import home, asd, feed_now, schedule_feeding, feeding_history

urlpatterns = [
    path('', home, name='home'),
    path('asd/', asd, name='index'),
    path('feed-now/', feed_now, name='feed_now'),
    path('schedule-feeding/', schedule_feeding, name='schedule_feeding'),
    path('feeding-history/', feeding_history, name='feeding_history'),  # New URL for feeding history
]
