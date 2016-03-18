http=require('http');
var svr = http.createServer(function(req, resp) {
   var body = "";
  req.on('data', function (chunk) {
    body += chunk;
  });
  req.on('end', function () {
    console.log('body: ' + body);
    var jsonObj = JSON.parse(body);
  console.log(jsonObj.$key);
  })
    resp.end('Hello, World!');
}).listen(8124);

