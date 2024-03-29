from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.key_types import KeyTypes
import re
from openapi_server import util

from openapi_server.models.key_types import KeyTypes  # noqa: E501
import re  # noqa: E501

class Key(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, value=None):  # noqa: E501
        """Key - a model defined in OpenAPI

        :param type: The type of this Key.  # noqa: E501
        :type type: KeyTypes
        :param value: The value of this Key.  # noqa: E501
        :type value: str
        """
        self.openapi_types = {
            'type': KeyTypes,
            'value': str
        }

        self.attribute_map = {
            'type': 'type',
            'value': 'value'
        }

        self._type = type
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'Key':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Key of this Key.  # noqa: E501
        :rtype: Key
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> KeyTypes:
        """Gets the type of this Key.


        :return: The type of this Key.
        :rtype: KeyTypes
        """
        return self._type

    @type.setter
    def type(self, type: KeyTypes):
        """Sets the type of this Key.


        :param type: The type of this Key.
        :type type: KeyTypes
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def value(self) -> str:
        """Gets the value of this Key.


        :return: The value of this Key.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this Key.


        :param value: The value of this Key.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if value is not None and len(value) > 2000:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `2000`")  # noqa: E501
        if value is not None and len(value) < 1:
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  # noqa: E501
        if value is not None and not re.search(r'^([\t\n\r -퟿-�]|\ud800[\udc00-\udfff]|[\ud801-\udbfe][\udc00-\udfff]|\udbff[\udc00-\udfff])*$', value):  # noqa: E501
            raise ValueError("Invalid value for `value`, must be a follow pattern or equal to `/^([\t\n\r -퟿-�]|\ud800[\udc00-\udfff]|[\ud801-\udbfe][\udc00-\udfff]|\udbff[\udc00-\udfff])*$/`")  # noqa: E501

        self._value = value
