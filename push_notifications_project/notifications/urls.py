# notifications/urls.py
from django.urls import path
from .views import PushNotificationView

urlpatterns = [
    path('send-notification/', PushNotificationView.as_view(), name='send_notification'),
]
