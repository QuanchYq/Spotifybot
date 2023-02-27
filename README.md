# Spotify Bot 

Telegram bot to download any type of music from Youtube using Spotify API for analyzing and searching.

## What this bot can do?

This bot allows users to search for and download songs from Spotify using the artist or song name. It leverages the Spotify API and YouTube to find and download the desired track, and then sends it as an audio file to the user.

## Features

- Download MP3 files of songs from Spotify
- Search for tracks by name or artist
- Preview search results and choose the track you want to download
- Sends audio files directly to your Telegram account


## Installation

To use this bot, you will need to create a Spotify Developer account and set up a Spotify app. Then, create a `.env` file with the following contents:

- `API_ID`: Your Telegram API ID. You can obtain this value by creating a new application in the [Telegram API Development Tools](https://my.telegram.org/auth?to=apps) page.

- `API_HASH`: Your Telegram API hash. You can obtain this value from the same page where you obtained your API ID.

- `TOKEN`: Your Telegram bot token. You can obtain this value by talking to [BotFather](https://t.me/botfather) and creating a new bot.

- `SPOTIFY_CLIENT_ID`: Your Spotify application client ID. You can obtain this value by creating a new application in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/login).

- `SPOTIFY_CLIENT_SECRET`: Your Spotify application client secret. You can obtain this value from the same page where you obtained your client ID.

- `YOUTUBE_API_KEY`: Your YouTube Data API v3 key. You can obtain this value by creating a new project in the [Google Cloud Console](https://console.cloud.google.com/welcome?project=planar-door-378406), enabling the YouTube Data API v3, and creating a new API key.

Next, install the required dependencies by running:

``` 
pip install -r requirements.txt

```
Finally , run this bot:
```
python funtion.py

```

#Deployment

<p align="center">
  <a href="https://heroku.com/deploy?template=https://github.com/gsoosk/TelegramSpotifyDownloader/tree/heroku">
    <img src="https://www.herokucdn.com/deploy/button.svg" width="300">
  </a>
</p>


## 🔗 Links
[![linkeddin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aikyn-urazalinov-4a9a35225/)
[![telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/PySpotiBot)

## Feedback

If you have any feedback, please reach out to us at aikyn.baurzhanovich99@gmail.com
