import config
import base64
from requests import post, get
import obs

def get_current_track():
    url = 'https://api.spotify.com/v1/me/player/currently-playing'

    token = config.util.prompt_for_user_token(
        config.SPOTIFY_USERNAME,
        config.SPOTIFY_SCOPE_CP,
        config.SPOTIFY_CLIENT_ID,
        config.SPOTIFY_CLIENT_SECRET,
        config.SPOTIFY_REDIRECT_URI)

    sp = config.spotipy.Spotify(auth=token)
    currentsong = sp.currently_playing()

    #print(currentsong)

    artists = ""
    first = True

    orig_al = currentsong['item']['artists']
    images = currentsong['item']['album']['images']
    is_playing = currentsong['is_playing']

    image_url = ""

    for image in images:
        if image['height'] == 64:
            image_url = image['url']

    for x in orig_al:
        if not first:
            artists += ", "
        artists += x['name']
        first = False

    
    songinfo = {
        'name':currentsong['item']['name'],
        'artists': artists,
        'image_url': image_url,
        'is_playing': is_playing,
        'time_left': currentsong['item']['duration_ms']-currentsong['progress_ms']
    }

    return songinfo

def toggle_obs(visibility):
    obs.toggle_source_visibility(config.TOP_OF_SCREEN, "Top of Screen - Spotify", visibility)

def update_obs():
    songinfo = get_current_track()
    path = "./Spotify Info/"

    toggle_obs(False)

    config.time.sleep(1)

    config.urllib.request.urlretrieve(songinfo['image_url'], path + "current_song.jpg")

    artist_file = path + "Artists.txt"
    song_file = path + "Song Name.txt"

    with open(artist_file, 'w') as file:
        file.write(songinfo['artists'])

    with open(song_file, 'w') as file:
        file.write(songinfo['name'])

    config.time.sleep(config.SLEEP_TIME)

    toggle_obs(True)

def loop_songs():

    songinfo = get_current_track()
    current_song = songinfo['name']
    config.time.sleep(songinfo['time_left']/1000)

    while True:
        songinfo = get_current_track()

        if(current_song != songinfo['name']):
            update_obs()

        config.time.sleep(songinfo['time_left']/1000)

def ping():
    try:
        url = 'https://api.spotify.com/v1/me/player/currently-playing'

        token = config.util.prompt_for_user_token(
            config.SPOTIFY_USERNAME,
            config.SPOTIFY_SCOPE_CP,
            config.SPOTIFY_CLIENT_ID,
            config.SPOTIFY_CLIENT_SECRET,
            config.SPOTIFY_REDIRECT_URI)

        sp = config.spotipy.Spotify(auth=token)
        currentsong = sp.currently_playing()

        orig_al = currentsong['item']['artists']

        return True
    except Exception as e:
        return False

if __name__ == "__main__":
    #get_current_track()
    
    config.init()
    print(get_current_track())
    #loop_songs()
    #update_obs()

    #get_time_played()