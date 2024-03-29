from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.protocol_information import ProtocolInformation
from openapi_server import util

from openapi_server.models.protocol_information import ProtocolInformation  # noqa: E501

class Endpoint(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, interface=None, protocol_information=None):  # noqa: E501
        """Endpoint - a model defined in OpenAPI

        :param interface: The interface of this Endpoint.  # noqa: E501
        :type interface: str
        :param protocol_information: The protocol_information of this Endpoint.  # noqa: E501
        :type protocol_information: ProtocolInformation
        """
        self.openapi_types = {
            'interface': str,
            'protocol_information': ProtocolInformation
        }

        self.attribute_map = {
            'interface': 'interface',
            'protocol_information': 'protocolInformation'
        }

        self._interface = interface
        self._protocol_information = protocol_information

    @classmethod
    def from_dict(cls, dikt) -> 'Endpoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Endpoint of this Endpoint.  # noqa: E501
        :rtype: Endpoint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def interface(self) -> str:
        """Gets the interface of this Endpoint.


        :return: The interface of this Endpoint.
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface: str):
        """Sets the interface of this Endpoint.


        :param interface: The interface of this Endpoint.
        :type interface: str
        """
        if interface is None:
            raise ValueError("Invalid value for `interface`, must not be `None`")  # noqa: E501
        if interface is not None and len(interface) > 128:
            raise ValueError("Invalid value for `interface`, length must be less than or equal to `128`")  # noqa: E501

        self._interface = interface

    @property
    def protocol_information(self) -> ProtocolInformation:
        """Gets the protocol_information of this Endpoint.


        :return: The protocol_information of this Endpoint.
        :rtype: ProtocolInformation
        """
        return self._protocol_information

    @protocol_information.setter
    def protocol_information(self, protocol_information: ProtocolInformation):
        """Sets the protocol_information of this Endpoint.


        :param protocol_information: The protocol_information of this Endpoint.
        :type protocol_information: ProtocolInformation
        """
        if protocol_information is None:
            raise ValueError("Invalid value for `protocol_information`, must not be `None`")  # noqa: E501

        self._protocol_information = protocol_information
