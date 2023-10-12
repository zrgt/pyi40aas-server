from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.paged_result_paging_metadata import PagedResultPagingMetadata
from openapi_server import util

from openapi_server.models.paged_result_paging_metadata import PagedResultPagingMetadata  # noqa: E501

class GetPathItemsResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, paging_metadata=None, result=None):  # noqa: E501
        """GetPathItemsResult - a model defined in OpenAPI

        :param paging_metadata: The paging_metadata of this GetPathItemsResult.  # noqa: E501
        :type paging_metadata: PagedResultPagingMetadata
        :param result: The result of this GetPathItemsResult.  # noqa: E501
        :type result: List[str]
        """
        self.openapi_types = {
            'paging_metadata': PagedResultPagingMetadata,
            'result': List[str]
        }

        self.attribute_map = {
            'paging_metadata': 'paging_metadata',
            'result': 'result'
        }

        self._paging_metadata = paging_metadata
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'GetPathItemsResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetPathItemsResult of this GetPathItemsResult.  # noqa: E501
        :rtype: GetPathItemsResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def paging_metadata(self) -> PagedResultPagingMetadata:
        """Gets the paging_metadata of this GetPathItemsResult.


        :return: The paging_metadata of this GetPathItemsResult.
        :rtype: PagedResultPagingMetadata
        """
        return self._paging_metadata

    @paging_metadata.setter
    def paging_metadata(self, paging_metadata: PagedResultPagingMetadata):
        """Sets the paging_metadata of this GetPathItemsResult.


        :param paging_metadata: The paging_metadata of this GetPathItemsResult.
        :type paging_metadata: PagedResultPagingMetadata
        """

        self._paging_metadata = paging_metadata

    @property
    def result(self) -> List[str]:
        """Gets the result of this GetPathItemsResult.


        :return: The result of this GetPathItemsResult.
        :rtype: List[str]
        """
        return self._result

    @result.setter
    def result(self, result: List[str]):
        """Sets the result of this GetPathItemsResult.


        :param result: The result of this GetPathItemsResult.
        :type result: List[str]
        """

        self._result = result
