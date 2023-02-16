# before importing, you need to run command line: pip install spotipy PyGithub

# Import required libraries
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from github import Github

# Authenticate with Spotify API to retrieve listening history
#resource: https://developer.spotify.com/documentation/general/guides/authorization/app-settings/#:~:text=Client%20ID%2C%20the%20unique%20identifier,Web%20API%20or%20SDK%20calls.

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="08923f56c32e46c1ae4b4ff05260b76f", client_secret="226fd5b07d874db0a61e720c750d646c", redirect_uri="http://my-cool-spotify-project://callback", scope="user-library-read"))
tracks = sp.current_user_saved_tracks()

g = Github("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")
user = g.get_user()
repo = user.get_repos()







