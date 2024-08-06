# notifications/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NotificationSerializer
from .firebase import send_push_notification

# Create your views here.
class PushNotificationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            title = serializer.validated_data['title']
            body = serializer.validated_data['body']
            try:
                response = send_push_notification(token, title, body)
                return Response({'status': 'success', 'response': response}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)