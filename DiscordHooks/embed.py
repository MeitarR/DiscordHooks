# -*- coding: utf-8 -*-

from datetime import datetime
from abc import ABC, abstractmethod


class Color:
    """The Color class

    Holds some common colors to use with the Embed.
    """
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
    """Abstract class for serializable objects"""
    __items__ = ()

    @property
    def dict(self) -> dict:
        """dict: The dict for serialization"""
        return {key: getattr(self, key) for key in self.__items__ if getattr(self, key) is not None}

    @staticmethod
    @abstractmethod
    def from_dict(obj: dict) -> 'BaseSerializable':
        """Abstract method for creating the object from dict

        Args:
            obj (dict): The dict the returned object will build from.

        Returns:
            BaseSerializable: The created object.
        """
        pass


class EmbedFooter(BaseSerializable):
    """Represent the Embed Footer according to Discord Developer Documentation for webhooks
    https://discordapp.com/developers/docs/resources/channel#embed-object-embed-footer-structure

    Attributes:
        text (str): footer text
        icon_url (str): url of footer icon (only supports http(s) and attachments)
    """
    __items__ = ('text', 'icon_url')

    def __init__(self, text: str = None, icon_url: str = None):
        """Initiate the EmbedFooter object

        Args:
            text (str): footer text
            icon_url (str): url of footer icon (only supports http(s) and attachments)
        """
        self.text = text
        self.icon_url = icon_url

    @property
    def text(self) -> str:
        """str: footer text. max length is 2048 characters"""
        return self._text

    @text.setter
    def text(self, text: str):
        if text is not None and not isinstance(text, str):
            raise TypeError('text must be string')
        if len(text) > 2048:
            raise ValueError('text length must be up to 2048 characters')
        self._text = text

    @property
    def icon_url(self) -> str:
        """str: url of footer icon (only supports http(s) and attachments)"""
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url: str):
        if icon_url is not None and not isinstance(icon_url, str):
            raise TypeError('icon_url must be string')
        self._icon_url = icon_url

    @staticmethod
    def from_dict(obj: dict) -> 'EmbedFooter':
        """Abstract method for creating the object from dict

        Args:
            obj (dict): The dict the returned object will build from.

        Returns:
            EmbedFooter: The created object.
        """
        return EmbedFooter(**obj)


class EmbedImage(BaseSerializable):
    """Represent the Embed Image according to Discord Developer Documentation for webhooks
    https://discordapp.com/developers/docs/resources/channel#embed-object-embed-image-structure

    Attributes:
        url (str): source url of image (only supports http(s) and attachments)
    """
    __items__ = ('url',)

    def __init__(self, url: str = None):
        """Initiate the EmbedImage object

        Args:
            url (str): source url of image (only supports http(s) and attachments)
        """
        self.url = url

    @property
    def url(self) -> str:
        """str: source url of image (only supports http(s) and attachments)"""
        return self._url

    @url.setter
    def url(self, url: str):
        if url is not None and not isinstance(url, str):
            raise TypeError('url must be string')
        self._url = url

    @staticmethod
    def from_dict(obj: dict) -> 'EmbedImage':
        """Abstract method for creating the object from dict

        Args:
            obj (dict): The dict the returned object will build from.

        Returns:
            EmbedImage: The created object.
        """
        return EmbedImage(**obj)


class EmbedThumbnail(BaseSerializable):
    """Represent the Embed Thumbnail according to Discord Developer Documentation for webhooks
    https://discordapp.com/developers/docs/resources/channel#embed-object-embed-thumbnail-structure

    Attributes:
        url (str): source url of thumbnail (only supports http(s) and attachments)
    """
    __items__ = ('url',)

    def __init__(self, url: str = None):
        """Initiate the EmbedThumbnail object

        Args:
            url (str): source url of thumbnail (only supports http(s) and attachments)
        """
        self.url = url

    @property
    def url(self) -> str:
        """str: source url of thumbnail (only supports http(s) and attachments)"""
        return self._url

    @url.setter
    def url(self, url: str):
        if url is not None and not isinstance(url, str):
            raise TypeError('url must be string')
        self._url = url

    @staticmethod
    def from_dict(obj: dict) -> 'EmbedThumbnail':
        """Abstract method for creating the object from dict

        Args:
            obj (dict): The dict the returned object will build from.

        Returns:
            EmbedThumbnail: The created object.
        """
        return EmbedThumbnail(**obj)


