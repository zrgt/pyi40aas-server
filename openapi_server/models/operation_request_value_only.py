from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
import re
from openapi_server import util

import re  # noqa: E501

class OperationRequestValueOnly(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, inoutput_arguments=None, input_arguments=None, client_timeout_duration=None):  # noqa: E501
        """OperationRequestValueOnly - a model defined in OpenAPI

        :param inoutput_arguments: The inoutput_arguments of this OperationRequestValueOnly.  # noqa: E501
        :type inoutput_arguments: object
        :param input_arguments: The input_arguments of this OperationRequestValueOnly.  # noqa: E501
        :type input_arguments: object
        :param client_timeout_duration: The client_timeout_duration of this OperationRequestValueOnly.  # noqa: E501
        :type client_timeout_duration: str
        """
        self.openapi_types = {
            'inoutput_arguments': object,
            'input_arguments': object,
            'client_timeout_duration': str
        }

        self.attribute_map = {
            'inoutput_arguments': 'inoutputArguments',
            'input_arguments': 'inputArguments',
            'client_timeout_duration': 'clientTimeoutDuration'
        }

        self._inoutput_arguments = inoutput_arguments
        self._input_arguments = input_arguments
        self._client_timeout_duration = client_timeout_duration

    @classmethod
    def from_dict(cls, dikt) -> 'OperationRequestValueOnly':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OperationRequestValueOnly of this OperationRequestValueOnly.  # noqa: E501
        :rtype: OperationRequestValueOnly
        """
        return util.deserialize_model(dikt, cls)

    @property
    def inoutput_arguments(self) -> object:
        """Gets the inoutput_arguments of this OperationRequestValueOnly.

        The ValueOnly serialization of submodel elements (patternProperties and propertyNames will be supported propably with OpenApi 3.1). The full description of the generic JSON validation schema for the ValueOnly-serialization can be found in chapter 11.4.3 in Details of the Asset Administration Shell Part 2.   # noqa: E501

        :return: The inoutput_arguments of this OperationRequestValueOnly.
        :rtype: object
        """
        return self._inoutput_arguments

    @inoutput_arguments.setter
    def inoutput_arguments(self, inoutput_arguments: object):
        """Sets the inoutput_arguments of this OperationRequestValueOnly.

        The ValueOnly serialization of submodel elements (patternProperties and propertyNames will be supported propably with OpenApi 3.1). The full description of the generic JSON validation schema for the ValueOnly-serialization can be found in chapter 11.4.3 in Details of the Asset Administration Shell Part 2.   # noqa: E501

        :param inoutput_arguments: The inoutput_arguments of this OperationRequestValueOnly.
        :type inoutput_arguments: object
        """

        self._inoutput_arguments = inoutput_arguments

    @property
    def input_arguments(self) -> object:
        """Gets the input_arguments of this OperationRequestValueOnly.

        The ValueOnly serialization of submodel elements (patternProperties and propertyNames will be supported propably with OpenApi 3.1). The full description of the generic JSON validation schema for the ValueOnly-serialization can be found in chapter 11.4.3 in Details of the Asset Administration Shell Part 2.   # noqa: E501

        :return: The input_arguments of this OperationRequestValueOnly.
        :rtype: object
        """
        return self._input_arguments

    @input_arguments.setter
    def input_arguments(self, input_arguments: object):
        """Sets the input_arguments of this OperationRequestValueOnly.

        The ValueOnly serialization of submodel elements (patternProperties and propertyNames will be supported propably with OpenApi 3.1). The full description of the generic JSON validation schema for the ValueOnly-serialization can be found in chapter 11.4.3 in Details of the Asset Administration Shell Part 2.   # noqa: E501

        :param input_arguments: The input_arguments of this OperationRequestValueOnly.
        :type input_arguments: object
        """

        self._input_arguments = input_arguments

    @property
    def client_timeout_duration(self) -> str:
        """Gets the client_timeout_duration of this OperationRequestValueOnly.


        :return: The client_timeout_duration of this OperationRequestValueOnly.
        :rtype: str
        """
        return self._client_timeout_duration

    @client_timeout_duration.setter
    def client_timeout_duration(self, client_timeout_duration: str):
        """Sets the client_timeout_duration of this OperationRequestValueOnly.


        :param client_timeout_duration: The client_timeout_duration of this OperationRequestValueOnly.
        :type client_timeout_duration: str
        """
        if client_timeout_duration is None:
            raise ValueError("Invalid value for `client_timeout_duration`, must not be `None`")  # noqa: E501
        if client_timeout_duration is not None and not re.search(r'^(-?)P(?=.)((\d+)Y)?((\d+)M)?((\d+)D)?(T(?=.)((\d+)H)?((\d+)M)?(\d*(\.\d+)?S)?)?$', client_timeout_duration):  # noqa: E501
            raise ValueError("Invalid value for `client_timeout_duration`, must be a follow pattern or equal to `/^(-?)P(?=.)((\d+)Y)?((\d+)M)?((\d+)D)?(T(?=.)((\d+)H)?((\d+)M)?(\d*(\.\d+)?S)?)?$/`")  # noqa: E501

        self._client_timeout_duration = client_timeout_duration
