const request = require('request');
var http = require('http');
const axios = require('axios');
// const fetch = request("fetch");
const sentimentService = require(".././service/sentiment");


this.newVideoAnalytics = async function makeGetRequest(url, videoId) {

  let res = await axios.get(url, {
      params: {
          id: videoId
      }
  });

  let data = res.data;
  return data
}


this.videoAnalytics = function (videoId) {

    // var url = "https://www.googleapis.com/youtube/v3/videos?part=contentDetails,statistics&id=" + videoId + "&key=AIzaSyCZccaLt_5Fa9q9tny4IglH8edDyxgtufo";

    var options = {
        url: url,
        headers: {
            'User-Agent': 'request'
        }
    };

    return new Promise(function (resolve, reject) {
        // Do async job
        request.get(options, function (err, resp, body) {
            if (err) {
                reject(err);
            } else {
                var wrapper  = {summary: JSON.parse(body)};
                resolve(wrapper);
            }
        });
    });
};

this.videoAnalytics_old = function (videoId) {
    var obj = {
        aggrigateComments : "",
        negativeScore : 0,
        positiveScore : 0,
        neutralScore : 0,    
        finalResponse : ""
    };
    var url = "https://www.googleapis.com/youtube/v3/videos?part=contentDetails,statistics&id=" + videoId + "&key=AIzaSyCZccaLt_5Fa9q9tny4IglH8edDyxgtufo";

    var options = {
        url: url,
        headers: {
            'User-Agent': 'request'
        }
    };

    return new Promise(function (resolve, reject) {
        // Do async job
        request.get(options, function (err, resp, body) {
            if (err) {
                reject(err);
            } else {
                //obj.finalResponse= responseHTML(JSON.parse(body));
                obj.finalResponse= JSON.parse(body);
                resolve(obj.finalResponse);
            }
        }).end();
    });/*.then(function (obj) {

    j = 1;
       
        return new Promise((resolve, reject) => {
            var tempResponse = obj.finalResponse;
            var responseHTML = "</br></br>";
            responseHTML = responseHTML + "<b><u>Comments</u></b>";
            responseHTML = responseHTML + "</br></br>";
            
            //finalResponse = finalResponse + responseHTML;
            obj.finalResponse = responseHTML;
            var pageToken = null;
            callCommentAPI(pageToken);
            function callCommentAPI(pageToken) {
                var url = "https://www.googleapis.com/youtube/v3/commentThreads?part=snippet,replies,id&videoId=" + videoId + "&key=AIzaSyCZccaLt_5Fa9q9tny4IglH8edDyxgtufo&maxResults=100";
                if (pageToken != null) {
                    url = url + "&pageToken=" + pageToken
                }

                axios.get(url).then(response => {
                    obj = responseHTMLForComments(response.data, obj);
                    // obj.finalResponse = obj.finalResponse + 
                    pageToken = response.data.nextPageToken;
                    if (pageToken != null) {
                        callCommentAPI(pageToken);
                    } else {
                        var aggrigatedResult = sentimentService.getSentiment(obj.aggrigateComments);
                        obj.finalResponse= "<div><br/><br/><b>Sentiment Analysis Summary</b></br>Positive: "+obj.positiveScore+" </br>Negative: "+obj.negativeScore+"</br> Neutral Comments: "+obj.neutralScore+" </br> Average: "+aggrigatedResult.score+"</div>   <div><br/><br/><b>Sentiment Analysis Details</b></br></div><div>"+JSON.stringify(aggrigatedResult)+"</div></br></br>"+obj.finalResponse;
                        obj.finalResponse = tempResponse +"<div>Comment Count: " + (j-1) + "</div>"+ obj.finalResponse;
                        resolve(obj.finalResponse);
                    }
                })
            }
        });
    });*/
};