class EmbedAuthor(BaseSerializable):
    """Represent the Embed Author according to Discord Developer Documentation for webhooks
    https://discordapp.com/developers/docs/resources/channel#embed-object-embed-author-structure

    Attributes:
        name (str): name of author
        url (str): url of author
        icon_url (str): url of author icon (only supports http(s) and attachments)
    """
    __items__ = ('name', 'url', 'icon_url')

    def __init__(self, name: str = None, url: str = None, icon_url: str = None):
        """Initiate the EmbedAuthor object

        Args:
            name (str): name of author
            url (str): url of author
            icon_url (str): url of author icon (only supports http(s) and attachments)
        """
        self.name = name
        self.url = url
        self.icon_url = icon_url

    @property
    def name(self) -> str:
        """str: name of author. max length is 256 characters"""
        return self._name

    @name.setter
    def name(self, name: str):
        if name is not None and not isinstance(name, str):
            raise TypeError('name must be string')
        if len(name) > 256:
            raise ValueError('name length must be up to 256 characters')
        self._name = name

    @property
    def url(self) -> str:
        """str: url of author"""
        return self._url

    @url.setter
    def url(self, url: str):
        if url is not None and not isinstance(url, str):
            raise TypeError('url must be string')
        self._url = url

    @property
    def icon_url(self) -> str:
        """str: url of author icon (only supports http(s) and attachments)"""
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url: str):
        if icon_url is not None and not isinstance(icon_url, str):
            raise TypeError('icon_url must be string')
        self._icon_url = icon_url

    @staticmethod
    def from_dict(obj: dict) -> 'EmbedAuthor':
        """Abstract method for creating the object from dict

        Args:
            obj (dict): The dict the returned object will build from.

        Returns:
            EmbedAuthor: The created object.
        """
        return EmbedAuthor(**obj)


class EmbedField(BaseSerializable):
    """Represent the Embed Field according to Discord Developer Documentation for webhooks
    https://discordapp.com/developers/docs/resources/channel#embed-object-embed-field-structure

    Attributes:
        name (str): name of the field
        value (str): value of the field
    """
    __items__ = ('name', 'value')

    def __init__(self, name: str = None, value: str = None):
        """Initiate the EmbedField object

        Args:
            name (str): name of the field
            value (str): value of the field
        """
        self.name = name
        self.value = value

    @property
    def name(self) -> str:
        """str: name of the field. max length is 256 characters"""
        return self._name

    @name.setter
    def name(self, name: str):
        if name is not None and not isinstance(name, str):
            raise TypeError('name must be string')
        if len(name) > 256:
            raise ValueError('name length must be up to 256 characters')
        self._name = name

    @property
    def value(self) -> str:
        """str: value of the field. max length is 1024 characters"""
        return self._value

    @value.setter
    def value(self, value: str):
        if value is not None and not isinstance(value, str):
            raise TypeError('value must be string')
        if len(value) > 1024:
            raise ValueError('value length must be up to 1024 characters')
        self._value = value

    @staticmethod
    def from_dict(obj: dict) -> 'EmbedField':
        """Abstract method for creating the object from dict

        Args:
            obj (dict): The dict the returned object will build from.

        Returns:
            EmbedField: The created object.
        """
        return EmbedField(**obj)


