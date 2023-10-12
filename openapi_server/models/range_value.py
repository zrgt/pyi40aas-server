from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class RangeValue(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, max=None, min=None):  # noqa: E501
        """RangeValue - a model defined in OpenAPI

        :param max: The max of this RangeValue.  # noqa: E501
        :type max: float
        :param min: The min of this RangeValue.  # noqa: E501
        :type min: float
        """
        self.openapi_types = {
            'max': float,
            'min': float
        }

        self.attribute_map = {
            'max': 'max',
            'min': 'min'
        }

        self._max = max
        self._min = min

    @classmethod
    def from_dict(cls, dikt) -> 'RangeValue':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RangeValue of this RangeValue.  # noqa: E501
        :rtype: RangeValue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def max(self) -> float:
        """Gets the max of this RangeValue.


        :return: The max of this RangeValue.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max: float):
        """Sets the max of this RangeValue.


        :param max: The max of this RangeValue.
        :type max: float
        """
        if max is None:
            raise ValueError("Invalid value for `max`, must not be `None`")  # noqa: E501

        self._max = max

    @property
    def min(self) -> float:
        """Gets the min of this RangeValue.


        :return: The min of this RangeValue.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min: float):
        """Sets the min of this RangeValue.


        :param min: The min of this RangeValue.
        :type min: float
        """
        if min is None:
            raise ValueError("Invalid value for `min`, must not be `None`")  # noqa: E501

        self._min = min