// var responseHTML = function (body) {
//     var responseHTML = "<br/>";
//     responseHTML = responseHTML + "<div>Video Id: " + body.items[0].id + "</div>";
//     responseHTML = responseHTML + "<div>Views Count: " + body.items[0].statistics.viewCount + "</div>";
//     responseHTML = responseHTML + "<div>Like Count: " + body.items[0].statistics.likeCount + "</div>";
//     responseHTML = responseHTML + "<div>Dislike Count: " + body.items[0].statistics.dislikeCount + "</div>";
//     //responseHTML = responseHTML + "<div>Comment Count: " + body.items[0].statistics.commentCount + "</div>";
//     responseHTML = "<iframe width='250' height='150' src='https://www.youtube.com/embed/"+body.items[0].id+"?controls=0'></iframe>"+ responseHTML;
//     return responseHTML;
// };

// var responseHTMLForComments = function (body,obj) {
//     var responseHTML = "</br></br>";
//     // responseHTML = responseHTML + "<b><u>Comments</u></b>";
//     // responseHTML = responseHTML + "</br></br>";
//     for (var i in body.items) {
//         responseHTML = responseHTML + "<b><u>Comment: "+j+"</u></b>";
//         j++;
//         responseHTML = responseHTML + "<div>" + body.items[i].snippet.topLevelComment.snippet.textDisplay + "</div>";
//         responseHTML = responseHTML + "<div>Like Count: " + body.items[i].snippet.topLevelComment.snippet.likeCount + "</div>";
//         obj.aggrigateComments = obj.aggrigateComments + " " + body.items[i].snippet.topLevelComment.snippet.textDisplay;
//         var result = sentimentService.getSentiment(body.items[i].snippet.topLevelComment.snippet.textDisplay);
//         if(result.score === 0){
//             obj.neutralScore = obj.neutralScore + 1;
//         }
//         else if(result.score>0){
//             obj.positiveScore = obj.positiveScore + result.score;
//         }else{
//             obj.negativeScore = obj.negativeScore + (result.score*-1);
//         }
//         responseHTML = responseHTML + "</br></br>";
//         responseHTML = responseHTML + "<b>Sentiment Anaalysis</b>";
//         responseHTML = responseHTML + "<div>" + JSON.stringify(result) + "</div>"

//         if(body.items[i].replies){
//             for (var x in body.items[i].replies.comments) {                
//                 responseHTML = responseHTML + "<b><u>Comment: "+j+"</u></b>";
//                 j++;
//                 responseHTML = responseHTML + "<div>" + body.items[i].replies.comments[x].snippet.textDisplay + "</div>";
//                 responseHTML = responseHTML + "<div>Like Count: " + body.items[i].replies.comments[x].snippet.likeCount + "</div>";
//                 obj.aggrigateComments = obj.aggrigateComments + " " + body.items[i].replies.comments[x].snippet.textDisplay;
//                 var result1 = sentimentService.getSentiment(body.items[i].replies.comments[x].snippet.textDisplay);
//                 if(result1.score === 0){
//                     obj.neutralScore = obj.neutralScore + 1;
//                 }
//                 else if(result1.score>0){
//                     obj.positiveScore = obj.positiveScore + result1.score;
//                 }else{
//                     obj.negativeScore = obj.negativeScore + (result1.score*-1);
//                 }
//                 responseHTML = responseHTML + "</br></br>";
//                 responseHTML = responseHTML + "<b>Sentiment Anaalysis</b>";
//                 responseHTML = responseHTML + "<div>" + JSON.stringify(result1) + "</div>"
//             }
//         }
//     }

//     //var aggrigatedResult = sentimentService.getSentiment(aggrigateComments);

//     //responseHTML= "<div><br/><br/><b>Sentiment Analysis Summary</b></br>Positive: "+positiveScore+" </br>Negative: "+negativeScore+"</br> Neutral Comments: "+neutralScore+" </br> Average: "+aggrigatedResult.score+"</div>   <div><br/><br/><b>Sentiment Analysis Details</b></br></div><div>"+JSON.stringify(aggrigatedResult)+"</div></br></br>"+responseHTML;
//     obj.finalResponse= obj.finalResponse + responseHTML;
//     return obj;
// };