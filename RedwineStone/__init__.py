from RedwineStone.core.bot import Sang
from RedwineStone.core.dir import dirr
from RedwineStone.core.git import git
from RedwineStone.core.userbot import Userbot
from RedwineStone.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Sang()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()


# © Sangram
