from typing import List

from spotipy import Spotify

from .artist import Artist
from .playlist import Playlist
from .track import Track


class SpotifyWrapper:
    def __init__(self, client: Spotify, username: str):
        self._client = client
        self._username = username

    def get_playlists(self) -> List[Playlist]:
        playlists: List[Playlist] = []
        playlists_row = self._client.user_playlists(self._username)

        while playlists_row:
            for playlist in playlists_row['items']:
                playlist_name = str(playlist['name'])
                playlist_id = str(playlist['id'])

                print(f'Extracting playlist: {playlist_name}')

                playlists.append(Playlist(
                    name=playlist_name,
                    id=playlist_id,
                    tracks=self.extract_playlist_tracks(playlist_id)))

            if playlists_row['next']:
                playlists_row = self._client.next(playlists_row)
            else:
                playlists_row = None

        return playlists

    def extract_playlist_tracks(self, playlist_id: str) -> List[Track]:
        tracks: List[Track] = []

        offset = 0
        while True:
            response = self._client.playlist_items(
                playlist_id,
                offset=offset,
                fields='items.track.id,total',
                additional_types=['track']
            )

            if len(response['items']) == 0:
                break

            for item in response['items']:
                tracks.append(self.extract_track_credentials(item['track']['id']))

            offset += len(response['items'])

        return tracks

    def extract_track_credentials(self, track_id: str):
        track = self._client.track(track_id)
        artists = list(map(lambda artist: Artist(id=artist['id'], name=artist['name']), track['artists']))

        return Track(id=track_id, title=track['name'], artists=artists)
