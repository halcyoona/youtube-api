var express = require('express');
var router = express.Router();
var controller = require('./controller');

//Here we setup multiple routes
router.route('/video/:videoId/analytics').get(controller.getVideoAnalytics);

module.exports = router;