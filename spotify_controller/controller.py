import errno
import tempfile
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from .env import *

class TokenManager:
    def __init__(self, auth_manager, refresh_token):
        self.refresh_token = refresh_token
        self.auth_manager = auth_manager
        self.token_info = None

    def get_access_token(self):
        if self.token_info is None or self.auth_manager.is_token_expired(self.token_info):
            self.token_info = self.auth_manager.refresh_access_token(self.refresh_token)
        return self.token_info["access_token"]

class SpotifyController:
    def _find_device(self):
        for device in self.sp.devices()["devices"]:
            if device["name"] == "car_raspotify":
                return device["id"]
        return None

    def __init__(self):
        # spotipy uses cache to save the access token (on refresh_access_token) and it can't be disabled
        # since we don't care about this cache just use a temp file
        tmp_cache = tempfile.NamedTemporaryFile()

        scope = "user-library-read user-read-playback-state user-modify-playback-state user-read-currently-playing user-read-private"
        redirect_uri = "http://localhost"
        auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=redirect_uri, open_browser=False, cache_path=tmp_cache.name)
        self.sp = spotipy.Spotify(auth_manager=TokenManager(auth_manager, REFRESH_TOKEN))

        self.device_id = None
        while self.device_id is None:
            self.device_id = self._find_device()

    def get_progress_ms(self):
        return self.sp.currently_playing()["progress_ms"]

    def seek_track(self, progress_ms):
        if progress_ms > 0:
            self.sp.seek_track(progress_ms)
    
    def play(self):
        self.sp.transfer_playback(self.device_id)

    def pause(self):
        self.sp.pause_playback(self.device_id)

    def next(self):
        self.sp.next_track(self.device_id)

    def prev(self):
        self.sp.previous_track(self.device_id)
        
    def cur_playing(self):
        return self.sp.currently_playing()
