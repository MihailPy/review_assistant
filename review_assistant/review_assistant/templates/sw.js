//console.log('Hello from sw.js');
//
//importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.2.0/workbox-sw.js');
//
//if (workbox) {
//  console.log(`Yay! Workbox is loaded 🎉`);
//  navigator.serviceWorker.addEventListener('controllerchange',  ()  => window.location.reload());
//  workbox.precaching.precacheAndRoute([
//    {
//      "url": "/home_page/",
//      "revision": "1"
//    }
//  ]);
//
//  workbox.routing.registerRoute(
//    /\.(?:js|css)$/,
//    workbox.strategies.staleWhileRevalidate({
//      cacheName: 'static-resources',
//    }),
//  );
//
//  workbox.routing.registerRoute(
//    /\.(?:png|gif|jpg|jpeg|svg)$/,
//    workbox.strategies.cacheFirst({
//      cacheName: 'images',
//      plugins: [
//        new workbox.expiration.Plugin({
//          maxEntries: 60,
//          maxAgeSeconds: 30 * 24 * 60 * 60, // 30 Days
//        }),
//      ],
//    }),
//  );
//
//  workbox.routing.registerRoute(
//    new RegExp('https://fonts.(?:googleapis|gstatic).com/(.*)'),
//    workbox.strategies.cacheFirst({
//      cacheName: 'googleapis',
//      plugins: [
//        new workbox.expiration.Plugin({
//          maxEntries: 30,
//        }),
//      ],
//    }),
//  );
//} else {
//  console.log(`Boo! Workbox didn't load 😬`);
//}
//self.addEventListener('push', function(event) {
//  var message = JSON.parse(event.data.text()); //
//  event.waitUntil(
//    self.registration.showNotification(message.title, {
//      body: message.body,
//    })
//  );
//});
// Register event listener for the 'push' event.
self.addEventListener('push', function (event) {
    // Retrieve the textual payload from event.data (a PushMessageData object).
    // Other formats are supported (ArrayBuffer, Blob, JSON), check out the documentation
    // on https://developer.mozilla.org/en-US/docs/Web/API/PushMessageData.
    const eventInfo = event.data.text();
    const data = JSON.parse(eventInfo);
    const head = data.head || 'New Notification 🕺🕺';
    const body = data.body || 'This is default content. Your notification didn\'t have one 🙄🙄';

    // Keep the service worker alive until the notification is created.
    event.waitUntil(
        self.registration.showNotification(head, {
            body: body,
            icon: 'https://i.imgur.com/MZM3K5w.png'
        })
    );
});