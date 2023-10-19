# Importing Libraries
from googleapiclient.discovery import build
import pandas as pd

def getChannelStats(youtube, channel_ids):
    all_data = []
    request = youtube.channels().list(
        part='snippet,contentDetails,statistics',
        id=','.join(channel_ids)
    )
    response = request.execute()
    # Check the JSON object here : print(response)

    for i in range(len(response['items'])):
        data = dict(Channel_name=response['items'][i]['snippet']['title'],
                    Subscribers=response['items'][i]['statistics']['subscriberCount'],
                    Views=response['items'][i]['statistics']['viewCount'],
                    Total_videos=response['items'][i]['statistics']['videoCount'],
                    Playlist_id=response['items'][i]['contentDetails']['relatedPlaylists']['uploads']
                    )
        all_data.append(data)

    df = pd.DataFrame(all_data)
    return df

def getVideoIDs(youtube, playlist_id):
    video_ids = []

    request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,
        maxResults=50
    )
    response = request.execute()
    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])

    next_page_token = response.get('nextPageToken')
    more_pages = True
    while more_pages:
        if next_page_token is None:
            more_pages = False
        else:
            request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=next_page_token
            )
            response = request.execute()
            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])
            next_page_token = response.get('nextPageToken')

    return len(video_ids), video_ids

def getVideoDetails(youtube, video_ids):
    all_video_stats = []

    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part='snippet, statistics',
            id=','.join(video_ids[i:i + 50])
        )
        response = request.execute()

        for video in response['items']:
            try:
                video_stats = dict(Title=video['snippet']['title'],
                                  Published_date=video['snippet']['publishedAt'],
                                  Views=video['statistics']['viewCount'],
                                  Likes=video['statistics']['likeCount'],
                                  Comments=video['statistics']['commentCount']
                                  )
            except:
                video_stats = dict(Title=video['snippet']['title'],
                                  Published_date=video['snippet']['publishedAt'],
                                  Views=video['statistics']['viewCount'],
                                  )

            all_video_stats.append(video_stats)

        df = pd.DataFrame(all_video_stats)
    return df

def getComments(youtube, video_id):
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    )
    response = request.execute()

    comments = []

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append([
            comment['authorDisplayName'],
            comment['publishedAt'],
            comment['updatedAt'],
            comment['likeCount'],
            comment['textDisplay']
        ])

    df = pd.DataFrame(comments, columns=['author', 'published_at', 'updated_at', 'like_count', 'text'])
    return df


if __name__ == '__main__':
    # Generating API key
    api_key = 'AIzaSyDEVuXP9UsT-Ozc-HXlfaoDboR07Fo7gU0'

    # Setting up the YT Data API Client
    api_service_name = "youtube"
    api_version = "v3"
    youtube = build(api_service_name, api_version, developerKey=api_key)

    # Getting sample YT Channel IDs
    channel_ids = ['UCSyOPVc6Bwltnwu1BjcT0eg',  # SSNinstitutions
                   'UChKQYI9z5rO_sdNjhwyyjSg',  # SideSerfCakes
                   'UCZSNzBgFub_WWil6TOTYwAg',  # NetflixIndiaOfficial
                   'UCQYMhOMi_Cdj1CEAU-fv80A'  # nesoacademy
                   ]

    # Getting Channel Statistics
    channels_data = getChannelStats(youtube, channel_ids)
    print('\nChannel\'s Data :\n', channels_data)

    # Getting Video IDs
    playlist_id = channels_data.loc[channels_data['Channel_name'] == 'Neso Academy', 'Playlist_id'].iloc[0]
    n_videos, video_ids = getVideoIDs(youtube, playlist_id)
    print('Total number of videos in \'uploads\' playlist (', playlist_id, ') :', n_videos)

    # Getting Video Details
    video_details = getVideoDetails(youtube, video_ids)
    print('\n\nVideo Details : ', video_details)

    # Getting Comments
    selected_video_id = video_ids[4]
    comments = getComments(youtube, selected_video_id)
    print(f'\n\nComments from the video "{selected_video_id}" :\n', comments)
