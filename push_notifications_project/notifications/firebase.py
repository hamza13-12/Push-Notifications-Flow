# notifications/firebase.py
import firebase_admin
from firebase_admin import credentials, messaging
import os

# Path to your service account key file
cred_path = os.path.join(os.path.dirname(__file__), '..', 'credentials', 'serviceAccountKey.json')

if not os.path.exists(cred_path):
    raise FileNotFoundError(f"Service account key file not found: {cred_path}")

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

def send_push_notification(registration_token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=registration_token,
    )
    response = messaging.send(message)
    return response
