var express = require('express');
//var exphbs  = require('express-handlebars');
//var hbs = require('express-hbs');
var routes = require('./routes/router');
var path = require('path')

var init = require('./init.js');
var app = express();


init.start();
app.use(express.json());
//app.use(express.urlencoded({ extended: false }));

app.set('view engine', 'hbs');
app.set('views', __dirname + '/views');
// app.set('views', __dirname + '/views/youtube/hello.html');
//app.use(express.static(path.join(__dirname, 'public')));
//app.use(express.static("public"));
//app.set('pblic', __dirname + '/public');
//app.use(express.static(__dirname + '/public'));

//app.use(express.static('public'));
// app.set('images', express.static(__dirname + '/public/youtube/app-assets/images/slider'));


// app.set('images', __dirname + '/public/youtube/app-assets/images/slider/');
//app.use(express.static(path.join(__dirname, '/public')));
//app.use('/images', express.static(__dirname + '/public/youtube/app-assets/images/slider/'));

// server.route({
//     method: 'GET',
//     path: '/{filename*}',
//     handler: {
//       directory: {
//         path:    __dirname + '/public',
//         listing: false,
//         index:   false
//       }
//     }
//   });
// app.engine('handlebars', exphbs({defaultLayout: 'youtube'}));
// app.set('view engine', 'handlebars');

//Enable CORS
// app.all('/*', function (req, res, next) {
//     res.header("Access-Control-Allow-Origin", "*");
//     res.header("Access-Control-Allow-Headers", "X-Requested-With");
//     next();
// });

//Adding Routing
app.use('/', routes);

// app.get('/favicon.ico', (req, res) => res.status(204).json({ nope: true }));

//Plz uncomment below 3 lines to run API in local machine.
var port = 3000;
app.listen(port);
console.log("Web Server running on port:" + port);

// Export your Express configuration so that it can be consumed by the Lambda handler
module.exports = app