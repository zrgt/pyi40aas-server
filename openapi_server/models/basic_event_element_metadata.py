from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.direction import Direction
from openapi_server.models.embedded_data_specification import EmbeddedDataSpecification
from openapi_server.models.extension import Extension
from openapi_server.models.lang_string_name_type import LangStringNameType
from openapi_server.models.lang_string_text_type import LangStringTextType
from openapi_server.models.model_type import ModelType
from openapi_server.models.modelling_kind import ModellingKind
from openapi_server.models.qualifier import Qualifier
from openapi_server.models.reference import Reference
from openapi_server.models.state_of_event import StateOfEvent
import re
from openapi_server import util

from openapi_server.models.direction import Direction  # noqa: E501
from openapi_server.models.embedded_data_specification import EmbeddedDataSpecification  # noqa: E501
from openapi_server.models.extension import Extension  # noqa: E501
from openapi_server.models.lang_string_name_type import LangStringNameType  # noqa: E501
from openapi_server.models.lang_string_text_type import LangStringTextType  # noqa: E501
from openapi_server.models.model_type import ModelType  # noqa: E501
from openapi_server.models.modelling_kind import ModellingKind  # noqa: E501
from openapi_server.models.qualifier import Qualifier  # noqa: E501
from openapi_server.models.reference import Reference  # noqa: E501
from openapi_server.models.state_of_event import StateOfEvent  # noqa: E501
import re  # noqa: E501

