import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from ..models.base_operation_result import BaseOperationResult  # noqa: E501
from ..models.get_path_items_result import GetPathItemsResult  # noqa: E501
from ..models.get_references_result import GetReferencesResult  # noqa: E501
from ..models.get_submodel_elements_metadata_result import GetSubmodelElementsMetadataResult  # noqa: E501
from ..models.get_submodel_elements_result import GetSubmodelElementsResult  # noqa: E501
from ..models.get_submodel_elements_value_result import GetSubmodelElementsValueResult  # noqa: E501
from ..models.operation_request import OperationRequest  # noqa: E501
from ..models.operation_request_value_only import OperationRequestValueOnly  # noqa: E501
from ..models.operation_result import OperationResult  # noqa: E501
from ..models.operation_result_value_only import OperationResultValueOnly  # noqa: E501
from ..models.reference import Reference  # noqa: E501
from ..models.result import Result  # noqa: E501
from ..models.submodel import Submodel  # noqa: E501
from ..models.submodel_element import SubmodelElement  # noqa: E501
from ..models.submodel_element_metadata import SubmodelElementMetadata  # noqa: E501
from ..models.submodel_element_value import SubmodelElementValue  # noqa: E501
from ..models.submodel_metadata import SubmodelMetadata  # noqa: E501
from ..models.submodel_value import SubmodelValue  # noqa: E501
from .. import util

from basyx.aas import model as basyx_model

CURRENT_SUBMODEL: basyx_model.Submodel

def delete_file_by_path(id_short_path):  # noqa: E501
    """Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def delete_submodel_element_by_path(id_short_path):  # noqa: E501
    """Deletes a submodel element at a specified path within the submodel elements hierarchy

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    se = basyx_model.ModelReference.resolve_idshort_path_from(CURRENT_SUBMODEL, id_short_path.split("/"))
    se.parent.remove_referable()
    CURRENT_SUBMODEL.submodel_element.remove_by_id()
    return 'do some magic!'


