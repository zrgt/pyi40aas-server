from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.asset_administration_shell import AssetAdministrationShell
from openapi_server.models.concept_description import ConceptDescription
from openapi_server.models.submodel import Submodel
from openapi_server import util

from openapi_server.models.asset_administration_shell import AssetAdministrationShell  # noqa: E501
from openapi_server.models.concept_description import ConceptDescription  # noqa: E501
from openapi_server.models.submodel import Submodel  # noqa: E501

class Environment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, asset_administration_shells=None, submodels=None, concept_descriptions=None):  # noqa: E501
        """Environment - a model defined in OpenAPI

        :param asset_administration_shells: The asset_administration_shells of this Environment.  # noqa: E501
        :type asset_administration_shells: List[AssetAdministrationShell]
        :param submodels: The submodels of this Environment.  # noqa: E501
        :type submodels: List[Submodel]
        :param concept_descriptions: The concept_descriptions of this Environment.  # noqa: E501
        :type concept_descriptions: List[ConceptDescription]
        """
        self.openapi_types = {
            'asset_administration_shells': List[AssetAdministrationShell],
            'submodels': List[Submodel],
            'concept_descriptions': List[ConceptDescription]
        }

        self.attribute_map = {
            'asset_administration_shells': 'assetAdministrationShells',
            'submodels': 'submodels',
            'concept_descriptions': 'conceptDescriptions'
        }

        self._asset_administration_shells = asset_administration_shells
        self._submodels = submodels
        self._concept_descriptions = concept_descriptions

    @classmethod
    def from_dict(cls, dikt) -> 'Environment':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Environment of this Environment.  # noqa: E501
        :rtype: Environment
        """
        return util.deserialize_model(dikt, cls)

    @property
    def asset_administration_shells(self) -> List[AssetAdministrationShell]:
        """Gets the asset_administration_shells of this Environment.


        :return: The asset_administration_shells of this Environment.
        :rtype: List[AssetAdministrationShell]
        """
        return self._asset_administration_shells

    @asset_administration_shells.setter
    def asset_administration_shells(self, asset_administration_shells: List[AssetAdministrationShell]):
        """Sets the asset_administration_shells of this Environment.


        :param asset_administration_shells: The asset_administration_shells of this Environment.
        :type asset_administration_shells: List[AssetAdministrationShell]
        """
        if asset_administration_shells is not None and len(asset_administration_shells) < 1:
            raise ValueError("Invalid value for `asset_administration_shells`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._asset_administration_shells = asset_administration_shells

    @property
    def submodels(self) -> List[Submodel]:
        """Gets the submodels of this Environment.


        :return: The submodels of this Environment.
        :rtype: List[Submodel]
        """
        return self._submodels

    @submodels.setter
    def submodels(self, submodels: List[Submodel]):
        """Sets the submodels of this Environment.


        :param submodels: The submodels of this Environment.
        :type submodels: List[Submodel]
        """
        if submodels is not None and len(submodels) < 1:
            raise ValueError("Invalid value for `submodels`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._submodels = submodels

    @property
    def concept_descriptions(self) -> List[ConceptDescription]:
        """Gets the concept_descriptions of this Environment.


        :return: The concept_descriptions of this Environment.
        :rtype: List[ConceptDescription]
        """
        return self._concept_descriptions

    @concept_descriptions.setter
    def concept_descriptions(self, concept_descriptions: List[ConceptDescription]):
        """Sets the concept_descriptions of this Environment.


        :param concept_descriptions: The concept_descriptions of this Environment.
        :type concept_descriptions: List[ConceptDescription]
        """
        if concept_descriptions is not None and len(concept_descriptions) < 1:
            raise ValueError("Invalid value for `concept_descriptions`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._concept_descriptions = concept_descriptions
