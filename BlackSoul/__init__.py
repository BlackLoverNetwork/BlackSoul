#
# Copyright (C) 2021-2022 by BlackLoverNetwork@Github, < https://github.com/BlackLoverNetwork >.
#
# This file is part of < https://github.com/BlackLoverNetwork/BlackSoul > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/BlackLoverNetwork/BlackSoul/blob/master/LICENSE >
#
# All rights reserved.

from BlackSoul.core.bot import YukkiBot
from BlackSoul.core.dir import dirr
from BlackSoul.core.git import git
from BlackSoul.core.userbot import Userbot
from BlackSoul.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = YukkiBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
