from .library import *

admin_user_id = 6864201346 #<--- آیدی ادمین
api_id = 28154690 #<--- آی پی آی آیدی
api_hash = '48e335fa46cfeab2fecd0129b47c1a9e' #<--- ای پی آی هش
helper_username = 'dragonrangerBot' #<--- یوزر ربات هلپر بدون @
bot_token = '7768076075:AAFkhzSxYYyKCG3PCOkcLWCR6Y3SNrwRBMw' #<--- توکن ربات هلپر

client_id = '01e7dc6b41c3471b94efe87abeb05919'
client_secret = '4f5f93af1ced4b0d9ba8440606803639'

client = TelegramClient('TRself-MT', api_id, api_hash)
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
