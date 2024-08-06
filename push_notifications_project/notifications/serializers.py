# notifications/serializers.py
from rest_framework import serializers

class NotificationSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
    body = serializers.CharField(max_length=255)
