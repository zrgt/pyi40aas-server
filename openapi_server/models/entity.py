from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.embedded_data_specification import EmbeddedDataSpecification
from openapi_server.models.entity_type import EntityType
from openapi_server.models.extension import Extension
from openapi_server.models.lang_string_name_type import LangStringNameType
from openapi_server.models.lang_string_text_type import LangStringTextType
from openapi_server.models.qualifier import Qualifier
from openapi_server.models.reference import Reference
from openapi_server.models.specific_asset_id import SpecificAssetId
from openapi_server.models.submodel_element_choice import SubmodelElementChoice
import re
from openapi_server import util

from openapi_server.models.embedded_data_specification import EmbeddedDataSpecification  # noqa: E501
from openapi_server.models.entity_type import EntityType  # noqa: E501
from openapi_server.models.extension import Extension  # noqa: E501
from openapi_server.models.lang_string_name_type import LangStringNameType  # noqa: E501
from openapi_server.models.lang_string_text_type import LangStringTextType  # noqa: E501
from openapi_server.models.qualifier import Qualifier  # noqa: E501
from openapi_server.models.reference import Reference  # noqa: E501
from openapi_server.models.specific_asset_id import SpecificAssetId  # noqa: E501
from openapi_server.models.submodel_element_choice import SubmodelElementChoice  # noqa: E501
import re  # noqa: E501

