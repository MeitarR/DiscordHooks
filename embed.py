# -*- coding: utf-8 -*-

from datetime import datetime
from abc import ABC, abstractmethod


class Color:
    White = 0xFFFFFF
    Black = 0x111111
    Navy = 0x001f3f
    Blue = 0x0074D9
    Aqua = 0x7FDBFF
    Teal = 0x39CCCC
    Olive = 0x3D9970
    Green = 0x2ECC40
    Lime = 0x01FF70
    Yellow = 0xFFDC00
    Orange = 0xFF851B
    Red = 0xFF4136
    Maroon = 0x85144b
    Fuchsia = 0xF012BE
    Purple = 0xB10DC9
    Gray = 0xAAAAAA
    Silver = 0xDDDDDD


class BaseSerializable(ABC):
    __items__ = ()

    @property
    def dict(self):
        return {key: getattr(self, key) for key in self.__items__}

    @staticmethod
    @abstractmethod
    def from_dict(obj):
        pass


class EmbedFooter(BaseSerializable):

    @staticmethod
    def from_dict(obj):
        pass


class EmbedImage(BaseSerializable):
    @staticmethod
    def from_dict(obj):
        pass


class EmbedThumbnail(BaseSerializable):
    @staticmethod
    def from_dict(obj):
        pass


class EmbedAuthor(BaseSerializable):
    __items__ = ('name', 'url', 'icon_url')

    def __init__(self, name: str = None, url: str = None, icon_url: str = None):
        self.name = name
        self.url = url
        self.icon_url = icon_url

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is not None and not isinstance(name, str):
            raise TypeError('name must be string')
        self._name = name

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        if url is not None and not isinstance(url, str):
            raise TypeError('url must be string')
        self._url = url

    @property
    def icon_url(self):
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        if icon_url is not None and not isinstance(icon_url, str):
            raise TypeError('icon_url must be string')
        self._icon_url = icon_url

    @staticmethod
    def from_dict(obj):
        pass


class EmbedField(BaseSerializable):
    @staticmethod
    def from_dict(obj):
        pass

    @property
    def dict(self):
        return {}


class Embed(BaseSerializable):
    __items__ = ('title', 'description', 'url', 'timestamp', 'color',
                 'footer', 'image', 'thumbnail', 'author', 'fields')

    def __init__(self, title: str = None, description: str = None, url: str = None, timestamp: datetime = None,
                 color: int = None,
                 footer: EmbedFooter = None, image: EmbedImage = None, thumbnail: EmbedThumbnail = None,
                 author: EmbedAuthor = None, fields: [EmbedField] = None):

        self.title = title
        self.description = description
        self.url = url
        self.timestamp = timestamp
        self.color = color
        self.footer = footer
        self.image = image
        self.thumbnail = thumbnail
        self.author = author
        self.fields = fields

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title is not None and not isinstance(title, str):
            raise TypeError('title must be string')
        if len(title) > 256:
            raise ValueError('title length must be up to 256 characters')
        self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if description is not None and not isinstance(description, str):
            raise TypeError('description must be string')
        if len(description) > 2048:
            raise ValueError('description length must be up to 2048 characters')
        self._description = description

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        if url is not None and not isinstance(url, str):
            raise TypeError('url must be string')
        self._url = url

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        if timestamp is not None and not isinstance(timestamp, datetime):
            raise TypeError('timestamp must be datetime')
        self._timestamp = timestamp

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if color is not None and not isinstance(color, int):
            raise TypeError('color must be int')
        self._color = color

    @property
    def footer(self):
        return self._footer

    @footer.setter
    def footer(self, footer):
        if footer is not None and not isinstance(footer, EmbedFooter):
            raise TypeError('footer must be EmbedFooter')
        self._footer = footer

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        if image is not None and not isinstance(image, EmbedImage):
            raise TypeError('image must be EmbedImage')
        self._image = image

    @property
    def thumbnail(self):
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        if thumbnail is not None and not isinstance(thumbnail, EmbedThumbnail):
            raise TypeError('thumbnail must be EmbedThumbnail')
        self._thumbnail = thumbnail

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if author is not None and not isinstance(author, EmbedAuthor):
            raise TypeError('author must be EmbedAuthor')
        self._author = author

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        if fields is None:
            self._fields = []
            return
        if not isinstance(fields, list):
            raise TypeError('embeds must be list')
        if len(fields) > 25:
            raise ValueError('embed can contain up to 25 field objects')
        self._fields = []
        for field in fields:
            if isinstance(field, EmbedField):
                self._fields.append(field)
            elif isinstance(field, dict):
                self._fields.append(EmbedField.from_dict(field))
            else:
                raise TypeError('fields items must be EmbedField or dict')

    @staticmethod
    def from_dict(obj):
        return Embed(**obj)

    @property
    def dict(self):
        return {key: getattr(self, key) for key in self.__items__ if getattr(self, key) is not None}
