from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.administrative_information import AdministrativeInformation
from openapi_server.models.asset_information import AssetInformation
from openapi_server.models.embedded_data_specification import EmbeddedDataSpecification
from openapi_server.models.extension import Extension
from openapi_server.models.lang_string_name_type import LangStringNameType
from openapi_server.models.lang_string_text_type import LangStringTextType
from openapi_server.models.reference import Reference
import re
from openapi_server import util

from openapi_server.models.administrative_information import AdministrativeInformation  # noqa: E501
from openapi_server.models.asset_information import AssetInformation  # noqa: E501
from openapi_server.models.embedded_data_specification import EmbeddedDataSpecification  # noqa: E501
from openapi_server.models.extension import Extension  # noqa: E501
from openapi_server.models.lang_string_name_type import LangStringNameType  # noqa: E501
from openapi_server.models.lang_string_text_type import LangStringTextType  # noqa: E501
from openapi_server.models.reference import Reference  # noqa: E501
import re  # noqa: E501

class AssetAdministrationShell(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, extensions=None, category=None, id_short=None, display_name=None, description=None, model_type=None, administration=None, id=None, embedded_data_specifications=None, derived_from=None, asset_information=None, submodels=None):  # noqa: E501
        """AssetAdministrationShell - a model defined in OpenAPI

        :param extensions: The extensions of this AssetAdministrationShell.  # noqa: E501
        :type extensions: List[Extension]
        :param category: The category of this AssetAdministrationShell.  # noqa: E501
        :type category: str
        :param id_short: The id_short of this AssetAdministrationShell.  # noqa: E501
        :type id_short: object
        :param display_name: The display_name of this AssetAdministrationShell.  # noqa: E501
        :type display_name: List[LangStringNameType]
        :param description: The description of this AssetAdministrationShell.  # noqa: E501
        :type description: List[LangStringTextType]
        :param model_type: The model_type of this AssetAdministrationShell.  # noqa: E501
        :type model_type: str
        :param administration: The administration of this AssetAdministrationShell.  # noqa: E501
        :type administration: AdministrativeInformation
        :param id: The id of this AssetAdministrationShell.  # noqa: E501
        :type id: str
        :param embedded_data_specifications: The embedded_data_specifications of this AssetAdministrationShell.  # noqa: E501
        :type embedded_data_specifications: List[EmbeddedDataSpecification]
        :param derived_from: The derived_from of this AssetAdministrationShell.  # noqa: E501
        :type derived_from: Reference
        :param asset_information: The asset_information of this AssetAdministrationShell.  # noqa: E501
        :type asset_information: AssetInformation
        :param submodels: The submodels of this AssetAdministrationShell.  # noqa: E501
        :type submodels: List[Reference]
        """
        self.openapi_types = {
            'extensions': List[Extension],
            'category': str,
            'id_short': object,
            'display_name': List[LangStringNameType],
            'description': List[LangStringTextType],
            'model_type': str,
            'administration': AdministrativeInformation,
            'id': str,
            'embedded_data_specifications': List[EmbeddedDataSpecification],
            'derived_from': Reference,
            'asset_information': AssetInformation,
            'submodels': List[Reference]
        }

        self.attribute_map = {
            'extensions': 'extensions',
            'category': 'category',
            'id_short': 'idShort',
            'display_name': 'displayName',
            'description': 'description',
            'model_type': 'modelType',
            'administration': 'administration',
            'id': 'id',
            'embedded_data_specifications': 'embeddedDataSpecifications',
            'derived_from': 'derivedFrom',
            'asset_information': 'assetInformation',
            'submodels': 'submodels'
        }

        self._extensions = extensions
        self._category = category
        self._id_short = id_short
        self._display_name = display_name
        self._description = description
        self._model_type = model_type
        self._administration = administration
        self._id = id
        self._embedded_data_specifications = embedded_data_specifications
        self._derived_from = derived_from
        self._asset_information = asset_information
        self._submodels = submodels

    @classmethod
    def from_dict(cls, dikt) -> 'AssetAdministrationShell':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AssetAdministrationShell of this AssetAdministrationShell.  # noqa: E501
        :rtype: AssetAdministrationShell
        """
        return util.deserialize_model(dikt, cls)

    @property
    def extensions(self) -> List[Extension]:
        """Gets the extensions of this AssetAdministrationShell.


        :return: The extensions of this AssetAdministrationShell.
        :rtype: List[Extension]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions: List[Extension]):
        """Sets the extensions of this AssetAdministrationShell.


        :param extensions: The extensions of this AssetAdministrationShell.
        :type extensions: List[Extension]
        """
        if extensions is not None and len(extensions) < 1:
            raise ValueError("Invalid value for `extensions`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._extensions = extensions

    @property
    def category(self) -> str:
        """Gets the category of this AssetAdministrationShell.


        :return: The category of this AssetAdministrationShell.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str):
        """Sets the category of this AssetAdministrationShell.


        :param category: The category of this AssetAdministrationShell.
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
        """Gets the id_short of this AssetAdministrationShell.


        :return: The id_short of this AssetAdministrationShell.
        :rtype: object
        """
        return self._id_short

    @id_short.setter
    def id_short(self, id_short: object):
        """Sets the id_short of this AssetAdministrationShell.


        :param id_short: The id_short of this AssetAdministrationShell.
        :type id_short: object
        """

        self._id_short = id_short

    @property
    def display_name(self) -> List[LangStringNameType]:
        """Gets the display_name of this AssetAdministrationShell.


        :return: The display_name of this AssetAdministrationShell.
        :rtype: List[LangStringNameType]
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: List[LangStringNameType]):
        """Sets the display_name of this AssetAdministrationShell.


        :param display_name: The display_name of this AssetAdministrationShell.
        :type display_name: List[LangStringNameType]
        """
        if display_name is not None and len(display_name) < 1:
            raise ValueError("Invalid value for `display_name`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self) -> List[LangStringTextType]:
        """Gets the description of this AssetAdministrationShell.


        :return: The description of this AssetAdministrationShell.
        :rtype: List[LangStringTextType]
        """
        return self._description

    @description.setter
    def description(self, description: List[LangStringTextType]):
        """Sets the description of this AssetAdministrationShell.


        :param description: The description of this AssetAdministrationShell.
        :type description: List[LangStringTextType]
        """
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def model_type(self) -> str:
        """Gets the model_type of this AssetAdministrationShell.


        :return: The model_type of this AssetAdministrationShell.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type: str):
        """Sets the model_type of this AssetAdministrationShell.


        :param model_type: The model_type of this AssetAdministrationShell.
        :type model_type: str
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501
        if model_type is not None and not re.search(r'AssetAdministrationShell', model_type):  # noqa: E501
            raise ValueError("Invalid value for `model_type`, must be a follow pattern or equal to `/AssetAdministrationShell/`")  # noqa: E501

        self._model_type = model_type

    @property
    def administration(self) -> AdministrativeInformation:
        """Gets the administration of this AssetAdministrationShell.


        :return: The administration of this AssetAdministrationShell.
        :rtype: AdministrativeInformation
        """
        return self._administration

    @administration.setter
    def administration(self, administration: AdministrativeInformation):
        """Sets the administration of this AssetAdministrationShell.


        :param administration: The administration of this AssetAdministrationShell.
        :type administration: AdministrativeInformation
        """

        self._administration = administration

    @property
    def id(self) -> str:
        """Gets the id of this AssetAdministrationShell.


        :return: The id of this AssetAdministrationShell.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this AssetAdministrationShell.


        :param id: The id of this AssetAdministrationShell.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 2000:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `2000`")  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501
        if id is not None and not re.search(r'^([\t\n\r -퟿-�]|\ud800[\udc00-\udfff]|[\ud801-\udbfe][\udc00-\udfff]|\udbff[\udc00-\udfff])*$', id):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/^([\t\n\r -퟿-�]|\ud800[\udc00-\udfff]|[\ud801-\udbfe][\udc00-\udfff]|\udbff[\udc00-\udfff])*$/`")  # noqa: E501

        self._id = id

    @property
    def embedded_data_specifications(self) -> List[EmbeddedDataSpecification]:
        """Gets the embedded_data_specifications of this AssetAdministrationShell.


        :return: The embedded_data_specifications of this AssetAdministrationShell.
        :rtype: List[EmbeddedDataSpecification]
        """
        return self._embedded_data_specifications

    @embedded_data_specifications.setter
    def embedded_data_specifications(self, embedded_data_specifications: List[EmbeddedDataSpecification]):
        """Sets the embedded_data_specifications of this AssetAdministrationShell.


        :param embedded_data_specifications: The embedded_data_specifications of this AssetAdministrationShell.
        :type embedded_data_specifications: List[EmbeddedDataSpecification]
        """
        if embedded_data_specifications is not None and len(embedded_data_specifications) < 1:
            raise ValueError("Invalid value for `embedded_data_specifications`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._embedded_data_specifications = embedded_data_specifications

    @property
    def derived_from(self) -> Reference:
        """Gets the derived_from of this AssetAdministrationShell.


        :return: The derived_from of this AssetAdministrationShell.
        :rtype: Reference
        """
        return self._derived_from

    @derived_from.setter
    def derived_from(self, derived_from: Reference):
        """Sets the derived_from of this AssetAdministrationShell.


        :param derived_from: The derived_from of this AssetAdministrationShell.
        :type derived_from: Reference
        """

        self._derived_from = derived_from

    @property
    def asset_information(self) -> AssetInformation:
        """Gets the asset_information of this AssetAdministrationShell.


        :return: The asset_information of this AssetAdministrationShell.
        :rtype: AssetInformation
        """
        return self._asset_information

    @asset_information.setter
    def asset_information(self, asset_information: AssetInformation):
        """Sets the asset_information of this AssetAdministrationShell.


        :param asset_information: The asset_information of this AssetAdministrationShell.
        :type asset_information: AssetInformation
        """
        if asset_information is None:
            raise ValueError("Invalid value for `asset_information`, must not be `None`")  # noqa: E501

        self._asset_information = asset_information

    @property
    def submodels(self) -> List[Reference]:
        """Gets the submodels of this AssetAdministrationShell.


        :return: The submodels of this AssetAdministrationShell.
        :rtype: List[Reference]
        """
        return self._submodels

    @submodels.setter
    def submodels(self, submodels: List[Reference]):
        """Sets the submodels of this AssetAdministrationShell.


        :param submodels: The submodels of this AssetAdministrationShell.
        :type submodels: List[Reference]
        """
        if submodels is not None and len(submodels) < 1:
            raise ValueError("Invalid value for `submodels`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._submodels = submodels
