import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.get_submodel_descriptors_result import GetSubmodelDescriptorsResult  # noqa: E501
from openapi_server.models.result import Result  # noqa: E501
from openapi_server.models.submodel_descriptor import SubmodelDescriptor  # noqa: E501
from openapi_server import util


def delete_submodel_descriptor_by_id(submodel_identifier):  # noqa: E501
    """Deletes a Submodel Descriptor, i.e. de-registers a submodel

     # noqa: E501

    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_submodel_descriptors(limit=None, cursor=None):  # noqa: E501
    """Returns all Submodel Descriptors

     # noqa: E501

    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str

    :rtype: Union[GetSubmodelDescriptorsResult, Tuple[GetSubmodelDescriptorsResult, int], Tuple[GetSubmodelDescriptorsResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_descriptor_by_id(submodel_identifier):  # noqa: E501
    """Returns a specific Submodel Descriptor

     # noqa: E501

    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str

    :rtype: Union[SubmodelDescriptor, Tuple[SubmodelDescriptor, int], Tuple[SubmodelDescriptor, int, Dict[str, str]]
    """
    return 'do some magic!'


def post_submodel_descriptor(submodel_descriptor):  # noqa: E501
    """Creates a new Submodel Descriptor, i.e. registers a submodel

     # noqa: E501

    :param submodel_descriptor: Submodel Descriptor object
    :type submodel_descriptor: dict | bytes

    :rtype: Union[SubmodelDescriptor, Tuple[SubmodelDescriptor, int], Tuple[SubmodelDescriptor, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_descriptor = SubmodelDescriptor.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_submodel_descriptor_by_id(submodel_identifier, submodel_descriptor):  # noqa: E501
    """Updates an existing Submodel Descriptor

     # noqa: E501

    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param submodel_descriptor: Submodel Descriptor object
    :type submodel_descriptor: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_descriptor = SubmodelDescriptor.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