class Embed(BaseSerializable):
    """Represent the Embed according to Discord Developer Documentation for webhooks
    https://discordapp.com/developers/docs/resources/channel#embed-object

    Attributes:
        title (str): title of embed
        description (str): description of embed
        url (str): url of embed
        timestamp (datetime): timestamp of embed content
        color (int): color code of the embed
        footer (EmbedFooter): footer object
        image (EmbedImage): image object
        thumbnail (EmbedThumbnail): thumbnail object
        author (EmbedAuthor): author object
        fields ([EmbedField]): field objects list
    """
    __items__ = ('title', 'description', 'url', 'timestamp', 'color',
                 'footer', 'image', 'thumbnail', 'author', 'fields')

    def __init__(self, title: str = None, description: str = None, url: str = None, timestamp: datetime = None,
                 color: int = None, footer: EmbedFooter = None, image: EmbedImage = None,
                 thumbnail: EmbedThumbnail = None, author: EmbedAuthor = None, fields: [EmbedField] = None):
        """Initiate the Embed object

        Args:
            title (str): title of embed
            description (str): description of embed
            url (str): url of embed
            timestamp (datetime): timestamp of embed content
            color (int): color code of the embed
            footer (EmbedFooter): footer object
            image (EmbedImage): image object
            thumbnail (EmbedThumbnail): thumbnail object
            author (EmbedAuthor): author object
            fields ([EmbedField]): field objects list
        """
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
    def title(self) -> str:
        """str: title of embed. max length is 256 characters"""
        return self._title

    @title.setter
    def title(self, title: str):
        if title is not None and not isinstance(title, str):
            raise TypeError('title must be string')
        if len(title) > 256:
            raise ValueError('title length must be up to 256 characters')
        self._title = title

    @property
    def description(self) -> str:
        """str: description of embed. max length is 2048 characters"""
        return self._description

    @description.setter
    def description(self, description: str):
        if description is not None and not isinstance(description, str):
            raise TypeError('description must be string')
        if len(description) > 2048:
            raise ValueError('description length must be up to 2048 characters')
        self._description = description

    @property
    def url(self) -> str:
        """str: url of embed"""
        return self._url

    @url.setter
    def url(self, url: str):
        if url is not None and not isinstance(url, str):
            raise TypeError('url must be string')
        self._url = url

    @property
    def timestamp(self) -> datetime:
        """datetime: timestamp of embed"""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        if timestamp is not None and not isinstance(timestamp, datetime):
            raise TypeError('timestamp must be datetime')
        self._timestamp = timestamp

    @property
    def color(self) -> int:
        """int: color code of the embed"""
        return self._color

    @color.setter
    def color(self, color: int):
        if color is not None and not isinstance(color, int):
            raise TypeError('color must be int')
        self._color = color

    @property
    def footer(self) -> EmbedFooter:
        """EmbedFooter: footer object"""
        return self._footer

    @footer.setter
    def footer(self, footer: EmbedFooter):
        if footer is not None and not isinstance(footer, EmbedFooter):
            raise TypeError('footer must be EmbedFooter')
        self._footer = footer

    @property
    def image(self) -> EmbedImage:
        """EmbedImage: image object"""
        return self._image

    @image.setter
    def image(self, image: EmbedImage):
        if image is not None and not isinstance(image, EmbedImage):
            raise TypeError('image must be EmbedImage')
        self._image = image

    @property
    def thumbnail(self) -> EmbedThumbnail:
        """EmbedThumbnail: thumbnail object"""
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail: EmbedThumbnail):
        if thumbnail is not None and not isinstance(thumbnail, EmbedThumbnail):
            raise TypeError('thumbnail must be EmbedThumbnail')
        self._thumbnail = thumbnail

    @property
    def author(self) -> EmbedAuthor:
        """EmbedAuthor: author object"""
        return self._author

    @author.setter
    def author(self, author: EmbedAuthor):
        if author is not None and not isinstance(author, EmbedAuthor):
            raise TypeError('author must be EmbedAuthor')
        self._author = author

    @property
    def fields(self) -> [EmbedField]:
        """[EmbedField]: field objects list. max length is 25 fields"""
        return self._fields

    @fields.setter
    def fields(self, fields: [EmbedField]):
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
    def from_dict(obj: dict) -> 'Embed':
        """Abstract method for creating the object from dict

        Args:
            obj (dict): The dict the returned object will build from.

        Returns:
            Embed: The created object.
        """
        return Embed(**obj)
