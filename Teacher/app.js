// Main

var koa = require('koa'),
	router = require('koa-router');

var app = koa();

// Routing
app.use(router(app));

// Timestamp Logging
app.use(function* timeStamper(next) {
	var t = new Date().getTime();

	yield next; // Defer till later (during Upstream)

	var t_a = new Date().getTime();
	var difference = t_a - t;
	console.log("Request length: " + difference + "ms");
});

//

console.log('Server started...');

try {
 app.listen(3001);
} catch(e) {
	console.log(e);
}