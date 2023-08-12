window.addEventListener('load', async () => {
  if ('serviceWorker' in navigator) {
    try {
      const reg = await navigator.serviceWorker.register('/sw.js')
      console.log('Service worker register success', reg)
    } catch (e) {
      console.log('Service worker register fail')
    }
  }

})
if ('serviceWorker' in navigator && 'SyncManager' in window) {
  navigator.serviceWorker.ready.then(function(reg) {
    console.log('create myFirstSync')
    return reg.sync.register('myFirstSync');
  }).catch(function() {
    // system was unable to register for a sync,
    // this could be an OS-level restriction
    getUpdate();
  });
} else {
  // serviceworker/sync not supported
  getUpdate();
}
function notifyMe(header, body) {
    Notification.requestPermission(function(result) {
      if (result === 'granted') {
        navigator.serviceWorker.ready.then(function (registration) {
            registration.showNotification(header, {body: body,});
        });
      }
    });
};
function getUpdate(){
$.ajax({
    url: '/notify/',         /* Куда отправить запрос */
    method: 'get',             /* Метод запроса (post или get) */
    dataType: 'json',          /* Тип данных в ответе (xml, json, script, html). */
    date: {data: "data"},
    success: function(data){   /* функция которая будет выполнена после успешного запроса.  */
        $.each(data, function(i, item) {
            date = Date.parse(item.datetime_notify);
            window.addEventListener('push');
            var today = new Date();
            if (date < today) {
                if (item.shown != true) {
                    notifyMe(item.header, item.body);
                    $.ajax({
                      url: '/notify/shown_notify/'+i,
                      method: 'get',
                    })
                }
            }
        });
    }
});
notifyMe('item.header', 'item.body');
}
setInterval('getUpdate', 5000);
