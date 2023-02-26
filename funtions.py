from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup , CallbackQuery
from main import *
from dotenv import load_dotenv
import requests

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
TOKEN = os.getenv("TOKEN")


app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

def artist_info(token, artist_id):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"https://api.spotify.com/v1/artists/{artist_id}", headers=headers)
    artist = response.json()
    if response.status_code == 200:
        return response.json()
    else:
        return None

def track_info(token, track_id):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"https://api.spotify.com/v1/tracks/{track_id}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


@app.on_message(filters.private & filters.command("start"))
def start(client, message):
    client.send_chat_action(message.from_user.id, enums.ChatAction.TYPING)
    message.reply("""👋 Hey there! 👋

🎵 To download a single song, send me the name of the song or artist.

Just let me know what you need and I'll do my best to assist you - @qanagattandrylmagandyktarynyzdan

🎶 Let's get started! 🎶""")


@app.on_message(filters.private & ~filters.command("download"))
def search_track(client, message):
    track_name = message.text

    token = get_token()

    track = search_for_track(token, track_name)
    if track is None:
        client.send_message(message.from_user.id, "No results found")
        return

    inline_keyboard = []
    for song in track:
        track_id = song['id']
        artist_id = song['artists'][0]['id']
        button = InlineKeyboardButton(
            f"{song['name']} - {song['artists'][0]['name']}",
            callback_data=f"download|{track_id}|{artist_id}")
        inline_keyboard.append([button])
    message.reply("Choose a song to download:", reply_markup=InlineKeyboardMarkup(inline_keyboard))


@app.on_callback_query()
def callback_query_handler(client: Client, callback_query: CallbackQuery):
    query_data = callback_query.data.split("|")
    query_type = query_data[0]

    if query_type == "download":

        token = get_token()
        track_id = query_data[1]
        artist_id = query_data[2]
        track = track_info(token, track_id)
        artist = artist_info(token, artist_id)
        if track is None or artist is None:
            client.send_message(callback_query.from_user.id, "Error occurred while fetching track information")
            return

        query = f"{track['name']} {artist['name']} audio"
        url = get_youtube_url(query)

        if url is None:
            client.send_message(callback_query.from_user.id, "No results found")
            return


        track_name = f"{track['name']} - {artist['name']}"
        try:
            download_track(url, f"{track_name}.mp3")
            client.send_chat_action(callback_query.from_user.id, enums.ChatAction.UPLOAD_AUDIO)
            client.send_audio(callback_query.from_user.id, f"{track_name}.mp3", performer=artist['name'], title=track['name'], caption=f"🎵 {track_name} 🎵")
            os.remove(f"{track_name}.mp3")
        except OSError as os_error:
            download_track(url, f"{callback_query.from_user.id}.mp3")
            client.send_chat_action(callback_query.from_user.id, enums.ChatAction.UPLOAD_AUDIO)
            client.send_audio(callback_query.from_user.id, f"{callback_query.from_user.id}.mp3", performer=artist['name'], title=track['name'], caption=f"🎵 {track_name} 🎵")
            os.remove(f"{callback_query.from_user.id}.mp3")
        
if __name__ == "__main__":
    app.run()

