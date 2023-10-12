from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.submodel_element_choice import SubmodelElementChoice
from openapi_server import util

from openapi_server.models.submodel_element_choice import SubmodelElementChoice  # noqa: E501

class OperationVariable(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value=None):  # noqa: E501
        """OperationVariable - a model defined in OpenAPI

        :param value: The value of this OperationVariable.  # noqa: E501
        :type value: SubmodelElementChoice
        """
        self.openapi_types = {
            'value': SubmodelElementChoice
        }

        self.attribute_map = {
            'value': 'value'
        }

        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'OperationVariable':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OperationVariable of this OperationVariable.  # noqa: E501
        :rtype: OperationVariable
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> SubmodelElementChoice:
        """Gets the value of this OperationVariable.


        :return: The value of this OperationVariable.
        :rtype: SubmodelElementChoice
        """
        return self._value

    @value.setter
    def value(self, value: SubmodelElementChoice):
        """Sets the value of this OperationVariable.


        :param value: The value of this OperationVariable.
        :type value: SubmodelElementChoice
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value
