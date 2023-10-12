from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.embedded_data_specification import EmbeddedDataSpecification
from openapi_server.models.extension import Extension
from openapi_server.models.lang_string_name_type import LangStringNameType
from openapi_server.models.lang_string_text_type import LangStringTextType
from openapi_server.models.qualifier import Qualifier
from openapi_server.models.reference import Reference
from openapi_server.models.submodel_element_choice import SubmodelElementChoice
import re
from openapi_server import util

from openapi_server.models.embedded_data_specification import EmbeddedDataSpecification  # noqa: E501
from openapi_server.models.extension import Extension  # noqa: E501
from openapi_server.models.lang_string_name_type import LangStringNameType  # noqa: E501
from openapi_server.models.lang_string_text_type import LangStringTextType  # noqa: E501
from openapi_server.models.qualifier import Qualifier  # noqa: E501
from openapi_server.models.reference import Reference  # noqa: E501
from openapi_server.models.submodel_element_choice import SubmodelElementChoice  # noqa: E501
import re  # noqa: E501

class SubmodelElementCollection(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, extensions=None, category=None, id_short=None, display_name=None, description=None, model_type=None, semantic_id=None, supplemental_semantic_ids=None, qualifiers=None, embedded_data_specifications=None, value=None):  # noqa: E501
        """SubmodelElementCollection - a model defined in OpenAPI

        :param extensions: The extensions of this SubmodelElementCollection.  # noqa: E501
        :type extensions: List[Extension]
        :param category: The category of this SubmodelElementCollection.  # noqa: E501
        :type category: str
        :param id_short: The id_short of this SubmodelElementCollection.  # noqa: E501
        :type id_short: object
        :param display_name: The display_name of this SubmodelElementCollection.  # noqa: E501
        :type display_name: List[LangStringNameType]
        :param description: The description of this SubmodelElementCollection.  # noqa: E501
        :type description: List[LangStringTextType]
        :param model_type: The model_type of this SubmodelElementCollection.  # noqa: E501
        :type model_type: str
        :param semantic_id: The semantic_id of this SubmodelElementCollection.  # noqa: E501
        :type semantic_id: Reference
        :param supplemental_semantic_ids: The supplemental_semantic_ids of this SubmodelElementCollection.  # noqa: E501
        :type supplemental_semantic_ids: List[Reference]
        :param qualifiers: The qualifiers of this SubmodelElementCollection.  # noqa: E501
        :type qualifiers: List[Qualifier]
        :param embedded_data_specifications: The embedded_data_specifications of this SubmodelElementCollection.  # noqa: E501
        :type embedded_data_specifications: List[EmbeddedDataSpecification]
        :param value: The value of this SubmodelElementCollection.  # noqa: E501
        :type value: List[SubmodelElementChoice]
        """
        self.openapi_types = {
            'extensions': List[Extension],
            'category': str,
            'id_short': object,
            'display_name': List[LangStringNameType],
            'description': List[LangStringTextType],
            'model_type': str,
            'semantic_id': Reference,
            'supplemental_semantic_ids': List[Reference],
            'qualifiers': List[Qualifier],
            'embedded_data_specifications': List[EmbeddedDataSpecification],
            'value': List[SubmodelElementChoice]
        }

        self.attribute_map = {
            'extensions': 'extensions',
            'category': 'category',
            'id_short': 'idShort',
            'display_name': 'displayName',
            'description': 'description',
            'model_type': 'modelType',
            'semantic_id': 'semanticId',
            'supplemental_semantic_ids': 'supplementalSemanticIds',
            'qualifiers': 'qualifiers',
            'embedded_data_specifications': 'embeddedDataSpecifications',
            'value': 'value'
        }

        self._extensions = extensions
        self._category = category
        self._id_short = id_short
        self._display_name = display_name
        self._description = description
        self._model_type = model_type
        self._semantic_id = semantic_id
        self._supplemental_semantic_ids = supplemental_semantic_ids
        self._qualifiers = qualifiers
        self._embedded_data_specifications = embedded_data_specifications
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'SubmodelElementCollection':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubmodelElementCollection of this SubmodelElementCollection.  # noqa: E501
        :rtype: SubmodelElementCollection
        """
        return util.deserialize_model(dikt, cls)

    @property
    def extensions(self) -> List[Extension]:
        """Gets the extensions of this SubmodelElementCollection.


        :return: The extensions of this SubmodelElementCollection.
        :rtype: List[Extension]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions: List[Extension]):
        """Sets the extensions of this SubmodelElementCollection.


        :param extensions: The extensions of this SubmodelElementCollection.
        :type extensions: List[Extension]
        """
        if extensions is not None and len(extensions) < 1:
            raise ValueError("Invalid value for `extensions`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._extensions = extensions

    @property
    def category(self) -> str:
        """Gets the category of this SubmodelElementCollection.


        :return: The category of this SubmodelElementCollection.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str):
        """Sets the category of this SubmodelElementCollection.


        :param category: The category of this SubmodelElementCollection.
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
        """Gets the id_short of this SubmodelElementCollection.


        :return: The id_short of this SubmodelElementCollection.
        :rtype: object
        """
        return self._id_short

    @id_short.setter
    def id_short(self, id_short: object):
        """Sets the id_short of this SubmodelElementCollection.


        :param id_short: The id_short of this SubmodelElementCollection.
        :type id_short: object
        """

        self._id_short = id_short

    @property
    def display_name(self) -> List[LangStringNameType]:
        """Gets the display_name of this SubmodelElementCollection.


        :return: The display_name of this SubmodelElementCollection.
        :rtype: List[LangStringNameType]
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: List[LangStringNameType]):
        """Sets the display_name of this SubmodelElementCollection.


        :param display_name: The display_name of this SubmodelElementCollection.
        :type display_name: List[LangStringNameType]
        """
        if display_name is not None and len(display_name) < 1:
            raise ValueError("Invalid value for `display_name`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self) -> List[LangStringTextType]:
        """Gets the description of this SubmodelElementCollection.


        :return: The description of this SubmodelElementCollection.
        :rtype: List[LangStringTextType]
        """
        return self._description

    @description.setter
    def description(self, description: List[LangStringTextType]):
        """Sets the description of this SubmodelElementCollection.


        :param description: The description of this SubmodelElementCollection.
        :type description: List[LangStringTextType]
        """
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def model_type(self) -> str:
        """Gets the model_type of this SubmodelElementCollection.


        :return: The model_type of this SubmodelElementCollection.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type: str):
        """Sets the model_type of this SubmodelElementCollection.


        :param model_type: The model_type of this SubmodelElementCollection.
        :type model_type: str
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501
        if model_type is not None and not re.search(r'SubmodelElementCollection', model_type):  # noqa: E501
            raise ValueError("Invalid value for `model_type`, must be a follow pattern or equal to `/SubmodelElementCollection/`")  # noqa: E501

        self._model_type = model_type

    @property
    def semantic_id(self) -> Reference:
        """Gets the semantic_id of this SubmodelElementCollection.


        :return: The semantic_id of this SubmodelElementCollection.
        :rtype: Reference
        """
        return self._semantic_id

    @semantic_id.setter
    def semantic_id(self, semantic_id: Reference):
        """Sets the semantic_id of this SubmodelElementCollection.


        :param semantic_id: The semantic_id of this SubmodelElementCollection.
        :type semantic_id: Reference
        """

        self._semantic_id = semantic_id

    @property
    def supplemental_semantic_ids(self) -> List[Reference]:
        """Gets the supplemental_semantic_ids of this SubmodelElementCollection.


        :return: The supplemental_semantic_ids of this SubmodelElementCollection.
        :rtype: List[Reference]
        """
        return self._supplemental_semantic_ids

    @supplemental_semantic_ids.setter
    def supplemental_semantic_ids(self, supplemental_semantic_ids: List[Reference]):
        """Sets the supplemental_semantic_ids of this SubmodelElementCollection.


        :param supplemental_semantic_ids: The supplemental_semantic_ids of this SubmodelElementCollection.
        :type supplemental_semantic_ids: List[Reference]
        """
        if supplemental_semantic_ids is not None and len(supplemental_semantic_ids) < 1:
            raise ValueError("Invalid value for `supplemental_semantic_ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._supplemental_semantic_ids = supplemental_semantic_ids

    @property
    def qualifiers(self) -> List[Qualifier]:
        """Gets the qualifiers of this SubmodelElementCollection.


        :return: The qualifiers of this SubmodelElementCollection.
        :rtype: List[Qualifier]
        """
        return self._qualifiers

    @qualifiers.setter
    def qualifiers(self, qualifiers: List[Qualifier]):
        """Sets the qualifiers of this SubmodelElementCollection.


        :param qualifiers: The qualifiers of this SubmodelElementCollection.
        :type qualifiers: List[Qualifier]
        """
        if qualifiers is not None and len(qualifiers) < 1:
            raise ValueError("Invalid value for `qualifiers`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._qualifiers = qualifiers

    @property
    def embedded_data_specifications(self) -> List[EmbeddedDataSpecification]:
        """Gets the embedded_data_specifications of this SubmodelElementCollection.


        :return: The embedded_data_specifications of this SubmodelElementCollection.
        :rtype: List[EmbeddedDataSpecification]
        """
        return self._embedded_data_specifications

    @embedded_data_specifications.setter
    def embedded_data_specifications(self, embedded_data_specifications: List[EmbeddedDataSpecification]):
        """Sets the embedded_data_specifications of this SubmodelElementCollection.


        :param embedded_data_specifications: The embedded_data_specifications of this SubmodelElementCollection.
        :type embedded_data_specifications: List[EmbeddedDataSpecification]
        """
        if embedded_data_specifications is not None and len(embedded_data_specifications) < 1:
            raise ValueError("Invalid value for `embedded_data_specifications`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._embedded_data_specifications = embedded_data_specifications

    @property
    def value(self) -> List[SubmodelElementChoice]:
        """Gets the value of this SubmodelElementCollection.


        :return: The value of this SubmodelElementCollection.
        :rtype: List[SubmodelElementChoice]
        """
        return self._value

    @value.setter
    def value(self, value: List[SubmodelElementChoice]):
        """Sets the value of this SubmodelElementCollection.


        :param value: The value of this SubmodelElementCollection.
        :type value: List[SubmodelElementChoice]
        """
        if value is not None and len(value) < 1:
            raise ValueError("Invalid value for `value`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._value = value
