
from urllib.parse import urlparse, parse_qs
import datetime

# import pkg_resources
# pkg_resources.require("google-api-python-client")
from apiclient.discovery import build
from csv import writer

def get_channel_id(api_key, part, videoId):
    service = build('youtube', 'v3', developerKey=api_key)
    request = service.videos().list(
        part=part,
        id=videoId
    )
    response = request.execute()
    title =  response['items'][0]['snippet']['title']
    description = response['items'][0]['snippet']['description']
    return {
        "title": title,
        "description": description
    }


def video_share_count(channelId,videoId, api_key):
    todayDate = datetime.date.today()
    YouTube = build('youtube', 'v3', developerKey=api_key)
    startDate = YouTube.videos().list(part='snippet', id=id).execute()
    startDate = startDate['items'][0]['snippet']['publishedAt']
    startDate = (startDate.split('T'))[0]
    print(startDate)
    print(todayDate)
    # todayFormatted = Utilities.formatDate(today, 'UTC', 'yyyy-MM-dd')
    # startDateFormatted = Utilities.formatDate(new Date(startDate), 'UTC', 'yyyy-MM-dd')
    API_SERVICE_NAME = 'youtubeAnalytics'
    API_VERSION = 'v2'
    YouTubeAnalytics = build(API_SERVICE_NAME, API_VERSION, developerKey=api_key)
    analyticsResponse = YouTubeAnalytics.reports().query(
        ids=channelId,
        dimensions='video',
        metrics='shares',
        filters=videoId,
        startDate=startDate,
        endDate=todayDate,
    ).execute()
    return analyticsResponse

    # if analyticsResponse.rows:
    #     return analyticsResponse.rows[0][1]
    # else:
    #     return 0

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

    API_SERVICE_NAME = 'youtubeAnalytics'
    API_VERSION = 'v2'
    youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=api_key)
    channelId = get_channel_id(api_key, 'snippet', id)
    lst = {"Name": "Mehmood", "class": "B"}
    lst["title"] = channelId["title"]
    # response =  video_share_count(channelId, id, api_key)
    # print(type(youtube))
    # request = youtube.commentThreads().list(part="snippet", parentId="UC_RjkFugnomSYah5JfDqbkQ")
    # response = get_channel_id(
    #         api_key=api_key,
    #         part='snippet',
    #         videoId=id)


    print(lst)   