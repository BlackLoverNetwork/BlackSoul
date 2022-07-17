#
# Copyright (C) 2021-2022 by BlackLoverNetwork@Github, < https://github.com/BlackLoverNetwork >.
#
# This file is part of < https://github.com/BlackLoverNetwork/BlackSoul > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/BlackLoverNetwork/BlackSoul/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters

import config
from strings import get_command
from BlackSoul import app
from BlackSoul.misc import SUDOERS
from BlackSoul.utils.database import autoend_off, autoend_on
from BlackSoul.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**Usage:**\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "Auto End Stream Enabled.\n\nBot will leave voice chat automatically after 3 mins if no one is listening with a warning message.."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("Auto End Stream Disabled.")
    else:
        await message.reply_text(usage)