def get_all_submodel_elements(limit=None, cursor=None, level=None, extent=None):  # noqa: E501
    """Returns all submodel elements including their hierarchy

     # noqa: E501

    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str
    :param extent: Determines to which extent the resource is being serialized
    :type extent: str

    :rtype: Union[GetSubmodelElementsResult, Tuple[GetSubmodelElementsResult, int], Tuple[GetSubmodelElementsResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_submodel_elements_metadata(limit=None, cursor=None, level=None):  # noqa: E501
    """Returns the metadata attributes of all submodel elements including their hierarchy

     # noqa: E501

    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[GetSubmodelElementsMetadataResult, Tuple[GetSubmodelElementsMetadataResult, int], Tuple[GetSubmodelElementsMetadataResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_submodel_elements_path(limit=None, cursor=None, level=None):  # noqa: E501
    """Returns all submodel elements including their hierarchy in the Path notation

     # noqa: E501

    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[GetPathItemsResult, Tuple[GetPathItemsResult, int], Tuple[GetPathItemsResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_submodel_elements_reference(limit=None, cursor=None, level=None):  # noqa: E501
    """Returns the References of all submodel elements

     # noqa: E501

    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[GetReferencesResult, Tuple[GetReferencesResult, int], Tuple[GetReferencesResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_submodel_elements_value_only(limit=None, cursor=None, level=None, extent=None):  # noqa: E501
    """Returns all submodel elements including their hierarchy in the ValueOnly representation

     # noqa: E501

    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str
    :param extent: Determines to which extent the resource is being serialized
    :type extent: str

    :rtype: Union[GetSubmodelElementsValueResult, Tuple[GetSubmodelElementsValueResult, int], Tuple[GetSubmodelElementsValueResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_file_by_path(id_short_path):  # noqa: E501
    """Downloads file content from a specific submodel element from the Submodel at a specified path

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str

    :rtype: Union[file, Tuple[file, int], Tuple[file, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_operation_async_result(id_short_path, handle_id):  # noqa: E501
    """Returns the Operation result of an asynchronous invoked Operation

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param handle_id: The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)
    :type handle_id: str

    :rtype: Union[OperationResult, Tuple[OperationResult, int], Tuple[OperationResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_operation_async_result_value_only(id_short_path, handle_id):  # noqa: E501
    """Returns the value of the Operation result of an asynchronous invoked Operation

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param handle_id: The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)
    :type handle_id: str

    :rtype: Union[OperationResultValueOnly, Tuple[OperationResultValueOnly, int], Tuple[OperationResultValueOnly, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_operation_async_status(id_short_path, handle_id):  # noqa: E501
    """Returns the Operation status of an asynchronous invoked Operation

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param handle_id: The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)
    :type handle_id: str

    :rtype: Union[BaseOperationResult, Tuple[BaseOperationResult, int], Tuple[BaseOperationResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel(level=None, extent=None):  # noqa: E501
    """Returns the Submodel

     # noqa: E501

    :param level: Determines the structural depth of the respective resource content
    :type level: str
    :param extent: Determines to which extent the resource is being serialized
    :type extent: str

    :rtype: Union[Submodel, Tuple[Submodel, int], Tuple[Submodel, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_element_by_path(id_short_path, level=None, extent=None):  # noqa: E501
    """Returns a specific submodel element from the Submodel at a specified path

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str
    :param extent: Determines to which extent the resource is being serialized
    :type extent: str

    :rtype: Union[SubmodelElement, Tuple[SubmodelElement, int], Tuple[SubmodelElement, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_element_by_path_metadata(id_short_path, cursor=None):  # noqa: E501
    """Returns the matadata attributes of a specific submodel element from the Submodel at a specified path

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str

    :rtype: Union[SubmodelElementMetadata, Tuple[SubmodelElementMetadata, int], Tuple[SubmodelElementMetadata, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_element_by_path_path(id_short_path, level=None):  # noqa: E501
    """Returns a specific submodel element from the Submodel at a specified path in the Path notation

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_element_by_path_reference(id_short_path, level=None):  # noqa: E501
    """Returns the Referene of a specific submodel element from the Submodel at a specified path

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[Reference, Tuple[Reference, int], Tuple[Reference, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_element_by_path_value_only(id_short_path, level=None, extent=None):  # noqa: E501
    """Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str
    :param extent: Determines to which extent the resource is being serialized
    :type extent: str

    :rtype: Union[SubmodelElementValue, Tuple[SubmodelElementValue, int], Tuple[SubmodelElementValue, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_metadata(level=None):  # noqa: E501
    """Returns the metadata attributes of a specific Submodel

     # noqa: E501

    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[SubmodelMetadata, Tuple[SubmodelMetadata, int], Tuple[SubmodelMetadata, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_path(level=None):  # noqa: E501
    """Returns the Submodel in the Path notation

     # noqa: E501

    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[List[str], Tuple[List[str], int], Tuple[List[str], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_reference(level=None):  # noqa: E501
    """Returns the Reference of the Submodel

     # noqa: E501

    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[Reference, Tuple[Reference, int], Tuple[Reference, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_value_only(level=None, extent=None):  # noqa: E501
    """Returns the Submodel in the ValueOnly representation

     # noqa: E501

    :param level: Determines the structural depth of the respective resource content
    :type level: str
    :param extent: Determines to which extent the resource is being serialized
    :type extent: str

    :rtype: Union[SubmodelValue, Tuple[SubmodelValue, int], Tuple[SubmodelValue, int, Dict[str, str]]
    """
    return 'do some magic!'


def invoke_operation(id_short_path, operation_request):  # noqa: E501
    """Synchronously invokes an Operation at a specified path

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param operation_request: Operation request object
    :type operation_request: dict | bytes

    :rtype: Union[OperationResult, Tuple[OperationResult, int], Tuple[OperationResult, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        operation_request = OperationRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def invoke_operation_async(id_short_path, operation_request):  # noqa: E501
    """Asynchronously invokes an Operation at a specified path

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param operation_request: Operation request object
    :type operation_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        operation_request = OperationRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def invoke_operation_async_value_only(id_short_path, operation_request_value_only):  # noqa: E501
    """Asynchronously invokes an Operation at a specified path

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param operation_request_value_only: Operation request object
    :type operation_request_value_only: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        operation_request_value_only = OperationRequestValueOnly.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def invoke_operation_sync_value_only(id_short_path, operation_request_value_only):  # noqa: E501
    """Synchronously invokes an Operation at a specified path

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param operation_request_value_only: Operation request object
    :type operation_request_value_only: dict | bytes

    :rtype: Union[OperationResultValueOnly, Tuple[OperationResultValueOnly, int], Tuple[OperationResultValueOnly, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        operation_request_value_only = OperationRequestValueOnly.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_submodel(submodel, level=None):  # noqa: E501
    """Updates the Submodel

     # noqa: E501

    :param submodel: Submodel object
    :type submodel: dict | bytes
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel = Submodel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_submodel_element_by_path(id_short_path, submodel_element, level=None):  # noqa: E501
    """Updates an existing SubmodelElement

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param submodel_element: SubmodelElement object
    :type submodel_element: dict | bytes
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_element = SubmodelElement.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_submodel_element_by_path_metadata(id_short_path, get_submodel_elements_metadata_result, limit=None, cursor=None, level=None):  # noqa: E501
    """Updates the metadata attributes an existing SubmodelElement

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param get_submodel_elements_metadata_result: Metadata attributes of the SubmodelElement
    :type get_submodel_elements_metadata_result: dict | bytes
    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        get_submodel_elements_metadata_result = GetSubmodelElementsMetadataResult.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_submodel_element_by_path_value_only(id_short_path, get_submodel_elements_value_result, limit=None, cursor=None, level=None):  # noqa: E501
    """Updates the value of an existing SubmodelElement

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param get_submodel_elements_value_result: The SubmodelElement in its ValueOnly representation
    :type get_submodel_elements_value_result: dict | bytes
    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        get_submodel_elements_value_result = GetSubmodelElementsValueResult.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_submodel_metadata(submodel_metadata, level=None):  # noqa: E501
    """Updates the metadata attributes of the Submodel

     # noqa: E501

    :param submodel_metadata: The metadata attributes of the Submodel object
    :type submodel_metadata: dict | bytes
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_metadata = SubmodelMetadata.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_submodel_value_only(submodel_value, level=None):  # noqa: E501
    """Updates the values of the Submodel

     # noqa: E501

    :param submodel_value: Submodel object in its ValueOnly representation
    :type submodel_value: dict | bytes
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_value = SubmodelValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_submodel_element(submodel_element):  # noqa: E501
    """Creates a new submodel element

     # noqa: E501

    :param submodel_element: Requested submodel element
    :type submodel_element: dict | bytes

    :rtype: Union[SubmodelElement, Tuple[SubmodelElement, int], Tuple[SubmodelElement, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_element = SubmodelElement.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_submodel_element_by_path(id_short_path, submodel_element):  # noqa: E501
    """Creates a new submodel element at a specified path within submodel elements hierarchy

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param submodel_element: Requested submodel element
    :type submodel_element: dict | bytes

    :rtype: Union[SubmodelElement, Tuple[SubmodelElement, int], Tuple[SubmodelElement, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_element = SubmodelElement.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_file_by_path(id_short_path, file_name=None, file=None):  # noqa: E501
    """Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param file_name: 
    :type file_name: str
    :param file: 
    :type file: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def put_submodel(submodel, level=None):  # noqa: E501
    """Updates the Submodel

     # noqa: E501

    :param submodel: Submodel object
    :type submodel: dict | bytes
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel = Submodel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_submodel_element_by_path(id_short_path, submodel_element, level=None):  # noqa: E501
    """Updates an existing submodel element at a specified path within submodel elements hierarchy

     # noqa: E501

    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param submodel_element: Requested submodel element
    :type submodel_element: dict | bytes
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_element = SubmodelElement.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
