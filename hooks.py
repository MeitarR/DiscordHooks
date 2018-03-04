# -*- coding: utf-8 -*-

import json
import logging
import requests

from embed import BaseSerializable, Embed, datetime


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

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


class DiscordWebHook:
    __items__ = ('content', 'username', 'avatar_url', 'tts', 'file', 'embeds')

    def __init__(self, hook_url: str = None, content: str = None, username: str = None, avatar_url: str = None,
                 tts: bool = False, file: bytes = None, embeds: [Embed] = None):
        self.hook_url = hook_url

        self.content = content
        self.username = username
        self.avatar_url = avatar_url
        self.tts = tts
        self.file = file
        self.embeds = embeds

    @property
    def hook_url(self):
        return self._hook_url

    @hook_url.setter
    def hook_url(self, hook_url):
        if hook_url is not None and not isinstance(hook_url, str):
            raise TypeError('hook_url must be string')
        self._hook_url = hook_url

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        if content is not None and not isinstance(content, str):
            raise TypeError('content must be string')
        if content is not None and len(content) > 2000:
            raise ValueError('content length must be up to 2000 characters')
        self._content = content

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if username is not None and not isinstance(username, str):
            raise TypeError('username must be string')
        self._username = username

    @property
    def avatar_url(self):
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        if avatar_url is not None and not isinstance(avatar_url, str):
            raise TypeError('avatar_url must be string')
        self._avatar_url = avatar_url

    @property
    def tts(self):
        return self._tts

    @tts.setter
    def tts(self, tts):
        if not isinstance(tts, bool):
            raise TypeError('tts must be bool')
        self._tts = tts

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, file):
        self._file = file

    @property
    def embeds(self):
        return self._embeds

    @embeds.setter
    def embeds(self, embeds):
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
    def json(self):
        data = {key: getattr(self, key) for key in self.__items__ if getattr(self, key) is not None}

        if not (data.get('content') or data.get('file') or data.get('embeds')):
            raise AttributeError('You cant post an empty payload.')

        return json.dumps(data, default=encode_complex)

    def execute(self, hook_url=None, json_obj=None):
        if not (hook_url or self.hook_url):
            raise AttributeError('hook_url is not set')
        elif not hook_url:
            hook_url = self.hook_url

        if not (json_obj or self.json):
            raise AttributeError('json_obj is not set')
        elif not json_obj:
            json_obj = self.json

        result = requests.post(hook_url, data=json_obj, headers={'Content-Type': 'application/json'})

        if 200 <= result.status_code <= 299:
            logger.info("Payload delivered successfully. Code: {}".format(result.status_code))
        else:
            logger.debug(result.content)
            logger.error("Post Failed, Error {}: '{}'".format(result. status_code, result.content))
