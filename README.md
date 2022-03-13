# spotify2yandexmusic
Tool for Migration from Spotify to Yandex Music

## Getting stated
1) Install requirements: `pip3 install -r requirements.txt`
2) Provide environment variables ([see configuration](#configuration))
3) Run application: `python3 ./src/main.py`

## Configuration
```shell
SPOTIFY_USERNAME="your or someone else spotify username"
YANDEX_MUSIC_TOKEN="your yandex music token"
```

### Spotify username
Could be found [here](https://www.spotify.com/ru-ru/account/overview/)

### Yandex music token
You can get it by clicking on the [link](https://oauth.yandex.ru/authorize?response_type=token&client_id=23cabbbdc6cd418abb4b39c32c41195d).
Pre-enable throttling=`Slow 3G` in the developer tools, 
than you can pull out the authorization token when redirecting.
Copy the url that looks like: 
```
https://music.yandex.ru/#access_token=AgAuX91237GMpF0&token_type=bearer&expires_in=31515252
```
Your token is placed between `access-token=` and `&token_type`.
