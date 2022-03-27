import spotipy
from spotipy import SpotifyOAuth
from spotipy.cache_handler import MemoryCacheHandler
from yandex_music import Client

from config import Config
from spotify.spotify import SpotifyWrapper
from yandexmusic.yandex_music import YandexMusicWrapper


def main():
    config = Config()
    spotify = SpotifyWrapper(
        client=spotipy.Spotify(client_credentials_manager=SpotifyOAuth(
            client_id=config.spotify_client_id,
            client_secret=config.spotify_client_secret,
            redirect_uri=config.spotify_redirect_uri,
            scope='user-library-read,playlist-read-collaborative,playlist-read-private',
            cache_handler=MemoryCacheHandler()))
    )

    yam = YandexMusicWrapper(Client(config.yandex_music_token).init())

    for spotify_playlist in spotify.get_playlists():
        print(f'Adding {spotify_playlist.name}')

        yandex_playlist = yam.create_playlist(spotify_playlist.name)

        for spotify_track in spotify_playlist.tracks:
            artists = ' '.join(map(lambda artist: artist.name, spotify_track.artists))
            track_name = f'{spotify_track.title} {artists}'

            attempt_count = 1
            while attempt_count <= 3:
                try:
                    yandex_track = yam.search_track(track_name)
                    yandex_playlist = yam.add_to_playlist(yandex_playlist, yandex_track)
                    break
                except TypeError:
                    print(f'Can\'t found track: "{track_name}" to add to playlist "{spotify_playlist.name}"')
                    break
                except Exception as e:
                    print(f'Something went wrong... Attempt {attempt_count} {e}')
                
                attempt_count += 1
    
    spotify_playlist = spotify.get_saved_tracks()
    print(f'Adding {spotify_playlist.name}')
    
    for spotify_track in spotify_playlist.tracks:
        artists = ' '.join(map(lambda artist: artist.name, spotify_track.artists))
        track_name = f'{spotify_track.title} {artists}'

        attempt_count = 1
        while attempt_count <= 3:
            try:
                yandex_track = yam.search_track(track_name)
                yandex_playlist = yam.like_track(yandex_track)
                break
            except TypeError:
                print(f'Can\'t found track: "{track_name}" to add to playlist "{spotify_playlist.name}"')
                break
            except Exception as e:
                print(f'Something went wrong... Attempt {attempt_count} {e}')
                
            attempt_count += 1


if __name__ == '__main__':
    main()
