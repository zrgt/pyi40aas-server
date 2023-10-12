import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.asset_administration_shell import AssetAdministrationShell  # noqa: E501
from openapi_server.models.asset_information import AssetInformation  # noqa: E501
from openapi_server.models.base_operation_result import BaseOperationResult  # noqa: E501
from openapi_server.models.get_asset_administration_shells_result import GetAssetAdministrationShellsResult  # noqa: E501
from openapi_server.models.get_path_items_result import GetPathItemsResult  # noqa: E501
from openapi_server.models.get_references_result import GetReferencesResult  # noqa: E501
from openapi_server.models.get_submodel_elements_metadata_result import GetSubmodelElementsMetadataResult  # noqa: E501
from openapi_server.models.get_submodel_elements_result import GetSubmodelElementsResult  # noqa: E501
from openapi_server.models.get_submodel_elements_value_result import GetSubmodelElementsValueResult  # noqa: E501
from openapi_server.models.operation_request import OperationRequest  # noqa: E501
from openapi_server.models.operation_request_value_only import OperationRequestValueOnly  # noqa: E501
from openapi_server.models.operation_result import OperationResult  # noqa: E501
from openapi_server.models.operation_result_value_only import OperationResultValueOnly  # noqa: E501
from openapi_server.models.reference import Reference  # noqa: E501
from openapi_server.models.result import Result  # noqa: E501
from openapi_server.models.submodel import Submodel  # noqa: E501
from openapi_server.models.submodel_element import SubmodelElement  # noqa: E501
from openapi_server.models.submodel_element_metadata import SubmodelElementMetadata  # noqa: E501
from openapi_server.models.submodel_element_value import SubmodelElementValue  # noqa: E501
from openapi_server.models.submodel_metadata import SubmodelMetadata  # noqa: E501
from openapi_server.models.submodel_value import SubmodelValue  # noqa: E501
from openapi_server import util


