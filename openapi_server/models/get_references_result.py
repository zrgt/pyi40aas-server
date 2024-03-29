from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.paged_result_paging_metadata import PagedResultPagingMetadata
from openapi_server.models.reference import Reference
from openapi_server import util

from openapi_server.models.paged_result_paging_metadata import PagedResultPagingMetadata  # noqa: E501
from openapi_server.models.reference import Reference  # noqa: E501

class GetReferencesResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, paging_metadata=None, result=None):  # noqa: E501
        """GetReferencesResult - a model defined in OpenAPI

        :param paging_metadata: The paging_metadata of this GetReferencesResult.  # noqa: E501
        :type paging_metadata: PagedResultPagingMetadata
        :param result: The result of this GetReferencesResult.  # noqa: E501
        :type result: List[Reference]
        """
        self.openapi_types = {
            'paging_metadata': PagedResultPagingMetadata,
            'result': List[Reference]
        }

        self.attribute_map = {
            'paging_metadata': 'paging_metadata',
            'result': 'result'
        }

        self._paging_metadata = paging_metadata
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'GetReferencesResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetReferencesResult of this GetReferencesResult.  # noqa: E501
        :rtype: GetReferencesResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def paging_metadata(self) -> PagedResultPagingMetadata:
        """Gets the paging_metadata of this GetReferencesResult.


        :return: The paging_metadata of this GetReferencesResult.
        :rtype: PagedResultPagingMetadata
        """
        return self._paging_metadata

    @paging_metadata.setter
    def paging_metadata(self, paging_metadata: PagedResultPagingMetadata):
        """Sets the paging_metadata of this GetReferencesResult.


        :param paging_metadata: The paging_metadata of this GetReferencesResult.
        :type paging_metadata: PagedResultPagingMetadata
        """

        self._paging_metadata = paging_metadata

    @property
    def result(self) -> List[Reference]:
        """Gets the result of this GetReferencesResult.


        :return: The result of this GetReferencesResult.
        :rtype: List[Reference]
        """
        return self._result

    @result.setter
    def result(self, result: List[Reference]):
        """Sets the result of this GetReferencesResult.


        :param result: The result of this GetReferencesResult.
        :type result: List[Reference]
        """

        self._result = result
