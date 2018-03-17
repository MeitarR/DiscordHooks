# -*- coding: utf-8 -*-
import json
import logging
import requests

from .embed import BaseSerializable, Embed, datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


def encode_complex(obj):
    if isinstance(obj, BaseSerializable):
        return obj.dict
    elif isinstance(obj, datetime):
        return obj.isoformat()

    raise TypeError(repr(obj) + " is not JSON serializable")


class Hook:
    """Represent the webhook according to Discord Developer Documentation

    WebHooks are a low-effort way to post messages to channels in Discord.
    They do not require a bot user or authentication to use.
    for more info you can read here:
    https://discordapp.com/developers/docs/resources/webhook#execute-webhook-jsonform-params

    Note:
        Discord webhook must include at least one of content, file, embeds

    Attributes:
        hook_url (str): The url which the data will be sent to. Mostly in this format:
            https://discordapp.com/api/webhooks/{webhook.id}/{webhook.token}
        content (str): The message contents (up to 2000 characters).
        username (str): Override the default username of the webhook.
        avatar_url (str): Override the default avatar of the webhook.
        tts (bool): True if this is a Text-To-Speech message.
        file (bytes): The contents of the file being sent.
        embeds ([Embed]): List of embed objects being sent.
    """
    __items__ = ('content', 'username', 'avatar_url', 'tts', 'file', 'embeds')

    def __init__(self, hook_url: str = None, content: str = None, username: str = None, avatar_url: str = None,
                 tts: bool = False, file: bytes = None, embeds: [Embed] = None):
        """Initiate the Hook object

        Args:
            hook_url (str): The url which the data will be sent to.
            content (str): The message contents (up to 2000 characters).
            username (str): Override the default username of the webhook.
            avatar_url (str): Override the default avatar of the webhook.
            tts (bool): True if this is a Text-To-Speech message.
            file (bytes): The contents of the file being sent.
            embeds ([Embed]): List of embed objects being sent.
        """
        self.hook_url = hook_url

        self.content = content
        self.username = username
        self.avatar_url = avatar_url
        self.tts = tts
        self.file = file
        self.embeds = embeds

    @property
    def hook_url(self) -> str:
        """str: The url which the data will be sent to."""
        return self._hook_url

    @hook_url.setter
    def hook_url(self, hook_url: str):
        if hook_url is not None and not isinstance(hook_url, str):
            raise TypeError('hook_url must be string')
        self._hook_url = hook_url

    @property
    def content(self) -> str:
        """str: The message contents (up to 2000 characters)."""
        return self._content

    @content.setter
    def content(self, content: str):
        if content is not None and not isinstance(content, str):
            raise TypeError('content must be string')
        if content is not None and len(content) > 2000:
            raise ValueError('content length must be up to 2000 characters')
        self._content = content

    @property
    def username(self) -> str:
        """str: Override the default username of the webhook."""
        return self._username

    @username.setter
    def username(self, username: str):
        if username is not None and not isinstance(username, str):
            raise TypeError('username must be string')
        self._username = username

    @property
    def avatar_url(self) -> str:
        """str: Override the default avatar of the webhook."""
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url: str):
        if avatar_url is not None and not isinstance(avatar_url, str):
            raise TypeError('avatar_url must be string')
        self._avatar_url = avatar_url

    @property
    def tts(self) -> bool:
        """bool: True if this is a Text-To-Speech message."""
        return self._tts

    @tts.setter
    def tts(self, tts: bool):
        if not isinstance(tts, bool):
            raise TypeError('tts must be bool')
        self._tts = tts

    @property
    def file(self) -> bytes:
        """bytes: The contents of the file being sent."""
        return self._file

    @file.setter
    def file(self, file: bytes):
        self._file = file

    @property
    def embeds(self) -> [Embed]:
        """[Embed]: List of embed objects being sent."""
        return self._embeds

    @embeds.setter
    def embeds(self, embeds: [Embed]):
        if embeds is None:
            self._embeds = []
            return
        if not isinstance(embeds, list):
            raise TypeError('embeds must be list')
        self._embeds = []
        for embed in embeds:
            if isinstance(embed, Embed):
                self._embeds.append(embed)
            elif isinstance(embed, dict):
                self._embeds.append(Embed.from_dict(embed))
            else:
                raise TypeError('embeds items must be Embed or dict')

    @property
    def json(self) -> str:
        """str: Generate json string of the webhook to be sent to the server"""
        data = {key: getattr(self, key) for key in self.__items__ if getattr(self, key) is not None}

        if not (data.get('content') or data.get('file') or data.get('embeds')):
            raise AttributeError('You cant post an empty payload.')

        return json.dumps(data, default=encode_complex)

    def execute(self, hook_url: str = None, json_obj: str = None):
        """Execute the webhook (sending the message)

        Note:
            The arguments are optional.
            You may use them if you didn't specify them before.

            So for example you can create Hook without hook_url;
            and then use this function with some different hook_urls.

        Args:
            hook_url (str): The url which the data will be sent to.
            json_obj (str): The json string that will be sent.
        """
        if not (hook_url or self.hook_url):
            raise AttributeError('hook_url is not set')
        elif hook_url is None:
            hook_url = self.hook_url

        if not (json_obj or self.json):
            raise AttributeError('json_obj is not set')
        elif json_obj is None:
            json_obj = self.json

        result = requests.post(hook_url, data=json_obj, headers={'Content-Type': 'application/json'})

        if 200 <= result.status_code <= 299:
            logger.info("Hook sent successfully. Code: {}".format(result.status_code))
        else:
            logger.debug(result.content)
            logger.error("Error while sending the Hook. ERROR {}: '{}'".format(result. status_code, result.content))