class Entity(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, extensions=None, category=None, id_short=None, display_name=None, description=None, model_type=None, semantic_id=None, supplemental_semantic_ids=None, qualifiers=None, embedded_data_specifications=None, statements=None, entity_type=None, global_asset_id=None, specific_asset_ids=None):  # noqa: E501
        """Entity - a model defined in OpenAPI

        :param extensions: The extensions of this Entity.  # noqa: E501
        :type extensions: List[Extension]
        :param category: The category of this Entity.  # noqa: E501
        :type category: str
        :param id_short: The id_short of this Entity.  # noqa: E501
        :type id_short: object
        :param display_name: The display_name of this Entity.  # noqa: E501
        :type display_name: List[LangStringNameType]
        :param description: The description of this Entity.  # noqa: E501
        :type description: List[LangStringTextType]
        :param model_type: The model_type of this Entity.  # noqa: E501
        :type model_type: str
        :param semantic_id: The semantic_id of this Entity.  # noqa: E501
        :type semantic_id: Reference
        :param supplemental_semantic_ids: The supplemental_semantic_ids of this Entity.  # noqa: E501
        :type supplemental_semantic_ids: List[Reference]
        :param qualifiers: The qualifiers of this Entity.  # noqa: E501
        :type qualifiers: List[Qualifier]
        :param embedded_data_specifications: The embedded_data_specifications of this Entity.  # noqa: E501
        :type embedded_data_specifications: List[EmbeddedDataSpecification]
        :param statements: The statements of this Entity.  # noqa: E501
        :type statements: List[SubmodelElementChoice]
        :param entity_type: The entity_type of this Entity.  # noqa: E501
        :type entity_type: EntityType
        :param global_asset_id: The global_asset_id of this Entity.  # noqa: E501
        :type global_asset_id: str
        :param specific_asset_ids: The specific_asset_ids of this Entity.  # noqa: E501
        :type specific_asset_ids: List[SpecificAssetId]
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
            'statements': List[SubmodelElementChoice],
            'entity_type': EntityType,
            'global_asset_id': str,
            'specific_asset_ids': List[SpecificAssetId]
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
            'statements': 'statements',
            'entity_type': 'entityType',
            'global_asset_id': 'globalAssetId',
            'specific_asset_ids': 'specificAssetIds'
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
        self._statements = statements
        self._entity_type = entity_type
        self._global_asset_id = global_asset_id
        self._specific_asset_ids = specific_asset_ids

    @classmethod
    def from_dict(cls, dikt) -> 'Entity':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Entity of this Entity.  # noqa: E501
        :rtype: Entity
        """
        return util.deserialize_model(dikt, cls)

    @property
    def extensions(self) -> List[Extension]:
        """Gets the extensions of this Entity.


        :return: The extensions of this Entity.
        :rtype: List[Extension]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions: List[Extension]):
        """Sets the extensions of this Entity.


        :param extensions: The extensions of this Entity.
        :type extensions: List[Extension]
        """
        if extensions is not None and len(extensions) < 1:
            raise ValueError("Invalid value for `extensions`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._extensions = extensions

    @property
    def category(self) -> str:
        """Gets the category of this Entity.


        :return: The category of this Entity.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str):
        """Sets the category of this Entity.


        :param category: The category of this Entity.
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
        """Gets the id_short of this Entity.


        :return: The id_short of this Entity.
        :rtype: object
        """
        return self._id_short

    @id_short.setter
    def id_short(self, id_short: object):
        """Sets the id_short of this Entity.


        :param id_short: The id_short of this Entity.
        :type id_short: object
        """

        self._id_short = id_short

    @property
    def display_name(self) -> List[LangStringNameType]:
        """Gets the display_name of this Entity.


        :return: The display_name of this Entity.
        :rtype: List[LangStringNameType]
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: List[LangStringNameType]):
        """Sets the display_name of this Entity.


        :param display_name: The display_name of this Entity.
        :type display_name: List[LangStringNameType]
        """
        if display_name is not None and len(display_name) < 1:
            raise ValueError("Invalid value for `display_name`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self) -> List[LangStringTextType]:
        """Gets the description of this Entity.


        :return: The description of this Entity.
        :rtype: List[LangStringTextType]
        """
        return self._description

    @description.setter
    def description(self, description: List[LangStringTextType]):
        """Sets the description of this Entity.


        :param description: The description of this Entity.
        :type description: List[LangStringTextType]
        """
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def model_type(self) -> str:
        """Gets the model_type of this Entity.


        :return: The model_type of this Entity.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type: str):
        """Sets the model_type of this Entity.


        :param model_type: The model_type of this Entity.
        :type model_type: str
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501
        if model_type is not None and not re.search(r'Entity', model_type):  # noqa: E501
            raise ValueError("Invalid value for `model_type`, must be a follow pattern or equal to `/Entity/`")  # noqa: E501

        self._model_type = model_type

    @property
    def semantic_id(self) -> Reference:
        """Gets the semantic_id of this Entity.


        :return: The semantic_id of this Entity.
        :rtype: Reference
        """
        return self._semantic_id

    @semantic_id.setter
    def semantic_id(self, semantic_id: Reference):
        """Sets the semantic_id of this Entity.


        :param semantic_id: The semantic_id of this Entity.
        :type semantic_id: Reference
        """

        self._semantic_id = semantic_id

    @property
    def supplemental_semantic_ids(self) -> List[Reference]:
        """Gets the supplemental_semantic_ids of this Entity.


        :return: The supplemental_semantic_ids of this Entity.
        :rtype: List[Reference]
        """
        return self._supplemental_semantic_ids

    @supplemental_semantic_ids.setter
    def supplemental_semantic_ids(self, supplemental_semantic_ids: List[Reference]):
        """Sets the supplemental_semantic_ids of this Entity.


        :param supplemental_semantic_ids: The supplemental_semantic_ids of this Entity.
        :type supplemental_semantic_ids: List[Reference]
        """
        if supplemental_semantic_ids is not None and len(supplemental_semantic_ids) < 1:
            raise ValueError("Invalid value for `supplemental_semantic_ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._supplemental_semantic_ids = supplemental_semantic_ids

    @property
    def qualifiers(self) -> List[Qualifier]:
        """Gets the qualifiers of this Entity.


        :return: The qualifiers of this Entity.
        :rtype: List[Qualifier]
        """
        return self._qualifiers

    @qualifiers.setter
    def qualifiers(self, qualifiers: List[Qualifier]):
        """Sets the qualifiers of this Entity.


        :param qualifiers: The qualifiers of this Entity.
        :type qualifiers: List[Qualifier]
        """
        if qualifiers is not None and len(qualifiers) < 1:
            raise ValueError("Invalid value for `qualifiers`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._qualifiers = qualifiers

    @property
    def embedded_data_specifications(self) -> List[EmbeddedDataSpecification]:
        """Gets the embedded_data_specifications of this Entity.


        :return: The embedded_data_specifications of this Entity.
        :rtype: List[EmbeddedDataSpecification]
        """
        return self._embedded_data_specifications

    @embedded_data_specifications.setter
    def embedded_data_specifications(self, embedded_data_specifications: List[EmbeddedDataSpecification]):
        """Sets the embedded_data_specifications of this Entity.


        :param embedded_data_specifications: The embedded_data_specifications of this Entity.
        :type embedded_data_specifications: List[EmbeddedDataSpecification]
        """
        if embedded_data_specifications is not None and len(embedded_data_specifications) < 1:
            raise ValueError("Invalid value for `embedded_data_specifications`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._embedded_data_specifications = embedded_data_specifications

    @property
    def statements(self) -> List[SubmodelElementChoice]:
        """Gets the statements of this Entity.


        :return: The statements of this Entity.
        :rtype: List[SubmodelElementChoice]
        """
        return self._statements

    @statements.setter
    def statements(self, statements: List[SubmodelElementChoice]):
        """Sets the statements of this Entity.


        :param statements: The statements of this Entity.
        :type statements: List[SubmodelElementChoice]
        """
        if statements is not None and len(statements) < 1:
            raise ValueError("Invalid value for `statements`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._statements = statements

    @property
    def entity_type(self) -> EntityType:
        """Gets the entity_type of this Entity.


        :return: The entity_type of this Entity.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type: EntityType):
        """Sets the entity_type of this Entity.


        :param entity_type: The entity_type of this Entity.
        :type entity_type: EntityType
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def global_asset_id(self) -> str:
        """Gets the global_asset_id of this Entity.


        :return: The global_asset_id of this Entity.
        :rtype: str
        """
        return self._global_asset_id

    @global_asset_id.setter
    def global_asset_id(self, global_asset_id: str):
        """Sets the global_asset_id of this Entity.


        :param global_asset_id: The global_asset_id of this Entity.
        :type global_asset_id: str
        """
        if global_asset_id is not None and len(global_asset_id) > 2000:
            raise ValueError("Invalid value for `global_asset_id`, length must be less than or equal to `2000`")  # noqa: E501
        if global_asset_id is not None and len(global_asset_id) < 1:
            raise ValueError("Invalid value for `global_asset_id`, length must be greater than or equal to `1`")  # noqa: E501
        if global_asset_id is not None and not re.search(r'^([\t\n\r -퟿-�]|\ud800[\udc00-\udfff]|[\ud801-\udbfe][\udc00-\udfff]|\udbff[\udc00-\udfff])*$', global_asset_id):  # noqa: E501
            raise ValueError("Invalid value for `global_asset_id`, must be a follow pattern or equal to `/^([\t\n\r -퟿-�]|\ud800[\udc00-\udfff]|[\ud801-\udbfe][\udc00-\udfff]|\udbff[\udc00-\udfff])*$/`")  # noqa: E501

        self._global_asset_id = global_asset_id

    @property
    def specific_asset_ids(self) -> List[SpecificAssetId]:
        """Gets the specific_asset_ids of this Entity.


        :return: The specific_asset_ids of this Entity.
        :rtype: List[SpecificAssetId]
        """
        return self._specific_asset_ids

    @specific_asset_ids.setter
    def specific_asset_ids(self, specific_asset_ids: List[SpecificAssetId]):
        """Sets the specific_asset_ids of this Entity.


        :param specific_asset_ids: The specific_asset_ids of this Entity.
        :type specific_asset_ids: List[SpecificAssetId]
        """
        if specific_asset_ids is not None and len(specific_asset_ids) < 1:
            raise ValueError("Invalid value for `specific_asset_ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._specific_asset_ids = specific_asset_ids
