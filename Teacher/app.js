// Main

var app = require('koa')(),
	router = require('koa-router')();

// Routing
router.get('/', index);
router.get('/about', about);
// Defined Routes
router.get('/home', function*(next) {
	switch(this.request.method) {
		case 'GET':
			var users = ['Ted', 'Rick', 'Steve'];
			this.body = users;
			break;
		case 'POST':
			this.body = 'Not yet implemented.';
	}
});

app
  .use(router.routes())
  .use(router.allowedMethods());

// Timestamp Logging
app.use(function* timeStamper(next) {
	var t = new Date().getTime();

	yield next; // Defer till later (during Upstream)

	var t_a = new Date().getTime();
	var difference = t_a - t;
	console.log("Request length: " + difference + "ms");
});

// Views
function* index() {
  this.body = "<h1>Hello! This is my home page!</h1>";
}

function* about() {
  this.body = "<h2>This is the ABOUT page.</h2>";
}


try {
 app.listen(3002);
} catch(e) {
	console.log("Error:\n" + e);
}

console.log('Server started...');