from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.paged_result_paging_metadata import PagedResultPagingMetadata
from openapi_server.models.submodel_element_metadata import SubmodelElementMetadata
from openapi_server import util

from openapi_server.models.paged_result_paging_metadata import PagedResultPagingMetadata  # noqa: E501
from openapi_server.models.submodel_element_metadata import SubmodelElementMetadata  # noqa: E501

class GetSubmodelElementsMetadataResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, paging_metadata=None, result=None):  # noqa: E501
        """GetSubmodelElementsMetadataResult - a model defined in OpenAPI

        :param paging_metadata: The paging_metadata of this GetSubmodelElementsMetadataResult.  # noqa: E501
        :type paging_metadata: PagedResultPagingMetadata
        :param result: The result of this GetSubmodelElementsMetadataResult.  # noqa: E501
        :type result: List[SubmodelElementMetadata]
        """
        self.openapi_types = {
            'paging_metadata': PagedResultPagingMetadata,
            'result': List[SubmodelElementMetadata]
        }

        self.attribute_map = {
            'paging_metadata': 'paging_metadata',
            'result': 'result'
        }

        self._paging_metadata = paging_metadata
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'GetSubmodelElementsMetadataResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetSubmodelElementsMetadataResult of this GetSubmodelElementsMetadataResult.  # noqa: E501
        :rtype: GetSubmodelElementsMetadataResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def paging_metadata(self) -> PagedResultPagingMetadata:
        """Gets the paging_metadata of this GetSubmodelElementsMetadataResult.


        :return: The paging_metadata of this GetSubmodelElementsMetadataResult.
        :rtype: PagedResultPagingMetadata
        """
        return self._paging_metadata

    @paging_metadata.setter
    def paging_metadata(self, paging_metadata: PagedResultPagingMetadata):
        """Sets the paging_metadata of this GetSubmodelElementsMetadataResult.


        :param paging_metadata: The paging_metadata of this GetSubmodelElementsMetadataResult.
        :type paging_metadata: PagedResultPagingMetadata
        """

        self._paging_metadata = paging_metadata

    @property
    def result(self) -> List[SubmodelElementMetadata]:
        """Gets the result of this GetSubmodelElementsMetadataResult.


        :return: The result of this GetSubmodelElementsMetadataResult.
        :rtype: List[SubmodelElementMetadata]
        """
        return self._result

    @result.setter
    def result(self, result: List[SubmodelElementMetadata]):
        """Sets the result of this GetSubmodelElementsMetadataResult.


        :param result: The result of this GetSubmodelElementsMetadataResult.
        :type result: List[SubmodelElementMetadata]
        """

        self._result = result
