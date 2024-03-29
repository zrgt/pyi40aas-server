from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.administrative_information import AdministrativeInformation
from openapi_server.models.endpoint import Endpoint
from openapi_server.models.extension import Extension
from openapi_server.models.lang_string_name_type import LangStringNameType
from openapi_server.models.lang_string_text_type import LangStringTextType
from openapi_server.models.reference import Reference
import re
from openapi_server import util

from openapi_server.models.administrative_information import AdministrativeInformation  # noqa: E501
from openapi_server.models.endpoint import Endpoint  # noqa: E501
from openapi_server.models.extension import Extension  # noqa: E501
from openapi_server.models.lang_string_name_type import LangStringNameType  # noqa: E501
from openapi_server.models.lang_string_text_type import LangStringTextType  # noqa: E501
from openapi_server.models.reference import Reference  # noqa: E501
import re  # noqa: E501

class SubmodelDescriptor(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, administration=None, endpoints=None, id_short=None, id=None, semantic_id=None, supplemental_semantic_id=None, description=None, display_name=None, extensions=None):  # noqa: E501
        """SubmodelDescriptor - a model defined in OpenAPI

        :param administration: The administration of this SubmodelDescriptor.  # noqa: E501
        :type administration: AdministrativeInformation
        :param endpoints: The endpoints of this SubmodelDescriptor.  # noqa: E501
        :type endpoints: List[Endpoint]
        :param id_short: The id_short of this SubmodelDescriptor.  # noqa: E501
        :type id_short: str
        :param id: The id of this SubmodelDescriptor.  # noqa: E501
        :type id: str
        :param semantic_id: The semantic_id of this SubmodelDescriptor.  # noqa: E501
        :type semantic_id: Reference
        :param supplemental_semantic_id: The supplemental_semantic_id of this SubmodelDescriptor.  # noqa: E501
        :type supplemental_semantic_id: List[Reference]
        :param description: The description of this SubmodelDescriptor.  # noqa: E501
        :type description: List[LangStringTextType]
        :param display_name: The display_name of this SubmodelDescriptor.  # noqa: E501
        :type display_name: List[LangStringNameType]
        :param extensions: The extensions of this SubmodelDescriptor.  # noqa: E501
        :type extensions: List[Extension]
        """
        self.openapi_types = {
            'administration': AdministrativeInformation,
            'endpoints': List[Endpoint],
            'id_short': str,
            'id': str,
            'semantic_id': Reference,
            'supplemental_semantic_id': List[Reference],
            'description': List[LangStringTextType],
            'display_name': List[LangStringNameType],
            'extensions': List[Extension]
        }

        self.attribute_map = {
            'administration': 'administration',
            'endpoints': 'endpoints',
            'id_short': 'idShort',
            'id': 'id',
            'semantic_id': 'semanticId',
            'supplemental_semantic_id': 'supplementalSemanticId',
            'description': 'description',
            'display_name': 'displayName',
            'extensions': 'extensions'
        }

        self._administration = administration
        self._endpoints = endpoints
        self._id_short = id_short
        self._id = id
        self._semantic_id = semantic_id
        self._supplemental_semantic_id = supplemental_semantic_id
        self._description = description
        self._display_name = display_name
        self._extensions = extensions

    @classmethod
    def from_dict(cls, dikt) -> 'SubmodelDescriptor':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubmodelDescriptor of this SubmodelDescriptor.  # noqa: E501
        :rtype: SubmodelDescriptor
        """
        return util.deserialize_model(dikt, cls)

    @property
    def administration(self) -> AdministrativeInformation:
        """Gets the administration of this SubmodelDescriptor.


        :return: The administration of this SubmodelDescriptor.
        :rtype: AdministrativeInformation
        """
        return self._administration

    @administration.setter
    def administration(self, administration: AdministrativeInformation):
        """Sets the administration of this SubmodelDescriptor.


        :param administration: The administration of this SubmodelDescriptor.
        :type administration: AdministrativeInformation
        """

        self._administration = administration

    @property
    def endpoints(self) -> List[Endpoint]:
        """Gets the endpoints of this SubmodelDescriptor.


        :return: The endpoints of this SubmodelDescriptor.
        :rtype: List[Endpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints: List[Endpoint]):
        """Sets the endpoints of this SubmodelDescriptor.


        :param endpoints: The endpoints of this SubmodelDescriptor.
        :type endpoints: List[Endpoint]
        """
        if endpoints is None:
            raise ValueError("Invalid value for `endpoints`, must not be `None`")  # noqa: E501
        if endpoints is not None and len(endpoints) < 1:
            raise ValueError("Invalid value for `endpoints`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._endpoints = endpoints

    @property
    def id_short(self) -> str:
        """Gets the id_short of this SubmodelDescriptor.


        :return: The id_short of this SubmodelDescriptor.
        :rtype: str
        """
        return self._id_short

    @id_short.setter
    def id_short(self, id_short: str):
        """Sets the id_short of this SubmodelDescriptor.


        :param id_short: The id_short of this SubmodelDescriptor.
        :type id_short: str
        """
        if id_short is not None and len(id_short) > 128:
            raise ValueError("Invalid value for `id_short`, length must be less than or equal to `128`")  # noqa: E501

        self._id_short = id_short

    @property
    def id(self) -> str:
        """Gets the id of this SubmodelDescriptor.


        :return: The id of this SubmodelDescriptor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this SubmodelDescriptor.


        :param id: The id of this SubmodelDescriptor.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 2000:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `2000`")  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501
        if id is not None and not re.search(r'^[\x09\x0A\x0D\x20-\uD7FF\uE000-\uFFFD\U00010000-\U0010FFFF]*$', id):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/^[\x09\x0A\x0D\x20-\uD7FF\uE000-\uFFFD\U00010000-\U0010FFFF]*$/`")  # noqa: E501

        self._id = id

    @property
    def semantic_id(self) -> Reference:
        """Gets the semantic_id of this SubmodelDescriptor.


        :return: The semantic_id of this SubmodelDescriptor.
        :rtype: Reference
        """
        return self._semantic_id

    @semantic_id.setter
    def semantic_id(self, semantic_id: Reference):
        """Sets the semantic_id of this SubmodelDescriptor.


        :param semantic_id: The semantic_id of this SubmodelDescriptor.
        :type semantic_id: Reference
        """

        self._semantic_id = semantic_id

    @property
    def supplemental_semantic_id(self) -> List[Reference]:
        """Gets the supplemental_semantic_id of this SubmodelDescriptor.


        :return: The supplemental_semantic_id of this SubmodelDescriptor.
        :rtype: List[Reference]
        """
        return self._supplemental_semantic_id

    @supplemental_semantic_id.setter
    def supplemental_semantic_id(self, supplemental_semantic_id: List[Reference]):
        """Sets the supplemental_semantic_id of this SubmodelDescriptor.


        :param supplemental_semantic_id: The supplemental_semantic_id of this SubmodelDescriptor.
        :type supplemental_semantic_id: List[Reference]
        """
        if supplemental_semantic_id is not None and len(supplemental_semantic_id) < 1:
            raise ValueError("Invalid value for `supplemental_semantic_id`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._supplemental_semantic_id = supplemental_semantic_id

    @property
    def description(self) -> List[LangStringTextType]:
        """Gets the description of this SubmodelDescriptor.


        :return: The description of this SubmodelDescriptor.
        :rtype: List[LangStringTextType]
        """
        return self._description

    @description.setter
    def description(self, description: List[LangStringTextType]):
        """Sets the description of this SubmodelDescriptor.


        :param description: The description of this SubmodelDescriptor.
        :type description: List[LangStringTextType]
        """

        self._description = description

    @property
    def display_name(self) -> List[LangStringNameType]:
        """Gets the display_name of this SubmodelDescriptor.


        :return: The display_name of this SubmodelDescriptor.
        :rtype: List[LangStringNameType]
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: List[LangStringNameType]):
        """Sets the display_name of this SubmodelDescriptor.


        :param display_name: The display_name of this SubmodelDescriptor.
        :type display_name: List[LangStringNameType]
        """

        self._display_name = display_name

    @property
    def extensions(self) -> List[Extension]:
        """Gets the extensions of this SubmodelDescriptor.


        :return: The extensions of this SubmodelDescriptor.
        :rtype: List[Extension]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions: List[Extension]):
        """Sets the extensions of this SubmodelDescriptor.


        :param extensions: The extensions of this SubmodelDescriptor.
        :type extensions: List[Extension]
        """
        if extensions is not None and len(extensions) < 1:
            raise ValueError("Invalid value for `extensions`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._extensions = extensions
