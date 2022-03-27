from yandex_music import Client, Playlist

from .track import Track


class YandexMusicWrapper:
    def __init__(self, client: Client):
        self._client = client

    def create_playlist(self, title: str) -> Playlist:
        return self._client.users_playlists_create(title)

    def add_to_playlist(self, playlist: Playlist, track: Track) -> Playlist:
        return playlist.insert_track(track_id=int(track.id), album_id=int(track.album_id))
    
    def like_track(self, track: Track) -> bool:
        return self._client.users_likes_tracks_add(track_ids=int(track.id))

    def search_track(self, query) -> Track:
        track = self._client.search(query).tracks['results'][0]
        track_id = track['id']
        album_id = track['albums'][0]['id']

        return Track(id=track_id, album_id=album_id)