class BasicEventElementMetadata(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, extensions=None, category=None, id_short=None, display_name=None, description=None, model_type=None, embedded_data_specifications=None, semantic_id=None, supplemental_semantic_ids=None, qualifiers=None, kind=None, direction=None, state=None, message_topic=None, message_broker=None, last_update=None, min_interval=None, max_interval=None):  # noqa: E501
        """BasicEventElementMetadata - a model defined in OpenAPI

        :param extensions: The extensions of this BasicEventElementMetadata.  # noqa: E501
        :type extensions: List[Extension]
        :param category: The category of this BasicEventElementMetadata.  # noqa: E501
        :type category: str
        :param id_short: The id_short of this BasicEventElementMetadata.  # noqa: E501
        :type id_short: object
        :param display_name: The display_name of this BasicEventElementMetadata.  # noqa: E501
        :type display_name: List[LangStringNameType]
        :param description: The description of this BasicEventElementMetadata.  # noqa: E501
        :type description: List[LangStringTextType]
        :param model_type: The model_type of this BasicEventElementMetadata.  # noqa: E501
        :type model_type: ModelType
        :param embedded_data_specifications: The embedded_data_specifications of this BasicEventElementMetadata.  # noqa: E501
        :type embedded_data_specifications: List[EmbeddedDataSpecification]
        :param semantic_id: The semantic_id of this BasicEventElementMetadata.  # noqa: E501
        :type semantic_id: Reference
        :param supplemental_semantic_ids: The supplemental_semantic_ids of this BasicEventElementMetadata.  # noqa: E501
        :type supplemental_semantic_ids: List[Reference]
        :param qualifiers: The qualifiers of this BasicEventElementMetadata.  # noqa: E501
        :type qualifiers: List[Qualifier]
        :param kind: The kind of this BasicEventElementMetadata.  # noqa: E501
        :type kind: ModellingKind
        :param direction: The direction of this BasicEventElementMetadata.  # noqa: E501
        :type direction: Direction
        :param state: The state of this BasicEventElementMetadata.  # noqa: E501
        :type state: StateOfEvent
        :param message_topic: The message_topic of this BasicEventElementMetadata.  # noqa: E501
        :type message_topic: str
        :param message_broker: The message_broker of this BasicEventElementMetadata.  # noqa: E501
        :type message_broker: Reference
        :param last_update: The last_update of this BasicEventElementMetadata.  # noqa: E501
        :type last_update: str
        :param min_interval: The min_interval of this BasicEventElementMetadata.  # noqa: E501
        :type min_interval: str
        :param max_interval: The max_interval of this BasicEventElementMetadata.  # noqa: E501
        :type max_interval: str
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
            'kind': ModellingKind,
            'direction': Direction,
            'state': StateOfEvent,
            'message_topic': str,
            'message_broker': Reference,
            'last_update': str,
            'min_interval': str,
            'max_interval': str
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
            'kind': 'kind',
            'direction': 'direction',
            'state': 'state',
            'message_topic': 'messageTopic',
            'message_broker': 'messageBroker',
            'last_update': 'lastUpdate',
            'min_interval': 'minInterval',
            'max_interval': 'maxInterval'
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
        self._direction = direction
        self._state = state
        self._message_topic = message_topic
        self._message_broker = message_broker
        self._last_update = last_update
        self._min_interval = min_interval
        self._max_interval = max_interval

    @classmethod
    def from_dict(cls, dikt) -> 'BasicEventElementMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BasicEventElementMetadata of this BasicEventElementMetadata.  # noqa: E501
        :rtype: BasicEventElementMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def extensions(self) -> List[Extension]:
        """Gets the extensions of this BasicEventElementMetadata.


        :return: The extensions of this BasicEventElementMetadata.
        :rtype: List[Extension]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions: List[Extension]):
        """Sets the extensions of this BasicEventElementMetadata.


        :param extensions: The extensions of this BasicEventElementMetadata.
        :type extensions: List[Extension]
        """
        if extensions is not None and len(extensions) < 1:
            raise ValueError("Invalid value for `extensions`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._extensions = extensions

    @property
    def category(self) -> str:
        """Gets the category of this BasicEventElementMetadata.


        :return: The category of this BasicEventElementMetadata.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str):
        """Sets the category of this BasicEventElementMetadata.


        :param category: The category of this BasicEventElementMetadata.
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
        """Gets the id_short of this BasicEventElementMetadata.


        :return: The id_short of this BasicEventElementMetadata.
        :rtype: object
        """
        return self._id_short

    @id_short.setter
    def id_short(self, id_short: object):
        """Sets the id_short of this BasicEventElementMetadata.


        :param id_short: The id_short of this BasicEventElementMetadata.
        :type id_short: object
        """

        self._id_short = id_short

    @property
    def display_name(self) -> List[LangStringNameType]:
        """Gets the display_name of this BasicEventElementMetadata.


        :return: The display_name of this BasicEventElementMetadata.
        :rtype: List[LangStringNameType]
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: List[LangStringNameType]):
        """Sets the display_name of this BasicEventElementMetadata.


        :param display_name: The display_name of this BasicEventElementMetadata.
        :type display_name: List[LangStringNameType]
        """
        if display_name is not None and len(display_name) < 1:
            raise ValueError("Invalid value for `display_name`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self) -> List[LangStringTextType]:
        """Gets the description of this BasicEventElementMetadata.


        :return: The description of this BasicEventElementMetadata.
        :rtype: List[LangStringTextType]
        """
        return self._description

    @description.setter
    def description(self, description: List[LangStringTextType]):
        """Sets the description of this BasicEventElementMetadata.


        :param description: The description of this BasicEventElementMetadata.
        :type description: List[LangStringTextType]
        """
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def model_type(self) -> ModelType:
        """Gets the model_type of this BasicEventElementMetadata.


        :return: The model_type of this BasicEventElementMetadata.
        :rtype: ModelType
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type: ModelType):
        """Sets the model_type of this BasicEventElementMetadata.


        :param model_type: The model_type of this BasicEventElementMetadata.
        :type model_type: ModelType
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501

        self._model_type = model_type

    @property
    def embedded_data_specifications(self) -> List[EmbeddedDataSpecification]:
        """Gets the embedded_data_specifications of this BasicEventElementMetadata.


        :return: The embedded_data_specifications of this BasicEventElementMetadata.
        :rtype: List[EmbeddedDataSpecification]
        """
        return self._embedded_data_specifications

    @embedded_data_specifications.setter
    def embedded_data_specifications(self, embedded_data_specifications: List[EmbeddedDataSpecification]):
        """Sets the embedded_data_specifications of this BasicEventElementMetadata.


        :param embedded_data_specifications: The embedded_data_specifications of this BasicEventElementMetadata.
        :type embedded_data_specifications: List[EmbeddedDataSpecification]
        """
        if embedded_data_specifications is not None and len(embedded_data_specifications) < 1:
            raise ValueError("Invalid value for `embedded_data_specifications`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._embedded_data_specifications = embedded_data_specifications

    @property
    def semantic_id(self) -> Reference:
        """Gets the semantic_id of this BasicEventElementMetadata.


        :return: The semantic_id of this BasicEventElementMetadata.
        :rtype: Reference
        """
        return self._semantic_id

    @semantic_id.setter
    def semantic_id(self, semantic_id: Reference):
        """Sets the semantic_id of this BasicEventElementMetadata.


        :param semantic_id: The semantic_id of this BasicEventElementMetadata.
        :type semantic_id: Reference
        """

        self._semantic_id = semantic_id

    @property
    def supplemental_semantic_ids(self) -> List[Reference]:
        """Gets the supplemental_semantic_ids of this BasicEventElementMetadata.


        :return: The supplemental_semantic_ids of this BasicEventElementMetadata.
        :rtype: List[Reference]
        """
        return self._supplemental_semantic_ids

    @supplemental_semantic_ids.setter
    def supplemental_semantic_ids(self, supplemental_semantic_ids: List[Reference]):
        """Sets the supplemental_semantic_ids of this BasicEventElementMetadata.


        :param supplemental_semantic_ids: The supplemental_semantic_ids of this BasicEventElementMetadata.
        :type supplemental_semantic_ids: List[Reference]
        """
        if supplemental_semantic_ids is not None and len(supplemental_semantic_ids) < 1:
            raise ValueError("Invalid value for `supplemental_semantic_ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._supplemental_semantic_ids = supplemental_semantic_ids

    @property
    def qualifiers(self) -> List[Qualifier]:
        """Gets the qualifiers of this BasicEventElementMetadata.


        :return: The qualifiers of this BasicEventElementMetadata.
        :rtype: List[Qualifier]
        """
        return self._qualifiers

    @qualifiers.setter
    def qualifiers(self, qualifiers: List[Qualifier]):
        """Sets the qualifiers of this BasicEventElementMetadata.


        :param qualifiers: The qualifiers of this BasicEventElementMetadata.
        :type qualifiers: List[Qualifier]
        """
        if qualifiers is not None and len(qualifiers) < 1:
            raise ValueError("Invalid value for `qualifiers`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._qualifiers = qualifiers

    @property
    def kind(self) -> ModellingKind:
        """Gets the kind of this BasicEventElementMetadata.


        :return: The kind of this BasicEventElementMetadata.
        :rtype: ModellingKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind: ModellingKind):
        """Sets the kind of this BasicEventElementMetadata.


        :param kind: The kind of this BasicEventElementMetadata.
        :type kind: ModellingKind
        """

        self._kind = kind

    @property
    def direction(self) -> Direction:
        """Gets the direction of this BasicEventElementMetadata.


        :return: The direction of this BasicEventElementMetadata.
        :rtype: Direction
        """
        return self._direction

    @direction.setter
    def direction(self, direction: Direction):
        """Sets the direction of this BasicEventElementMetadata.


        :param direction: The direction of this BasicEventElementMetadata.
        :type direction: Direction
        """

        self._direction = direction

    @property
    def state(self) -> StateOfEvent:
        """Gets the state of this BasicEventElementMetadata.


        :return: The state of this BasicEventElementMetadata.
        :rtype: StateOfEvent
        """
        return self._state

    @state.setter
    def state(self, state: StateOfEvent):
        """Sets the state of this BasicEventElementMetadata.


        :param state: The state of this BasicEventElementMetadata.
        :type state: StateOfEvent
        """

        self._state = state

    @property
    def message_topic(self) -> str:
        """Gets the message_topic of this BasicEventElementMetadata.


        :return: The message_topic of this BasicEventElementMetadata.
        :rtype: str
        """
        return self._message_topic

    @message_topic.setter
    def message_topic(self, message_topic: str):
        """Sets the message_topic of this BasicEventElementMetadata.


        :param message_topic: The message_topic of this BasicEventElementMetadata.
        :type message_topic: str
        """
        if message_topic is not None and len(message_topic) > 255:
            raise ValueError("Invalid value for `message_topic`, length must be less than or equal to `255`")  # noqa: E501

        self._message_topic = message_topic

    @property
    def message_broker(self) -> Reference:
        """Gets the message_broker of this BasicEventElementMetadata.


        :return: The message_broker of this BasicEventElementMetadata.
        :rtype: Reference
        """
        return self._message_broker

    @message_broker.setter
    def message_broker(self, message_broker: Reference):
        """Sets the message_broker of this BasicEventElementMetadata.


        :param message_broker: The message_broker of this BasicEventElementMetadata.
        :type message_broker: Reference
        """

        self._message_broker = message_broker

    @property
    def last_update(self) -> str:
        """Gets the last_update of this BasicEventElementMetadata.


        :return: The last_update of this BasicEventElementMetadata.
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update: str):
        """Sets the last_update of this BasicEventElementMetadata.


        :param last_update: The last_update of this BasicEventElementMetadata.
        :type last_update: str
        """

        self._last_update = last_update

    @property
    def min_interval(self) -> str:
        """Gets the min_interval of this BasicEventElementMetadata.


        :return: The min_interval of this BasicEventElementMetadata.
        :rtype: str
        """
        return self._min_interval

    @min_interval.setter
    def min_interval(self, min_interval: str):
        """Sets the min_interval of this BasicEventElementMetadata.


        :param min_interval: The min_interval of this BasicEventElementMetadata.
        :type min_interval: str
        """

        self._min_interval = min_interval

    @property
    def max_interval(self) -> str:
        """Gets the max_interval of this BasicEventElementMetadata.


        :return: The max_interval of this BasicEventElementMetadata.
        :rtype: str
        """
        return self._max_interval

    @max_interval.setter
    def max_interval(self, max_interval: str):
        """Sets the max_interval of this BasicEventElementMetadata.


        :param max_interval: The max_interval of this BasicEventElementMetadata.
        :type max_interval: str
        """

        self._max_interval = max_interval