def delete_asset_administration_shell_by_id(aas_identifier):  # noqa: E501
    """Deletes an Asset Administration Shell

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def delete_file_by_path_aas_repository(aas_identifier, submodel_identifier, id_short_path):  # noqa: E501
    """Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def delete_submodel_by_id_aas_repository(aas_identifier, submodel_identifier):  # noqa: E501
    """Deletes the submodel from the Asset Administration Shell and the Repository.

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def delete_submodel_element_by_path_aas_repository(aas_identifier, submodel_identifier, id_short_path):  # noqa: E501
    """Deletes a submodel element at a specified path within the submodel elements hierarchy

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def delete_submodel_reference_by_id_aas_repository(aas_identifier, submodel_identifier):  # noqa: E501
    """Deletes the submodel reference from the Asset Administration Shell. Does not delete the submodel itself!

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def delete_thumbnail_aas_repository(aas_identifier):  # noqa: E501
    """delete_thumbnail_aas_repository

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_asset_administration_shells(asset_ids=None, id_short=None, limit=None, cursor=None):  # noqa: E501
    """Returns all Asset Administration Shells

     # noqa: E501

    :param asset_ids: A list of specific Asset identifiers. Each Asset identifier is a base64-url-encoded [SpecificAssetId](https://api.swaggerhub.com/domains/Plattform_i40/Part1-MetaModel-Schemas/V3.0.1#/components/schemas/SpecificAssetId)
    :type asset_ids: List[str]
    :param id_short: The Asset Administration Shell’s IdShort
    :type id_short: str
    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str

    :rtype: Union[GetAssetAdministrationShellsResult, Tuple[GetAssetAdministrationShellsResult, int], Tuple[GetAssetAdministrationShellsResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_asset_administration_shells_reference(asset_ids=None, id_short=None, limit=None, cursor=None):  # noqa: E501
    """Returns References to all Asset Administration Shells

     # noqa: E501

    :param asset_ids: A list of specific Asset identifiers. Each Asset identifier is a base64-url-encoded [SpecificAssetId](https://api.swaggerhub.com/domains/Plattform_i40/Part1-MetaModel-Schemas/V3.0.1#/components/schemas/SpecificAssetId)
    :type asset_ids: List[str]
    :param id_short: The Asset Administration Shell’s IdShort
    :type id_short: str
    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str

    :rtype: Union[GetReferencesResult, Tuple[GetReferencesResult, int], Tuple[GetReferencesResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_submodel_elements_aas_repository(aas_identifier, submodel_identifier, limit=None, cursor=None, level=None, extent=None):  # noqa: E501
    """Returns all submodel elements including their hierarchy

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
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


def get_all_submodel_elements_metadata_aas_repository(aas_identifier, submodel_identifier, limit=None, cursor=None, level=None):  # noqa: E501
    """Returns all submodel elements including their hierarchy

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[GetSubmodelElementsMetadataResult, Tuple[GetSubmodelElementsMetadataResult, int], Tuple[GetSubmodelElementsMetadataResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_submodel_elements_path_aas_repository(aas_identifier, submodel_identifier, limit=None, cursor=None, level=None, extent=None):  # noqa: E501
    """Returns all submodel elements including their hierarchy

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str
    :param extent: Determines to which extent the resource is being serialized
    :type extent: str

    :rtype: Union[GetPathItemsResult, Tuple[GetPathItemsResult, int], Tuple[GetPathItemsResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_submodel_elements_reference_aas_repository(aas_identifier, submodel_identifier, limit=None, cursor=None, level=None):  # noqa: E501
    """Returns all submodel elements as a list of References

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[GetReferencesResult, Tuple[GetReferencesResult, int], Tuple[GetReferencesResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_submodel_elements_value_only_aas_repository(aas_identifier, submodel_identifier, limit=None, cursor=None, level=None):  # noqa: E501
    """Returns all submodel elements including their hierarchy in the ValueOnly representation

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[GetSubmodelElementsValueResult, Tuple[GetSubmodelElementsValueResult, int], Tuple[GetSubmodelElementsValueResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_submodel_references_aas_repository(aas_identifier, limit=None, cursor=None):  # noqa: E501
    """Returns all submodel references

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str

    :rtype: Union[GetReferencesResult, Tuple[GetReferencesResult, int], Tuple[GetReferencesResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_asset_administration_shell_by_id(aas_identifier):  # noqa: E501
    """Returns a specific Asset Administration Shell

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str

    :rtype: Union[AssetAdministrationShell, Tuple[AssetAdministrationShell, int], Tuple[AssetAdministrationShell, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_asset_administration_shell_by_id_reference_aas_repository(aas_identifier):  # noqa: E501
    """Returns a specific Asset Administration Shell as a Reference

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str

    :rtype: Union[Reference, Tuple[Reference, int], Tuple[Reference, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_asset_information_aas_repository(aas_identifier):  # noqa: E501
    """Returns the Asset Information

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str

    :rtype: Union[AssetInformation, Tuple[AssetInformation, int], Tuple[AssetInformation, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_file_by_path_aas_repository(aas_identifier, submodel_identifier, id_short_path):  # noqa: E501
    """Downloads file content from a specific submodel element from the Submodel at a specified path

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str

    :rtype: Union[file, Tuple[file, int], Tuple[file, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_operation_async_result_aas_repository(aas_identifier, submodel_identifier, id_short_path, handle_id):  # noqa: E501
    """Returns the Operation result of an asynchronous invoked Operation

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param handle_id: The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)
    :type handle_id: str

    :rtype: Union[OperationResult, Tuple[OperationResult, int], Tuple[OperationResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_operation_async_result_value_only_aas_repository(aas_identifier, submodel_identifier, id_short_path, handle_id):  # noqa: E501
    """Returns the ValueOnly notation of the Operation result of an asynchronous invoked Operation

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param handle_id: The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)
    :type handle_id: str

    :rtype: Union[OperationResultValueOnly, Tuple[OperationResultValueOnly, int], Tuple[OperationResultValueOnly, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_operation_async_status_aas_repository(aas_identifier, submodel_identifier, id_short_path, handle_id):  # noqa: E501
    """Returns the Operation status of an asynchronous invoked Operation

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param handle_id: The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)
    :type handle_id: str

    :rtype: Union[BaseOperationResult, Tuple[BaseOperationResult, int], Tuple[BaseOperationResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_by_id_aas_repository(aas_identifier, submodel_identifier, level=None, extent=None):  # noqa: E501
    """Returns the Submodel

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str
    :param extent: Determines to which extent the resource is being serialized
    :type extent: str

    :rtype: Union[Submodel, Tuple[Submodel, int], Tuple[Submodel, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_by_id_metadata_aas_repository(aas_identifier, submodel_identifier, level=None):  # noqa: E501
    """Returns the Submodel&#39;s metadata elements

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[SubmodelMetadata, Tuple[SubmodelMetadata, int], Tuple[SubmodelMetadata, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_by_id_path_aas_repository(aas_identifier, submodel_identifier, level=None):  # noqa: E501
    """Returns the Submodel&#39;s metadata elements

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[List[str], Tuple[List[str], int], Tuple[List[str], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_by_id_reference_aas_repository(aas_identifier, submodel_identifier):  # noqa: E501
    """Returns the Submodel as a Reference

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str

    :rtype: Union[Reference, Tuple[Reference, int], Tuple[Reference, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_by_id_value_only_aas_repository(aas_identifier, submodel_identifier, level=None, extent=None):  # noqa: E501
    """Returns the Submodel&#39;s ValueOnly representation

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str
    :param extent: Determines to which extent the resource is being serialized
    :type extent: str

    :rtype: Union[SubmodelValue, Tuple[SubmodelValue, int], Tuple[SubmodelValue, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_element_by_path_aas_repository(aas_identifier, submodel_identifier, id_short_path, level=None, extent=None):  # noqa: E501
    """Returns a specific submodel element from the Submodel at a specified path

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str
    :param extent: Determines to which extent the resource is being serialized
    :type extent: str

    :rtype: Union[SubmodelElement, Tuple[SubmodelElement, int], Tuple[SubmodelElement, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_element_by_path_metadata_aas_repository(aas_identifier, submodel_identifier, id_short_path, level=None):  # noqa: E501
    """Returns the metadata attributes if a specific submodel element from the Submodel at a specified path

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[SubmodelElementMetadata, Tuple[SubmodelElementMetadata, int], Tuple[SubmodelElementMetadata, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_element_by_path_path_aas_repository(aas_identifier, submodel_identifier, id_short_path, level=None):  # noqa: E501
    """Returns a specific submodel element from the Submodel at a specified path in the Path notation

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_element_by_path_reference_aas_repository(aas_identifier, submodel_identifier, id_short_path, level=None):  # noqa: E501
    """Returns the Reference of a specific submodel element from the Submodel at a specified path

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[Reference, Tuple[Reference, int], Tuple[Reference, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_element_by_path_value_only_aas_repository(aas_identifier, submodel_identifier, id_short_path, level=None, extent=None):  # noqa: E501
    """Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param level: Determines the structural depth of the respective resource content
    :type level: str
    :param extent: Determines to which extent the resource is being serialized
    :type extent: str

    :rtype: Union[SubmodelElementValue, Tuple[SubmodelElementValue, int], Tuple[SubmodelElementValue, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_thumbnail_aas_repository(aas_identifier):  # noqa: E501
    """get_thumbnail_aas_repository

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str

    :rtype: Union[file, Tuple[file, int], Tuple[file, int, Dict[str, str]]
    """
    return 'do some magic!'


def invoke_operation_aas_repository(aas_identifier, submodel_identifier, id_short_path, operation_request):  # noqa: E501
    """Synchronously invokes an Operation at a specified path

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param operation_request: Operation request object
    :type operation_request: dict | bytes

    :rtype: Union[OperationResult, Tuple[OperationResult, int], Tuple[OperationResult, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        operation_request = OperationRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def invoke_operation_async_aas_repository(aas_identifier, submodel_identifier, id_short_path, operation_request):  # noqa: E501
    """Asynchronously invokes an Operation at a specified path

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param operation_request: Operation request object
    :type operation_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        operation_request = OperationRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def invoke_operation_async_value_only_aas_repository(aas_identifier, submodel_identifier, id_short_path, operation_request_value_only):  # noqa: E501
    """Asynchronously invokes an Operation at a specified path

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param operation_request_value_only: Operation request object
    :type operation_request_value_only: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        operation_request_value_only = OperationRequestValueOnly.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def invoke_operation_value_only_aas_repository(aas_identifier, submodel_identifier, id_short_path, operation_request_value_only):  # noqa: E501
    """Synchronously invokes an Operation at a specified path

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param operation_request_value_only: Operation request object
    :type operation_request_value_only: dict | bytes

    :rtype: Union[OperationResultValueOnly, Tuple[OperationResultValueOnly, int], Tuple[OperationResultValueOnly, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        operation_request_value_only = OperationRequestValueOnly.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_submodel_aas_repository(aas_identifier, submodel_identifier, submodel, level=None):  # noqa: E501
    """Updates the Submodel

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param submodel: Submodel object
    :type submodel: dict | bytes
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel = Submodel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_submodel_by_id_metadata_aas_repository(aas_identifier, submodel_identifier, submodel_metadata, level=None):  # noqa: E501
    """Updates the metadata attributes of the Submodel

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param submodel_metadata: Submodel object
    :type submodel_metadata: dict | bytes
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_metadata = SubmodelMetadata.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_submodel_by_id_value_only_aas_repository(aas_identifier, submodel_identifier, submodel_value, level=None):  # noqa: E501
    """Updates teh values of the Submodel

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param submodel_value: Submodel object in the ValueOnly representation
    :type submodel_value: dict | bytes
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_value = SubmodelValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_submodel_element_value_by_path_aas_repository(aas_identifier, submodel_identifier, id_short_path, submodel_element, level=None):  # noqa: E501
    """Updates an existing submodel element value at a specified path within submodel elements hierarchy

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param submodel_element: The updated value of the submodel element
    :type submodel_element: dict | bytes
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_element = SubmodelElement.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_submodel_element_value_by_path_metadata(aas_identifier, submodel_identifier, id_short_path, submodel_element_metadata, level=None):  # noqa: E501
    """Updates the metadata attributes of an existing submodel element value at a specified path within submodel elements hierarchy

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param submodel_element_metadata: The updated metadata attributes of the submodel element
    :type submodel_element_metadata: dict | bytes
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_element_metadata = SubmodelElementMetadata.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_submodel_element_value_by_path_value_only(aas_identifier, submodel_identifier, id_short_path, submodel_element_value, level=None):  # noqa: E501
    """Updates the value of an existing submodel element value at a specified path within submodel elements hierarchy

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param submodel_element_value: The updated value of the submodel element
    :type submodel_element_value: dict | bytes
    :param level: Determines the structural depth of the respective resource content
    :type level: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_element_value = SubmodelElementValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_asset_administration_shell(asset_administration_shell):  # noqa: E501
    """Creates a new Asset Administration Shell

     # noqa: E501

    :param asset_administration_shell: Asset Administration Shell object
    :type asset_administration_shell: dict | bytes

    :rtype: Union[AssetAdministrationShell, Tuple[AssetAdministrationShell, int], Tuple[AssetAdministrationShell, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        asset_administration_shell = AssetAdministrationShell.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_submodel_element_aas_repository(aas_identifier, submodel_identifier, submodel_element):  # noqa: E501
    """Creates a new submodel element

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param submodel_element: Requested submodel element
    :type submodel_element: dict | bytes

    :rtype: Union[SubmodelElement, Tuple[SubmodelElement, int], Tuple[SubmodelElement, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_element = SubmodelElement.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_submodel_element_by_path_aas_repository(aas_identifier, submodel_identifier, id_short_path, submodel_element):  # noqa: E501
    """Creates a new submodel element at a specified path within submodel elements hierarchy

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param submodel_element: Requested submodel element
    :type submodel_element: dict | bytes

    :rtype: Union[SubmodelElement, Tuple[SubmodelElement, int], Tuple[SubmodelElement, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_element = SubmodelElement.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_submodel_reference_aas_repository(aas_identifier, reference):  # noqa: E501
    """Creates a submodel reference at the Asset Administration Shell

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param reference: Reference to the Submodel
    :type reference: dict | bytes

    :rtype: Union[Reference, Tuple[Reference, int], Tuple[Reference, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        reference = Reference.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_asset_administration_shell_by_id(aas_identifier, asset_administration_shell):  # noqa: E501
    """Updates an existing Asset Administration Shell

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param asset_administration_shell: Asset Administration Shell object
    :type asset_administration_shell: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        asset_administration_shell = AssetAdministrationShell.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_asset_information_aas_repository(aas_identifier, asset_information):  # noqa: E501
    """Updates the Asset Information

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param asset_information: Asset Information object
    :type asset_information: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        asset_information = AssetInformation.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_file_by_path_aas_repository(aas_identifier, submodel_identifier, id_short_path, file_name=None, file=None):  # noqa: E501
    """Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param file_name: 
    :type file_name: str
    :param file: 
    :type file: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def put_submodel_by_id_aas_repository(aas_identifier, submodel_identifier, submodel):  # noqa: E501
    """Updates the Submodel

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param submodel: Submodel object
    :type submodel: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel = Submodel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_submodel_element_by_path_aas_repository(aas_identifier, submodel_identifier, id_short_path, submodel_element):  # noqa: E501
    """Updates an existing submodel element at a specified path within submodel elements hierarchy

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param id_short_path: IdShort path to the submodel element (dot-separated)
    :type id_short_path: str
    :param submodel_element: Requested submodel element
    :type submodel_element: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_element = SubmodelElement.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_thumbnail_aas_repository(aas_identifier, file_name=None, file=None):  # noqa: E501
    """put_thumbnail_aas_repository

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param file_name: 
    :type file_name: str
    :param file: 
    :type file: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'
