import os


class Config:
    @property
    def spotify_client_id(self) -> str:
        return '828b41685b974673b3fd8e5fe373e98d'

    @property
    def spotify_client_secret(self) -> str:
        return '20a3a4ff050c4edaa91abc4e115942f9'

    @property
    def spotify_username(self) -> str:
        username = os.getenv('SPOTIFY_USERNAME')
        if username is None:
            raise Exception('empty username')

        return username

    @property
    def yandex_music_token(self) -> str:
        token = os.getenv('YANDEX_MUSIC_TOKEN')
        if token is None:
            raise Exception('empty yandex music token')

        return token
