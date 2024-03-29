from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.concept_description import ConceptDescription
from openapi_server.models.paged_result_paging_metadata import PagedResultPagingMetadata
from openapi_server import util

from openapi_server.models.concept_description import ConceptDescription  # noqa: E501
from openapi_server.models.paged_result_paging_metadata import PagedResultPagingMetadata  # noqa: E501

class GetConceptDescriptionsResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, paging_metadata=None, result=None):  # noqa: E501
        """GetConceptDescriptionsResult - a model defined in OpenAPI

        :param paging_metadata: The paging_metadata of this GetConceptDescriptionsResult.  # noqa: E501
        :type paging_metadata: PagedResultPagingMetadata
        :param result: The result of this GetConceptDescriptionsResult.  # noqa: E501
        :type result: List[ConceptDescription]
        """
        self.openapi_types = {
            'paging_metadata': PagedResultPagingMetadata,
            'result': List[ConceptDescription]
        }

        self.attribute_map = {
            'paging_metadata': 'paging_metadata',
            'result': 'result'
        }

        self._paging_metadata = paging_metadata
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'GetConceptDescriptionsResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetConceptDescriptionsResult of this GetConceptDescriptionsResult.  # noqa: E501
        :rtype: GetConceptDescriptionsResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def paging_metadata(self) -> PagedResultPagingMetadata:
        """Gets the paging_metadata of this GetConceptDescriptionsResult.


        :return: The paging_metadata of this GetConceptDescriptionsResult.
        :rtype: PagedResultPagingMetadata
        """
        return self._paging_metadata

    @paging_metadata.setter
    def paging_metadata(self, paging_metadata: PagedResultPagingMetadata):
        """Sets the paging_metadata of this GetConceptDescriptionsResult.


        :param paging_metadata: The paging_metadata of this GetConceptDescriptionsResult.
        :type paging_metadata: PagedResultPagingMetadata
        """

        self._paging_metadata = paging_metadata

    @property
    def result(self) -> List[ConceptDescription]:
        """Gets the result of this GetConceptDescriptionsResult.


        :return: The result of this GetConceptDescriptionsResult.
        :rtype: List[ConceptDescription]
        """
        return self._result

    @result.setter
    def result(self, result: List[ConceptDescription]):
        """Sets the result of this GetConceptDescriptionsResult.


        :param result: The result of this GetConceptDescriptionsResult.
        :type result: List[ConceptDescription]
        """

        self._result = result
