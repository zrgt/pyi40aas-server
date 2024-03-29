from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.administrative_information import AdministrativeInformation
from openapi_server.models.asset_kind import AssetKind
from openapi_server.models.endpoint import Endpoint
from openapi_server.models.extension import Extension
from openapi_server.models.lang_string_name_type import LangStringNameType
from openapi_server.models.lang_string_text_type import LangStringTextType
from openapi_server.models.specific_asset_id import SpecificAssetId
from openapi_server.models.submodel_descriptor import SubmodelDescriptor
import re
from openapi_server import util

from openapi_server.models.administrative_information import AdministrativeInformation  # noqa: E501
from openapi_server.models.asset_kind import AssetKind  # noqa: E501
from openapi_server.models.endpoint import Endpoint  # noqa: E501
from openapi_server.models.extension import Extension  # noqa: E501
from openapi_server.models.lang_string_name_type import LangStringNameType  # noqa: E501
from openapi_server.models.lang_string_text_type import LangStringTextType  # noqa: E501
from openapi_server.models.specific_asset_id import SpecificAssetId  # noqa: E501
from openapi_server.models.submodel_descriptor import SubmodelDescriptor  # noqa: E501
import re  # noqa: E501

class AssetAdministrationShellDescriptor(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description=None, display_name=None, extensions=None, administration=None, asset_kind=None, asset_type=None, endpoints=None, global_asset_id=None, id_short=None, id=None, specific_asset_ids=None, submodel_descriptors=None):  # noqa: E501
        """AssetAdministrationShellDescriptor - a model defined in OpenAPI

        :param description: The description of this AssetAdministrationShellDescriptor.  # noqa: E501
        :type description: List[LangStringTextType]
        :param display_name: The display_name of this AssetAdministrationShellDescriptor.  # noqa: E501
        :type display_name: List[LangStringNameType]
        :param extensions: The extensions of this AssetAdministrationShellDescriptor.  # noqa: E501
        :type extensions: List[Extension]
        :param administration: The administration of this AssetAdministrationShellDescriptor.  # noqa: E501
        :type administration: AdministrativeInformation
        :param asset_kind: The asset_kind of this AssetAdministrationShellDescriptor.  # noqa: E501
        :type asset_kind: AssetKind
        :param asset_type: The asset_type of this AssetAdministrationShellDescriptor.  # noqa: E501
        :type asset_type: str
        :param endpoints: The endpoints of this AssetAdministrationShellDescriptor.  # noqa: E501
        :type endpoints: List[Endpoint]
        :param global_asset_id: The global_asset_id of this AssetAdministrationShellDescriptor.  # noqa: E501
        :type global_asset_id: str
        :param id_short: The id_short of this AssetAdministrationShellDescriptor.  # noqa: E501
        :type id_short: str
        :param id: The id of this AssetAdministrationShellDescriptor.  # noqa: E501
        :type id: str
        :param specific_asset_ids: The specific_asset_ids of this AssetAdministrationShellDescriptor.  # noqa: E501
        :type specific_asset_ids: List[SpecificAssetId]
        :param submodel_descriptors: The submodel_descriptors of this AssetAdministrationShellDescriptor.  # noqa: E501
        :type submodel_descriptors: List[SubmodelDescriptor]
        """
        self.openapi_types = {
            'description': List[LangStringTextType],
            'display_name': List[LangStringNameType],
            'extensions': List[Extension],
            'administration': AdministrativeInformation,
            'asset_kind': AssetKind,
            'asset_type': str,
            'endpoints': List[Endpoint],
            'global_asset_id': str,
            'id_short': str,
            'id': str,
            'specific_asset_ids': List[SpecificAssetId],
            'submodel_descriptors': List[SubmodelDescriptor]
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'extensions': 'extensions',
            'administration': 'administration',
            'asset_kind': 'assetKind',
            'asset_type': 'assetType',
            'endpoints': 'endpoints',
            'global_asset_id': 'globalAssetId',
            'id_short': 'idShort',
            'id': 'id',
            'specific_asset_ids': 'specificAssetIds',
            'submodel_descriptors': 'submodelDescriptors'
        }

        self._description = description
        self._display_name = display_name
        self._extensions = extensions
        self._administration = administration
        self._asset_kind = asset_kind
        self._asset_type = asset_type
        self._endpoints = endpoints
        self._global_asset_id = global_asset_id
        self._id_short = id_short
        self._id = id
        self._specific_asset_ids = specific_asset_ids
        self._submodel_descriptors = submodel_descriptors

    @classmethod
    def from_dict(cls, dikt) -> 'AssetAdministrationShellDescriptor':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AssetAdministrationShellDescriptor of this AssetAdministrationShellDescriptor.  # noqa: E501
        :rtype: AssetAdministrationShellDescriptor
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self) -> List[LangStringTextType]:
        """Gets the description of this AssetAdministrationShellDescriptor.


        :return: The description of this AssetAdministrationShellDescriptor.
        :rtype: List[LangStringTextType]
        """
        return self._description

    @description.setter
    def description(self, description: List[LangStringTextType]):
        """Sets the description of this AssetAdministrationShellDescriptor.


        :param description: The description of this AssetAdministrationShellDescriptor.
        :type description: List[LangStringTextType]
        """

        self._description = description

    @property
    def display_name(self) -> List[LangStringNameType]:
        """Gets the display_name of this AssetAdministrationShellDescriptor.


        :return: The display_name of this AssetAdministrationShellDescriptor.
        :rtype: List[LangStringNameType]
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: List[LangStringNameType]):
        """Sets the display_name of this AssetAdministrationShellDescriptor.


        :param display_name: The display_name of this AssetAdministrationShellDescriptor.
        :type display_name: List[LangStringNameType]
        """

        self._display_name = display_name

    @property
    def extensions(self) -> List[Extension]:
        """Gets the extensions of this AssetAdministrationShellDescriptor.


        :return: The extensions of this AssetAdministrationShellDescriptor.
        :rtype: List[Extension]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions: List[Extension]):
        """Sets the extensions of this AssetAdministrationShellDescriptor.


        :param extensions: The extensions of this AssetAdministrationShellDescriptor.
        :type extensions: List[Extension]
        """
        if extensions is not None and len(extensions) < 1:
            raise ValueError("Invalid value for `extensions`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._extensions = extensions

    @property
    def administration(self) -> AdministrativeInformation:
        """Gets the administration of this AssetAdministrationShellDescriptor.


        :return: The administration of this AssetAdministrationShellDescriptor.
        :rtype: AdministrativeInformation
        """
        return self._administration

    @administration.setter
    def administration(self, administration: AdministrativeInformation):
        """Sets the administration of this AssetAdministrationShellDescriptor.


        :param administration: The administration of this AssetAdministrationShellDescriptor.
        :type administration: AdministrativeInformation
        """

        self._administration = administration

    @property
    def asset_kind(self) -> AssetKind:
        """Gets the asset_kind of this AssetAdministrationShellDescriptor.


        :return: The asset_kind of this AssetAdministrationShellDescriptor.
        :rtype: AssetKind
        """
        return self._asset_kind

    @asset_kind.setter
    def asset_kind(self, asset_kind: AssetKind):
        """Sets the asset_kind of this AssetAdministrationShellDescriptor.


        :param asset_kind: The asset_kind of this AssetAdministrationShellDescriptor.
        :type asset_kind: AssetKind
        """

        self._asset_kind = asset_kind

    @property
    def asset_type(self) -> str:
        """Gets the asset_type of this AssetAdministrationShellDescriptor.


        :return: The asset_type of this AssetAdministrationShellDescriptor.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type: str):
        """Sets the asset_type of this AssetAdministrationShellDescriptor.


        :param asset_type: The asset_type of this AssetAdministrationShellDescriptor.
        :type asset_type: str
        """
        if asset_type is not None and len(asset_type) > 2000:
            raise ValueError("Invalid value for `asset_type`, length must be less than or equal to `2000`")  # noqa: E501
        if asset_type is not None and len(asset_type) < 1:
            raise ValueError("Invalid value for `asset_type`, length must be greater than or equal to `1`")  # noqa: E501
        if asset_type is not None and not re.search(r'^[\x09\x0A\x0D\x20-\uD7FF\uE000-\uFFFD\U00010000-\U0010FFFF]*$', asset_type):  # noqa: E501
            raise ValueError("Invalid value for `asset_type`, must be a follow pattern or equal to `/^[\x09\x0A\x0D\x20-\uD7FF\uE000-\uFFFD\U00010000-\U0010FFFF]*$/`")  # noqa: E501

        self._asset_type = asset_type

    @property
    def endpoints(self) -> List[Endpoint]:
        """Gets the endpoints of this AssetAdministrationShellDescriptor.


        :return: The endpoints of this AssetAdministrationShellDescriptor.
        :rtype: List[Endpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints: List[Endpoint]):
        """Sets the endpoints of this AssetAdministrationShellDescriptor.


        :param endpoints: The endpoints of this AssetAdministrationShellDescriptor.
        :type endpoints: List[Endpoint]
        """
        if endpoints is not None and len(endpoints) < 1:
            raise ValueError("Invalid value for `endpoints`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._endpoints = endpoints

    @property
    def global_asset_id(self) -> str:
        """Gets the global_asset_id of this AssetAdministrationShellDescriptor.


        :return: The global_asset_id of this AssetAdministrationShellDescriptor.
        :rtype: str
        """
        return self._global_asset_id

    @global_asset_id.setter
    def global_asset_id(self, global_asset_id: str):
        """Sets the global_asset_id of this AssetAdministrationShellDescriptor.


        :param global_asset_id: The global_asset_id of this AssetAdministrationShellDescriptor.
        :type global_asset_id: str
        """
        if global_asset_id is not None and len(global_asset_id) > 2000:
            raise ValueError("Invalid value for `global_asset_id`, length must be less than or equal to `2000`")  # noqa: E501
        if global_asset_id is not None and len(global_asset_id) < 1:
            raise ValueError("Invalid value for `global_asset_id`, length must be greater than or equal to `1`")  # noqa: E501
        if global_asset_id is not None and not re.search(r'^[\x09\x0A\x0D\x20-\uD7FF\uE000-\uFFFD\U00010000-\U0010FFFF]*$', global_asset_id):  # noqa: E501
            raise ValueError("Invalid value for `global_asset_id`, must be a follow pattern or equal to `/^[\x09\x0A\x0D\x20-\uD7FF\uE000-\uFFFD\U00010000-\U0010FFFF]*$/`")  # noqa: E501

        self._global_asset_id = global_asset_id

    @property
    def id_short(self) -> str:
        """Gets the id_short of this AssetAdministrationShellDescriptor.


        :return: The id_short of this AssetAdministrationShellDescriptor.
        :rtype: str
        """
        return self._id_short

    @id_short.setter
    def id_short(self, id_short: str):
        """Sets the id_short of this AssetAdministrationShellDescriptor.


        :param id_short: The id_short of this AssetAdministrationShellDescriptor.
        :type id_short: str
        """
        if id_short is not None and len(id_short) > 128:
            raise ValueError("Invalid value for `id_short`, length must be less than or equal to `128`")  # noqa: E501

        self._id_short = id_short

    @property
    def id(self) -> str:
        """Gets the id of this AssetAdministrationShellDescriptor.


        :return: The id of this AssetAdministrationShellDescriptor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this AssetAdministrationShellDescriptor.


        :param id: The id of this AssetAdministrationShellDescriptor.
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
    def specific_asset_ids(self) -> List[SpecificAssetId]:
        """Gets the specific_asset_ids of this AssetAdministrationShellDescriptor.


        :return: The specific_asset_ids of this AssetAdministrationShellDescriptor.
        :rtype: List[SpecificAssetId]
        """
        return self._specific_asset_ids

    @specific_asset_ids.setter
    def specific_asset_ids(self, specific_asset_ids: List[SpecificAssetId]):
        """Sets the specific_asset_ids of this AssetAdministrationShellDescriptor.


        :param specific_asset_ids: The specific_asset_ids of this AssetAdministrationShellDescriptor.
        :type specific_asset_ids: List[SpecificAssetId]
        """

        self._specific_asset_ids = specific_asset_ids

    @property
    def submodel_descriptors(self) -> List[SubmodelDescriptor]:
        """Gets the submodel_descriptors of this AssetAdministrationShellDescriptor.


        :return: The submodel_descriptors of this AssetAdministrationShellDescriptor.
        :rtype: List[SubmodelDescriptor]
        """
        return self._submodel_descriptors

    @submodel_descriptors.setter
    def submodel_descriptors(self, submodel_descriptors: List[SubmodelDescriptor]):
        """Sets the submodel_descriptors of this AssetAdministrationShellDescriptor.


        :param submodel_descriptors: The submodel_descriptors of this AssetAdministrationShellDescriptor.
        :type submodel_descriptors: List[SubmodelDescriptor]
        """

        self._submodel_descriptors = submodel_descriptors
