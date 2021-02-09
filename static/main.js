function sendRequest(url, method, data) {
  var r = axios({
    method: method,
    url: url,
    data: data,
    xsrfCookieName: "csrftoken",
  });
}

var app = new Vue({
  el: "#app",
  data: {
    task: "",
    tasks: [
      {
        title: "One",
      },
      {
        title: "Two",
      },
    ],
  },
});
