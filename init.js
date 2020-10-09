require('dotenv').config();
(function () {

    var config = {};
    this.start = function () {
        //Initiat logger
        global.log = log;
    };

    this.setLoggerId = function (logId) {
        global.logId = logId;
    }


    var lastLoggedTime = null;
    var lastLoggerId = null;
    var log = function (message) {        
        var loggerId = global.logId ? global.logId: '';
        if (lastLoggerId == null || lastLoggerId != loggerId) {
            lastLoggedTime = null;
        }
        lastLoggerId = loggerId;

        if (message == undefined) {
            message = "";
        }

        if ((!!message) && (message.constructor === Object)) {
            message = JSON.stringify(message);
        }


        console.log("\n" +
            "LogId:" + loggerId + "\n" +
            "TimeStamp:" + timeStamp() + "\n" +
            "Message:" + message);


    };

    var addZero = function (x, n) {
        while (x.toString().length < n) {
            x = "0" + x;
        }
        return x;
    };

    var timeStamp = function () {
        var diff = 0;
        if (lastLoggedTime == null) {
            lastLoggedTime = new Date();
        }

        var d = new Date();
        diff = d.getTime() - lastLoggedTime.getTime();
        lastLoggedTime = d;
        var h = addZero(d.getHours(), 2);
        var m = addZero(d.getMinutes(), 2);
        var s = addZero(d.getSeconds(), 2);
        var ms = addZero(d.getMilliseconds(), 3);
        return h + ":" + m + ":" + s + ":" + ms + "[Diff (MS): " + diff + "]";

    };

}).apply(module.exports);