self.addEventListener("push", event => {
  console.log("Notification");
  self.registration.showNotification("header", {body: "body",});
});
self.addEventListener('sync', function(event) {
  if (event.tag == 'myFirstSync') {
    console.log("event");
    getUpdate();
    event.waitUntil(getUpdate());
  }
});
