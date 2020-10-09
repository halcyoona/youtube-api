var express = require('express');
var router = express.Router();

var _ = require("underscore");
var init = require('./../../init');
var youtubeRoute = require('./route.js');

var auth = function (req, res, next) {
    init.setLoggerId(_.uniqueId('log_'));
    next();
};

router.use('/', auth, youtubeRoute);

router.use('/', auth, function (req, res) {
    res.send("youtube API V1 running...");
});

module.exports = router;