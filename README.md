# DiscordHooks
A python module for easily execute discord webhooks with embeds and more
## Examples
```python
from DiscordHooks import Hook, Embed, EmbedAuthor, Color
from datetime import datetime

webhook = 'your webhook url from discord'

embed = Embed(title='look here', url='https://github.com/MeitarR', description="some embed text here :pencil:",
              timestamp=datetime.now(), color=Color.Aqua, author=EmbedAuthor(name="Meitar"))

Hook(hook_url=webhook, username="Meitar's webhook",
     avatar_url='https://avatars1.githubusercontent.com/u/14138694',
     content="Hello there! \U0001f62e", embeds=[embed]).execute()
```
![](https://i.snag.gy/xUHvqs.jpg)