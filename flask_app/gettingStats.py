

from urllib.parse import urlparse, parse_qs
from apiclient.discovery import build

def getting_statistics(id, api):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.

    # Get credentials and create an API client
    youtube = build('youtube', 'v3', developerKey=api)

    request = youtube.videos().list(
        part="statistics",
        id=id
    )
    
    response = request.execute()
    importantInfo = response['items'][0]['statistics']
    # print(importantInfo)
    return importantInfo
    # return response


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
    info = getting_statistics(id, api_key)
    print(info)