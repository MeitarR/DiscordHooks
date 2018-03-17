# -*- coding: utf-8 -*-
"""DiscordHooks - Discord WebHooks wrapper for Python

A python module for creating and executing
Discord WebHooks with emblems and more easily.

GitHub:
    https://github.com/MeitarR/DiscordHooks

Example:
    (for more examples look at the github page)

    from DiscordHooks import Hook, Embed, EmbedAuthor, Color
    from datetime import datetime

    webhook = 'your webhook url from discord'

    embed = Embed(title='look here', url='https://github.com/MeitarR', description="some embed text here :pencil:",
                  timestamp=datetime.now(), color=Color.Aqua, author=EmbedAuthor(name="Meitar"))

    Hook(hook_url=webhook, username="Meitar's webhook",
         avatar_url='https://avatars1.githubusercontent.com/u/14138694',
         content="Hello there! \U0001f62e", embeds=[embed]).execute()

"""

from .hook import Hook
from .embed import Embed, EmbedAuthor, EmbedField, EmbedFooter, EmbedImage, EmbedThumbnail, Color
