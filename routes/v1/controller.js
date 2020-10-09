const request = require('request');

const youtubeService = require('../../business/service/youtube');
const e = require('express');
const axios = require('axios');
const fs = require('fs');
const { stringify } = require('querystring');


(function () {

    let _handleError = (req, res, err) => {
        let objResp = {
            message: 'Oops! Something went wrong at our end. Please try again later.',
            statusCode: 500,
            errorCode: 0
        };

        if (res) {
            return res.status(objResp.statusCode).json(objResp);
        }
    };

    this.getVideoAnalytics = function (req, res) {
                
        var initializePromise = youtubeService.newVideoAnalytics('http://54.246.43.67/start', req.params.videoId);
        initializePromise.then(function(context) { 
            // console.log(context);
            // console.log(req.params.videoId);
            // let commentData = context.comments.Comments;
            // console.log(commentData[1]);
            let info = context.info;
            var views = info.viewCount
            var likes = info.likeCount
            var dislikes = info.dislikeCount
            var comments = info.commentCount
            views = views.toLocaleString() ;
            likes = likes.toLocaleString() ;
            dislikes = dislikes.toLocaleString() ;
            comments = comments.toLocaleString() ;
            info.likeCount = likes;
            info.dislikeCount = dislikes;
            info.commentCount = comments;
            info.viewCount = views;
            context.info = info;
            var data = { COMMENT: [ ] };
            for(var i = 0; i < context.comments.Comments.length; ++i)
                data.COMMENT.push({
                    comment:   context.comments.Comments[i],
                    likes: context.comments.LikeCount[i],
                    scores: context.comments.score[i]
                });
            context.comments = data        
            // console.log(context);
            context['videoId'] = req.params.videoId;
            // context['lines'] = '<div><hr><span></span></div>'
            // console.log(context.videoId);
            res.render('youtube/youtube', {context:context});
        });
            // var context; 
            // console.log(response);
            // res.render('youtube/youtube', {context:context});
        
    };


    var response = function (res, statusCode, returnData, message) {
        return res.status(statusCode).send({
            data: returnData,
            message: message ? message : ""
        });
    };

}).apply(module.exports);