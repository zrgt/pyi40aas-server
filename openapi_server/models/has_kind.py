from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.modelling_kind import ModellingKind
from openapi_server import util

from openapi_server.models.modelling_kind import ModellingKind  # noqa: E501

class HasKind(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, kind=None):  # noqa: E501
        """HasKind - a model defined in OpenAPI

        :param kind: The kind of this HasKind.  # noqa: E501
        :type kind: ModellingKind
        """
        self.openapi_types = {
            'kind': ModellingKind
        }

        self.attribute_map = {
            'kind': 'kind'
        }

        self._kind = kind

    @classmethod
    def from_dict(cls, dikt) -> 'HasKind':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HasKind of this HasKind.  # noqa: E501
        :rtype: HasKind
        """
        return util.deserialize_model(dikt, cls)

    @property
    def kind(self) -> ModellingKind:
        """Gets the kind of this HasKind.


        :return: The kind of this HasKind.
        :rtype: ModellingKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind: ModellingKind):
        """Sets the kind of this HasKind.


        :param kind: The kind of this HasKind.
        :type kind: ModellingKind
        """

        self._kind = kind
