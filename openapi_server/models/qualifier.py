from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.data_type_def_xsd import DataTypeDefXsd
from openapi_server.models.qualifier_kind import QualifierKind
from openapi_server.models.reference import Reference
import re
from openapi_server import util

from openapi_server.models.data_type_def_xsd import DataTypeDefXsd  # noqa: E501
from openapi_server.models.qualifier_kind import QualifierKind  # noqa: E501
from openapi_server.models.reference import Reference  # noqa: E501
import re  # noqa: E501

class Qualifier(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, semantic_id=None, supplemental_semantic_ids=None, kind=None, type=None, value_type=None, value=None, value_id=None):  # noqa: E501
        """Qualifier - a model defined in OpenAPI

        :param semantic_id: The semantic_id of this Qualifier.  # noqa: E501
        :type semantic_id: Reference
        :param supplemental_semantic_ids: The supplemental_semantic_ids of this Qualifier.  # noqa: E501
        :type supplemental_semantic_ids: List[Reference]
        :param kind: The kind of this Qualifier.  # noqa: E501
        :type kind: QualifierKind
        :param type: The type of this Qualifier.  # noqa: E501
        :type type: str
        :param value_type: The value_type of this Qualifier.  # noqa: E501
        :type value_type: DataTypeDefXsd
        :param value: The value of this Qualifier.  # noqa: E501
        :type value: str
        :param value_id: The value_id of this Qualifier.  # noqa: E501
        :type value_id: Reference
        """
        self.openapi_types = {
            'semantic_id': Reference,
            'supplemental_semantic_ids': List[Reference],
            'kind': QualifierKind,
            'type': str,
            'value_type': DataTypeDefXsd,
            'value': str,
            'value_id': Reference
        }

        self.attribute_map = {
            'semantic_id': 'semanticId',
            'supplemental_semantic_ids': 'supplementalSemanticIds',
            'kind': 'kind',
            'type': 'type',
            'value_type': 'valueType',
            'value': 'value',
            'value_id': 'valueId'
        }

        self._semantic_id = semantic_id
        self._supplemental_semantic_ids = supplemental_semantic_ids
        self._kind = kind
        self._type = type
        self._value_type = value_type
        self._value = value
        self._value_id = value_id

    @classmethod
    def from_dict(cls, dikt) -> 'Qualifier':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Qualifier of this Qualifier.  # noqa: E501
        :rtype: Qualifier
        """
        return util.deserialize_model(dikt, cls)

    @property
    def semantic_id(self) -> Reference:
        """Gets the semantic_id of this Qualifier.


        :return: The semantic_id of this Qualifier.
        :rtype: Reference
        """
        return self._semantic_id

    @semantic_id.setter
    def semantic_id(self, semantic_id: Reference):
        """Sets the semantic_id of this Qualifier.


        :param semantic_id: The semantic_id of this Qualifier.
        :type semantic_id: Reference
        """

        self._semantic_id = semantic_id

    @property
    def supplemental_semantic_ids(self) -> List[Reference]:
        """Gets the supplemental_semantic_ids of this Qualifier.


        :return: The supplemental_semantic_ids of this Qualifier.
        :rtype: List[Reference]
        """
        return self._supplemental_semantic_ids

    @supplemental_semantic_ids.setter
    def supplemental_semantic_ids(self, supplemental_semantic_ids: List[Reference]):
        """Sets the supplemental_semantic_ids of this Qualifier.


        :param supplemental_semantic_ids: The supplemental_semantic_ids of this Qualifier.
        :type supplemental_semantic_ids: List[Reference]
        """
        if supplemental_semantic_ids is not None and len(supplemental_semantic_ids) < 1:
            raise ValueError("Invalid value for `supplemental_semantic_ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._supplemental_semantic_ids = supplemental_semantic_ids

    @property
    def kind(self) -> QualifierKind:
        """Gets the kind of this Qualifier.


        :return: The kind of this Qualifier.
        :rtype: QualifierKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind: QualifierKind):
        """Sets the kind of this Qualifier.


        :param kind: The kind of this Qualifier.
        :type kind: QualifierKind
        """

        self._kind = kind

    @property
    def type(self) -> str:
        """Gets the type of this Qualifier.


        :return: The type of this Qualifier.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Qualifier.


        :param type: The type of this Qualifier.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if type is not None and len(type) > 128:
            raise ValueError("Invalid value for `type`, length must be less than or equal to `128`")  # noqa: E501
        if type is not None and len(type) < 1:
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501
        if type is not None and not re.search(r'^([\t\n\r -퟿-�]|\ud800[\udc00-\udfff]|[\ud801-\udbfe][\udc00-\udfff]|\udbff[\udc00-\udfff])*$', type):  # noqa: E501
            raise ValueError("Invalid value for `type`, must be a follow pattern or equal to `/^([\t\n\r -퟿-�]|\ud800[\udc00-\udfff]|[\ud801-\udbfe][\udc00-\udfff]|\udbff[\udc00-\udfff])*$/`")  # noqa: E501

        self._type = type

    @property
    def value_type(self) -> DataTypeDefXsd:
        """Gets the value_type of this Qualifier.


        :return: The value_type of this Qualifier.
        :rtype: DataTypeDefXsd
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type: DataTypeDefXsd):
        """Sets the value_type of this Qualifier.


        :param value_type: The value_type of this Qualifier.
        :type value_type: DataTypeDefXsd
        """
        if value_type is None:
            raise ValueError("Invalid value for `value_type`, must not be `None`")  # noqa: E501

        self._value_type = value_type

    @property
    def value(self) -> str:
        """Gets the value of this Qualifier.


        :return: The value of this Qualifier.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this Qualifier.


        :param value: The value of this Qualifier.
        :type value: str
        """

        self._value = value

    @property
    def value_id(self) -> Reference:
        """Gets the value_id of this Qualifier.


        :return: The value_id of this Qualifier.
        :rtype: Reference
        """
        return self._value_id

    @value_id.setter
    def value_id(self, value_id: Reference):
        """Sets the value_id of this Qualifier.


        :param value_id: The value_id of this Qualifier.
        :type value_id: Reference
        """

        self._value_id = value_id
