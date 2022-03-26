import os


class Config:
    @property
    def spotify_client_id(self) -> str:
        client_id = os.getenv('SPOTIFY_CLIENT_ID')
        if client_id is None:
            raise Exception('empty spotify client id')
            
        return client_id

    @property
    def spotify_client_secret(self) -> str:
        client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        if client_secret is None:
            raise Exception('empty spotify client secret')
        
        return client_secret

    @property
    def spotify_redirect_uri(self) -> str:
        redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')
        if redirect_uri is None:
            raise Exception('empty spotify redirect uri')
        
        return redirect_uri

    @property
    def yandex_music_token(self) -> str:
        token = os.getenv('YANDEX_MUSIC_TOKEN')
        if token is None:
            raise Exception('empty yandex music token')

        return token
