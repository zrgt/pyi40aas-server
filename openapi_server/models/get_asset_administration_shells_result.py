from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.asset_administration_shell import AssetAdministrationShell
from openapi_server.models.paged_result_paging_metadata import PagedResultPagingMetadata
from openapi_server import util

from openapi_server.models.asset_administration_shell import AssetAdministrationShell  # noqa: E501
from openapi_server.models.paged_result_paging_metadata import PagedResultPagingMetadata  # noqa: E501

class GetAssetAdministrationShellsResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, paging_metadata=None, result=None):  # noqa: E501
        """GetAssetAdministrationShellsResult - a model defined in OpenAPI

        :param paging_metadata: The paging_metadata of this GetAssetAdministrationShellsResult.  # noqa: E501
        :type paging_metadata: PagedResultPagingMetadata
        :param result: The result of this GetAssetAdministrationShellsResult.  # noqa: E501
        :type result: List[AssetAdministrationShell]
        """
        self.openapi_types = {
            'paging_metadata': PagedResultPagingMetadata,
            'result': List[AssetAdministrationShell]
        }

        self.attribute_map = {
            'paging_metadata': 'paging_metadata',
            'result': 'result'
        }

        self._paging_metadata = paging_metadata
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'GetAssetAdministrationShellsResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetAssetAdministrationShellsResult of this GetAssetAdministrationShellsResult.  # noqa: E501
        :rtype: GetAssetAdministrationShellsResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def paging_metadata(self) -> PagedResultPagingMetadata:
        """Gets the paging_metadata of this GetAssetAdministrationShellsResult.


        :return: The paging_metadata of this GetAssetAdministrationShellsResult.
        :rtype: PagedResultPagingMetadata
        """
        return self._paging_metadata

    @paging_metadata.setter
    def paging_metadata(self, paging_metadata: PagedResultPagingMetadata):
        """Sets the paging_metadata of this GetAssetAdministrationShellsResult.


        :param paging_metadata: The paging_metadata of this GetAssetAdministrationShellsResult.
        :type paging_metadata: PagedResultPagingMetadata
        """

        self._paging_metadata = paging_metadata

    @property
    def result(self) -> List[AssetAdministrationShell]:
        """Gets the result of this GetAssetAdministrationShellsResult.


        :return: The result of this GetAssetAdministrationShellsResult.
        :rtype: List[AssetAdministrationShell]
        """
        return self._result

    @result.setter
    def result(self, result: List[AssetAdministrationShell]):
        """Sets the result of this GetAssetAdministrationShellsResult.


        :param result: The result of this GetAssetAdministrationShellsResult.
        :type result: List[AssetAdministrationShell]
        """

        self._result = result
