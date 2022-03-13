import spotipy
from spotipy import SpotifyClientCredentials
from yandex_music import Client

from config import Config
from spotify.spotify import SpotifyWrapper
from yandexmusic.yandex_music import YandexMusicWrapper


def main():
    config = Config()
    spotify = SpotifyWrapper(
        client=spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
            client_id=config.spotify_client_id,
            client_secret=config.spotify_client_secret)),
        username=config.spotify_username
    )

    yam = YandexMusicWrapper(Client(config.yandex_music_token).init())

    for spotify_playlist in spotify.get_playlists():
        print(f'Adding {spotify_playlist.name}')

        yandex_playlist = yam.create_playlist(spotify_playlist.name)

        for spotify_track in spotify_playlist.tracks:
            artists = ' '.join(map(lambda artist: artist.name, spotify_track.artists))
            track_name = f"{spotify_track.title} {artists}"

            try:
                track = yam.search_track(track_name)
                yandex_playlist = yam.add_to_playlist(yandex_playlist, track)
            except TypeError:
                print(f"Can't found track: '{track_name}' to add to playlist '{spotify_playlist.name}'")
            except Exception as e:
                print(f"Something went wrong... {e}")


if __name__ == '__main__':
    main()
