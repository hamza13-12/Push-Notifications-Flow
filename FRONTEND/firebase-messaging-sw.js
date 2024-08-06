importScripts('https://www.gstatic.com/firebasejs/9.0.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.0.0/firebase-messaging-compat.js');

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCQOyeCippYoAxGA0K7qeoPSmhFwcgfbtE",
    authDomain: "test-notifications-3a770.firebaseapp.com",
    projectId: "test-notifications-3a770",
    storageBucket: "test-notifications-3a770.appspot.com",
    messagingSenderId: "136320399536",
    appId: "1:136320399536:web:634d21119a380d96c02375"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Initialize Firebase Cloud Messaging
const messaging = firebase.messaging();

messaging.onBackgroundMessage(function(payload) {
    console.log('[firebase-messaging-sw.js] Received background message ', payload);
    // Customize notification here
    const notificationTitle = payload.notification.title;
    const notificationOptions = {
        body: payload.notification.body
    };

    self.registration.showNotification(notificationTitle, notificationOptions);
});
