from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.embedded_data_specification import EmbeddedDataSpecification
from openapi_server.models.extension import Extension
from openapi_server.models.lang_string_name_type import LangStringNameType
from openapi_server.models.lang_string_text_type import LangStringTextType
from openapi_server.models.model_type import ModelType
from openapi_server.models.modelling_kind import ModellingKind
from openapi_server.models.qualifier import Qualifier
from openapi_server.models.reference import Reference
import re
from openapi_server import util

from openapi_server.models.embedded_data_specification import EmbeddedDataSpecification  # noqa: E501
from openapi_server.models.extension import Extension  # noqa: E501
from openapi_server.models.lang_string_name_type import LangStringNameType  # noqa: E501
from openapi_server.models.lang_string_text_type import LangStringTextType  # noqa: E501
from openapi_server.models.model_type import ModelType  # noqa: E501
from openapi_server.models.modelling_kind import ModellingKind  # noqa: E501
from openapi_server.models.qualifier import Qualifier  # noqa: E501
from openapi_server.models.reference import Reference  # noqa: E501
import re  # noqa: E501

class AnnotatedRelationshipElementMetadata(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, extensions=None, category=None, id_short=None, display_name=None, description=None, model_type=None, embedded_data_specifications=None, semantic_id=None, supplemental_semantic_ids=None, qualifiers=None, kind=None):  # noqa: E501
        """AnnotatedRelationshipElementMetadata - a model defined in OpenAPI

        :param extensions: The extensions of this AnnotatedRelationshipElementMetadata.  # noqa: E501
        :type extensions: List[Extension]
        :param category: The category of this AnnotatedRelationshipElementMetadata.  # noqa: E501
        :type category: str
        :param id_short: The id_short of this AnnotatedRelationshipElementMetadata.  # noqa: E501
        :type id_short: object
        :param display_name: The display_name of this AnnotatedRelationshipElementMetadata.  # noqa: E501
        :type display_name: List[LangStringNameType]
        :param description: The description of this AnnotatedRelationshipElementMetadata.  # noqa: E501
        :type description: List[LangStringTextType]
        :param model_type: The model_type of this AnnotatedRelationshipElementMetadata.  # noqa: E501
        :type model_type: ModelType
        :param embedded_data_specifications: The embedded_data_specifications of this AnnotatedRelationshipElementMetadata.  # noqa: E501
        :type embedded_data_specifications: List[EmbeddedDataSpecification]
        :param semantic_id: The semantic_id of this AnnotatedRelationshipElementMetadata.  # noqa: E501
        :type semantic_id: Reference
        :param supplemental_semantic_ids: The supplemental_semantic_ids of this AnnotatedRelationshipElementMetadata.  # noqa: E501
        :type supplemental_semantic_ids: List[Reference]
        :param qualifiers: The qualifiers of this AnnotatedRelationshipElementMetadata.  # noqa: E501
        :type qualifiers: List[Qualifier]
        :param kind: The kind of this AnnotatedRelationshipElementMetadata.  # noqa: E501
        :type kind: ModellingKind
        """
        self.openapi_types = {
            'extensions': List[Extension],
            'category': str,
            'id_short': object,
            'display_name': List[LangStringNameType],
            'description': List[LangStringTextType],
            'model_type': ModelType,
            'embedded_data_specifications': List[EmbeddedDataSpecification],
            'semantic_id': Reference,
            'supplemental_semantic_ids': List[Reference],
            'qualifiers': List[Qualifier],
            'kind': ModellingKind
        }

        self.attribute_map = {
            'extensions': 'extensions',
            'category': 'category',
            'id_short': 'idShort',
            'display_name': 'displayName',
            'description': 'description',
            'model_type': 'modelType',
            'embedded_data_specifications': 'embeddedDataSpecifications',
            'semantic_id': 'semanticId',
            'supplemental_semantic_ids': 'supplementalSemanticIds',
            'qualifiers': 'qualifiers',
            'kind': 'kind'
        }

        self._extensions = extensions
        self._category = category
        self._id_short = id_short
        self._display_name = display_name
        self._description = description
        self._model_type = model_type
        self._embedded_data_specifications = embedded_data_specifications
        self._semantic_id = semantic_id
        self._supplemental_semantic_ids = supplemental_semantic_ids
        self._qualifiers = qualifiers
        self._kind = kind

    @classmethod
    def from_dict(cls, dikt) -> 'AnnotatedRelationshipElementMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AnnotatedRelationshipElementMetadata of this AnnotatedRelationshipElementMetadata.  # noqa: E501
        :rtype: AnnotatedRelationshipElementMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def extensions(self) -> List[Extension]:
        """Gets the extensions of this AnnotatedRelationshipElementMetadata.


        :return: The extensions of this AnnotatedRelationshipElementMetadata.
        :rtype: List[Extension]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions: List[Extension]):
        """Sets the extensions of this AnnotatedRelationshipElementMetadata.


        :param extensions: The extensions of this AnnotatedRelationshipElementMetadata.
        :type extensions: List[Extension]
        """
        if extensions is not None and len(extensions) < 1:
            raise ValueError("Invalid value for `extensions`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._extensions = extensions

    @property
    def category(self) -> str:
        """Gets the category of this AnnotatedRelationshipElementMetadata.


        :return: The category of this AnnotatedRelationshipElementMetadata.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str):
        """Sets the category of this AnnotatedRelationshipElementMetadata.


        :param category: The category of this AnnotatedRelationshipElementMetadata.
        :type category: str
        """
        if category is not None and len(category) > 128:
            raise ValueError("Invalid value for `category`, length must be less than or equal to `128`")  # noqa: E501
        if category is not None and len(category) < 1:
            raise ValueError("Invalid value for `category`, length must be greater than or equal to `1`")  # noqa: E501
        if category is not None and not re.search(r'^([\t\n\r -퟿-�]|\ud800[\udc00-\udfff]|[\ud801-\udbfe][\udc00-\udfff]|\udbff[\udc00-\udfff])*$', category):  # noqa: E501
            raise ValueError("Invalid value for `category`, must be a follow pattern or equal to `/^([\t\n\r -퟿-�]|\ud800[\udc00-\udfff]|[\ud801-\udbfe][\udc00-\udfff]|\udbff[\udc00-\udfff])*$/`")  # noqa: E501

        self._category = category

    @property
    def id_short(self) -> object:
        """Gets the id_short of this AnnotatedRelationshipElementMetadata.


        :return: The id_short of this AnnotatedRelationshipElementMetadata.
        :rtype: object
        """
        return self._id_short

    @id_short.setter
    def id_short(self, id_short: object):
        """Sets the id_short of this AnnotatedRelationshipElementMetadata.


        :param id_short: The id_short of this AnnotatedRelationshipElementMetadata.
        :type id_short: object
        """

        self._id_short = id_short

    @property
    def display_name(self) -> List[LangStringNameType]:
        """Gets the display_name of this AnnotatedRelationshipElementMetadata.


        :return: The display_name of this AnnotatedRelationshipElementMetadata.
        :rtype: List[LangStringNameType]
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: List[LangStringNameType]):
        """Sets the display_name of this AnnotatedRelationshipElementMetadata.


        :param display_name: The display_name of this AnnotatedRelationshipElementMetadata.
        :type display_name: List[LangStringNameType]
        """
        if display_name is not None and len(display_name) < 1:
            raise ValueError("Invalid value for `display_name`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self) -> List[LangStringTextType]:
        """Gets the description of this AnnotatedRelationshipElementMetadata.


        :return: The description of this AnnotatedRelationshipElementMetadata.
        :rtype: List[LangStringTextType]
        """
        return self._description

    @description.setter
    def description(self, description: List[LangStringTextType]):
        """Sets the description of this AnnotatedRelationshipElementMetadata.


        :param description: The description of this AnnotatedRelationshipElementMetadata.
        :type description: List[LangStringTextType]
        """
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def model_type(self) -> ModelType:
        """Gets the model_type of this AnnotatedRelationshipElementMetadata.


        :return: The model_type of this AnnotatedRelationshipElementMetadata.
        :rtype: ModelType
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type: ModelType):
        """Sets the model_type of this AnnotatedRelationshipElementMetadata.


        :param model_type: The model_type of this AnnotatedRelationshipElementMetadata.
        :type model_type: ModelType
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501

        self._model_type = model_type

    @property
    def embedded_data_specifications(self) -> List[EmbeddedDataSpecification]:
        """Gets the embedded_data_specifications of this AnnotatedRelationshipElementMetadata.


        :return: The embedded_data_specifications of this AnnotatedRelationshipElementMetadata.
        :rtype: List[EmbeddedDataSpecification]
        """
        return self._embedded_data_specifications

    @embedded_data_specifications.setter
    def embedded_data_specifications(self, embedded_data_specifications: List[EmbeddedDataSpecification]):
        """Sets the embedded_data_specifications of this AnnotatedRelationshipElementMetadata.


        :param embedded_data_specifications: The embedded_data_specifications of this AnnotatedRelationshipElementMetadata.
        :type embedded_data_specifications: List[EmbeddedDataSpecification]
        """
        if embedded_data_specifications is not None and len(embedded_data_specifications) < 1:
            raise ValueError("Invalid value for `embedded_data_specifications`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._embedded_data_specifications = embedded_data_specifications

    @property
    def semantic_id(self) -> Reference:
        """Gets the semantic_id of this AnnotatedRelationshipElementMetadata.


        :return: The semantic_id of this AnnotatedRelationshipElementMetadata.
        :rtype: Reference
        """
        return self._semantic_id

    @semantic_id.setter
    def semantic_id(self, semantic_id: Reference):
        """Sets the semantic_id of this AnnotatedRelationshipElementMetadata.


        :param semantic_id: The semantic_id of this AnnotatedRelationshipElementMetadata.
        :type semantic_id: Reference
        """

        self._semantic_id = semantic_id

    @property
    def supplemental_semantic_ids(self) -> List[Reference]:
        """Gets the supplemental_semantic_ids of this AnnotatedRelationshipElementMetadata.


        :return: The supplemental_semantic_ids of this AnnotatedRelationshipElementMetadata.
        :rtype: List[Reference]
        """
        return self._supplemental_semantic_ids

    @supplemental_semantic_ids.setter
    def supplemental_semantic_ids(self, supplemental_semantic_ids: List[Reference]):
        """Sets the supplemental_semantic_ids of this AnnotatedRelationshipElementMetadata.


        :param supplemental_semantic_ids: The supplemental_semantic_ids of this AnnotatedRelationshipElementMetadata.
        :type supplemental_semantic_ids: List[Reference]
        """
        if supplemental_semantic_ids is not None and len(supplemental_semantic_ids) < 1:
            raise ValueError("Invalid value for `supplemental_semantic_ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._supplemental_semantic_ids = supplemental_semantic_ids

    @property
    def qualifiers(self) -> List[Qualifier]:
        """Gets the qualifiers of this AnnotatedRelationshipElementMetadata.


        :return: The qualifiers of this AnnotatedRelationshipElementMetadata.
        :rtype: List[Qualifier]
        """
        return self._qualifiers

    @qualifiers.setter
    def qualifiers(self, qualifiers: List[Qualifier]):
        """Sets the qualifiers of this AnnotatedRelationshipElementMetadata.


        :param qualifiers: The qualifiers of this AnnotatedRelationshipElementMetadata.
        :type qualifiers: List[Qualifier]
        """
        if qualifiers is not None and len(qualifiers) < 1:
            raise ValueError("Invalid value for `qualifiers`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._qualifiers = qualifiers

    @property
    def kind(self) -> ModellingKind:
        """Gets the kind of this AnnotatedRelationshipElementMetadata.


        :return: The kind of this AnnotatedRelationshipElementMetadata.
        :rtype: ModellingKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind: ModellingKind):
        """Sets the kind of this AnnotatedRelationshipElementMetadata.


        :param kind: The kind of this AnnotatedRelationshipElementMetadata.
        :type kind: ModellingKind
        """

        self._kind = kind
