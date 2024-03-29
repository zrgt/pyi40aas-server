from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.extension import Extension
from openapi_server import util

from openapi_server.models.extension import Extension  # noqa: E501

class HasExtensions(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, extensions=None):  # noqa: E501
        """HasExtensions - a model defined in OpenAPI

        :param extensions: The extensions of this HasExtensions.  # noqa: E501
        :type extensions: List[Extension]
        """
        self.openapi_types = {
            'extensions': List[Extension]
        }

        self.attribute_map = {
            'extensions': 'extensions'
        }

        self._extensions = extensions

    @classmethod
    def from_dict(cls, dikt) -> 'HasExtensions':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HasExtensions of this HasExtensions.  # noqa: E501
        :rtype: HasExtensions
        """
        return util.deserialize_model(dikt, cls)

    @property
    def extensions(self) -> List[Extension]:
        """Gets the extensions of this HasExtensions.


        :return: The extensions of this HasExtensions.
        :rtype: List[Extension]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions: List[Extension]):
        """Sets the extensions of this HasExtensions.


        :param extensions: The extensions of this HasExtensions.
        :type extensions: List[Extension]
        """
        if extensions is not None and len(extensions) < 1:
            raise ValueError("Invalid value for `extensions`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._extensions = extensions
