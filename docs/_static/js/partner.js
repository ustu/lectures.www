var blockId = "";
if (window.location.hostname == "lectures.uralbash.ru") {
  blockId = "R-A-231461-1";
} else {
  blockId = "R-A-222712-1";
}

(function(w, d, n, s, t) {
  w[n] = w[n] || [];
  w[n].push(function() {
    Ya.Context.AdvManager.render({
      blockId: blockId,
      renderTo: "yandex-partner",
      horizontalAlign: false,
      async: true
    });
  });
  t = d.getElementsByTagName("script")[0];
  s = d.createElement("script");
  s.type = "text/javascript";
  s.src = "//an.yandex.ru/system/context.js";
  s.async = true;
  t.parentNode.insertBefore(s, t);
})(window, window.document, "yandexContextAsyncCallbacks");

// setTimeout((function googAdSense(d) {
//   var partnerDiv = d.getElementById('yandex-partner');
//   if (!partnerDiv.innerHTML.trim()) {
//     var t = d.getElementsByTagName("script")[0];
//     var s = d.createElement("script");
//     s.type = "text/javascript";
//     s.src = "//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js";
//     s.async = true;
//     t.parentNode.insertBefore(s, t);
//
//     partnerDiv.innerHTML = `
// <ins class="adsbygoogle"
//      style="display:inline-block;width:300px;height:250px"
//      data-ad-client="ca-pub-2884502571619359"
//      data-ad-slot="6348097736"></ins>
// `;
//   }
// })(window.document), 2000);
//
// setTimeout((function () {(adsbygoogle = window.adsbygoogle || []).push({})})(), 2100);
