from dotenv import load_dotenv
load_dotenv()
import os
import base64
from requests import post,get
import json
from googleapiclient.discovery import build
import pytube

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_string_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_string_bytes ), "utf-8")

    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {auth_base64}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {'grant_type': 'client_credentials'}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return token

def get_auth_header(token):
    return {'Authorization': f'Bearer {token}'}

def top_tracks_week(token):
    url = "https://api.spotify.com/v1/browse/new-releases"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)['albums']['items']
    return json_result

def search_for_artist(token, artist_name):
    url = 'https://api.spotify.com/v1/search'
    headers = get_auth_header(token)
    query = f"q={artist_name}&type=artist&limit=10"
    query_url = url + '?' + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)['artists']['items']
    if len(json_result) == 0:
        print("No results found")
        return None
    
    return json_result[0]

def get_songs_for_artist(token, artist_id):
    url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks'
    headers = get_auth_header(token)
    query = 'country=US'
    query_url = url + '?' + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)['tracks']
    return json_result

def search_for_track(token, track_name):
    url = 'https://api.spotify.com/v1/search'
    headers = get_auth_header(token)
    query = f"q={track_name}&type=track&limit=5"
    query_url = url + '?' + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)['tracks']['items']
    if len(json_result) == 0:
        print("No results found")
        return None
    return json_result


def download_track(url, filename):
    youtube = pytube.YouTube(url)
    stream = youtube.streams.first()
    stream.download(filename=filename)

def get_youtube_url(url):
    api_key = os.getenv("YOUTUBE_API_KEY")
    youtube = build('youtube', 'v3', developerKey=api_key)
    search_response = youtube.search().list(
        q=url,
        part='id,snippet',
        maxResults=1
    ).execute()
    if len(search_response['items']) == 0:
        print("No results found")
        return None
    video_id = search_response['items'][0]['id']['videoId']
    return f"https://www.youtube.com/watch?v={video_id}"

   
