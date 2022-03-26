# spotify2yandexmusic
Tool for Migration from Spotify to Yandex Music

## Getting stated
1) Install requirements: `pip3 install -r requirements.txt`
2) Provide environment variables ([see configuration](#configuration))
3) Run application: `python3 ./src/main.py`
4) Log in to the open page in browser
5) Copy the url, paste it into the terminal
6) Ready

## Configuration
```shell
SPOTIFY_CLIENT_ID="your spotify client id"
SPOTIFY_CLIENT_SECRET="your spotify client secret"
SPOTIFY_REDIRECT_URI="your spotify redirect uri"
YANDEX_MUSIC_TOKEN="your yandex music token"
```

### Spotify client id, secret and redirect uri
Go to [dashboard](https://developer.spotify.com/dashboard/) and log in with your account.
Create a new application. Type something in app name and description fields, check the agreements.
Open settings, fill the field "Redirect URIs" with `https://localhost` and press "Add", after press "Save".
Client id will be under the name and app status. To get client secret press the button "Show client secret".

IMPORTANT: Redirect uri must be exactly the same one as in application settings is dashboard.

### Yandex music token
You can get it by clicking on the [link](https://oauth.yandex.ru/authorize?response_type=token&client_id=23cabbbdc6cd418abb4b39c32c41195d).
Pre-enable throttling=`Slow 3G` in the developer tools, 
than you can pull out the authorization token when redirecting.
Copy the url that looks like: 
```
https://music.yandex.ru/#access_token=AgAuX91237GMpF0&token_type=bearer&expires_in=31515252
```
Your token is placed between `access-token=` and `&token_type`.
