from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.message import Message
from openapi_server import util

from openapi_server.models.message import Message  # noqa: E501

class Result(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, messages=None):  # noqa: E501
        """Result - a model defined in OpenAPI

        :param messages: The messages of this Result.  # noqa: E501
        :type messages: List[Message]
        """
        self.openapi_types = {
            'messages': List[Message]
        }

        self.attribute_map = {
            'messages': 'messages'
        }

        self._messages = messages

    @classmethod
    def from_dict(cls, dikt) -> 'Result':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Result of this Result.  # noqa: E501
        :rtype: Result
        """
        return util.deserialize_model(dikt, cls)

    @property
    def messages(self) -> List[Message]:
        """Gets the messages of this Result.


        :return: The messages of this Result.
        :rtype: List[Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages: List[Message]):
        """Sets the messages of this Result.


        :param messages: The messages of this Result.
        :type messages: List[Message]
        """

        self._messages = messages
