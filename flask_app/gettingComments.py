
from urllib.parse import urlparse, parse_qs

# import pkg_resources
# pkg_resources.require("google-api-python-client")
from apiclient.discovery import build
from csv import writer


def get_comments(api_key, part='snippet', 
                 maxResults=100, 
                 textFormat='plainText',
                 order='time',
                 videoId='ioNng23DkIM',
                 csv_filename="commentText"):

    #3 create empty lists to store desired information
    comments, commentsId, repliesCount, likesCount, authors= [], [], [], [], []
       
    # build our service from path/to/apikey
    service = build('youtube', 'v3', developerKey=api_key)
    
    #4 make an API call using our service
    response = service.commentThreads().list(
        part=part,
        maxResults=maxResults,
        textFormat=textFormat,
        order=order,
        videoId=videoId
    ).execute()

     

    flag = 1
    while response: # this loop will continue to run until you max out your quota
                 
        for item in response['items']:
            #5 index item for desired data features
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            author_name = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            comment_id = item['snippet']['topLevelComment']['id']
            reply_count = item['snippet']['totalReplyCount']
            like_count = item['snippet']['topLevelComment']['snippet']['likeCount']
            
            #6 append to lists
            comments.append(comment)
            commentsId.append(comment_id)
            repliesCount.append(reply_count)
            likesCount.append(like_count)
            authors.append(author_name)
            
        
        #8 check for nextPageToken, and if it exists, set response equal to the JSON response
        if 'nextPageToken' in response:
            response = service.commentThreads().list(
                part=part,
                maxResults=maxResults,
                textFormat=textFormat,
                order=order,
                videoId=videoId,
                pageToken=response['nextPageToken']
            ).execute()
        else:
            break

    # # return response
    # #9 return our data of interest
    return {
        'Comments': comments,
        'CommentID': commentsId,
        'ReplyCount' : repliesCount,
        'LikeCount' : likesCount,
        'AuthorName': authors
    }




# source:
# https://stackoverflow.com/questions/45579306/get-youtube-video-url-or-youtube-video-id-from-a-string-using-regex
def get_id(url):
    u_pars = urlparse(url)
    quer_v = parse_qs(u_pars.query).get('v')
    if quer_v:
        return quer_v[0]
    pth = u_pars.path.split('/')
    if pth:
        return pth[-1]


if __name__ == "__main__":
    api_key = "AIzaSyB2aP-k5RgREln1UKM1q_QCRrh_JA4sSvM"
    id = get_id('https://www.youtube.com/watch?v=O7SOpGwDVcY')
    # id = get_id('https://www.youtube.com/watch?v=G6QS6HBi2pc')
    # id = get_id('https://www.youtube.com/watch?v=geL6eYSUNvo')
    youtube = build('youtube', 'v3', developerKey=api_key)
    # print(type(youtube))
    # request = youtube.commentThreads().list(part="snippet", parentId="UC_RjkFugnomSYah5JfDqbkQ")
    response = get_comments(
            api_key=api_key,
            part='snippet',
            maxResults=100,
            textFormat='plainText',
            order='time',
            videoId=id)

    print(response)    
    # print(response['Comments'])
    # print(response['CommentID'])
    # print(response['ReplyCount'])
    # print(response['LikeCount'])
    # print(response['AuthorName'])