from AARVIMUSIC.core.bot import AARVI
from AARVIMUSIC.core.dir import dirr
from AARVIMUSIC.core.git import git
from AARVIMUSIC.core.userbot import Userbot
from AARVIMUSIC.misc import dbb, heroku
from pyrogram import Client
from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = AARVI()
api = SafoneAPI()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
