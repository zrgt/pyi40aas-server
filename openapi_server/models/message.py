from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
import re
from openapi_server import util

import re  # noqa: E501

class Message(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code=None, correlation_id=None, message_type=None, text=None, timestamp=None):  # noqa: E501
        """Message - a model defined in OpenAPI

        :param code: The code of this Message.  # noqa: E501
        :type code: str
        :param correlation_id: The correlation_id of this Message.  # noqa: E501
        :type correlation_id: str
        :param message_type: The message_type of this Message.  # noqa: E501
        :type message_type: str
        :param text: The text of this Message.  # noqa: E501
        :type text: str
        :param timestamp: The timestamp of this Message.  # noqa: E501
        :type timestamp: str
        """
        self.openapi_types = {
            'code': str,
            'correlation_id': str,
            'message_type': str,
            'text': str,
            'timestamp': str
        }

        self.attribute_map = {
            'code': 'code',
            'correlation_id': 'correlationId',
            'message_type': 'messageType',
            'text': 'text',
            'timestamp': 'timestamp'
        }

        self._code = code
        self._correlation_id = correlation_id
        self._message_type = message_type
        self._text = text
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt) -> 'Message':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Message of this Message.  # noqa: E501
        :rtype: Message
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """Gets the code of this Message.


        :return: The code of this Message.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this Message.


        :param code: The code of this Message.
        :type code: str
        """
        if code is not None and len(code) > 32:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `32`")  # noqa: E501
        if code is not None and len(code) < 1:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501

        self._code = code

    @property
    def correlation_id(self) -> str:
        """Gets the correlation_id of this Message.


        :return: The correlation_id of this Message.
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id: str):
        """Sets the correlation_id of this Message.


        :param correlation_id: The correlation_id of this Message.
        :type correlation_id: str
        """
        if correlation_id is not None and len(correlation_id) > 128:
            raise ValueError("Invalid value for `correlation_id`, length must be less than or equal to `128`")  # noqa: E501
        if correlation_id is not None and len(correlation_id) < 1:
            raise ValueError("Invalid value for `correlation_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._correlation_id = correlation_id

    @property
    def message_type(self) -> str:
        """Gets the message_type of this Message.


        :return: The message_type of this Message.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type: str):
        """Sets the message_type of this Message.


        :param message_type: The message_type of this Message.
        :type message_type: str
        """
        allowed_values = ["Undefined", "Info", "Warning", "Error", "Exception"]  # noqa: E501
        if message_type not in allowed_values:
            raise ValueError(
                "Invalid value for `message_type` ({0}), must be one of {1}"
                .format(message_type, allowed_values)
            )

        self._message_type = message_type

    @property
    def text(self) -> str:
        """Gets the text of this Message.


        :return: The text of this Message.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this Message.


        :param text: The text of this Message.
        :type text: str
        """

        self._text = text

    @property
    def timestamp(self) -> str:
        """Gets the timestamp of this Message.


        :return: The timestamp of this Message.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        """Sets the timestamp of this Message.


        :param timestamp: The timestamp of this Message.
        :type timestamp: str
        """
        if timestamp is not None and not re.search(r'^-?(([1-9][0-9][0-9][0-9]+)|(0[0-9][0-9][0-9]))-((0[1-9])|(1[0-2]))-((0[1-9])|([12][0-9])|(3[01]))T(((([01][0-9])|(2[0-3])):[0-5][0-9]:([0-5][0-9])(\.[0-9]+)?)|24:00:00(\.0+)?)(Z|\+00:00|-00:00)$', timestamp):  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must be a follow pattern or equal to `/^-?(([1-9][0-9][0-9][0-9]+)|(0[0-9][0-9][0-9]))-((0[1-9])|(1[0-2]))-((0[1-9])|([12][0-9])|(3[01]))T(((([01][0-9])|(2[0-3])):[0-5][0-9]:([0-5][0-9])(\.[0-9]+)?)|24:00:00(\.0+)?)(Z|\+00:00|-00:00)$/`")  # noqa: E501

        self._timestamp = timestamp
