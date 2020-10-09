var Sentiment = require('sentiment');

this.getSentiment = function(comments){
    var sentiment = new Sentiment();
    return  sentiment.analyze(comments);
}