import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.asset_administration_shell_descriptor import AssetAdministrationShellDescriptor  # noqa: E501
from openapi_server.models.asset_kind import AssetKind  # noqa: E501
from openapi_server.models.get_asset_administration_shell_descriptors_result import GetAssetAdministrationShellDescriptorsResult  # noqa: E501
from openapi_server.models.get_submodel_descriptors_result import GetSubmodelDescriptorsResult  # noqa: E501
from openapi_server.models.result import Result  # noqa: E501
from openapi_server.models.submodel_descriptor import SubmodelDescriptor  # noqa: E501
from openapi_server import util


def delete_asset_administration_shell_descriptor_by_id(aas_identifier):  # noqa: E501
    """Deletes an Asset Administration Shell Descriptor, i.e. de-registers an AAS

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def delete_submodel_descriptor_by_id_through_superpath(aas_identifier, submodel_identifier):  # noqa: E501
    """Deletes a Submodel Descriptor, i.e. de-registers a submodel

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_asset_administration_shell_descriptors(limit=None, cursor=None, asset_kind=None, asset_type=None):  # noqa: E501
    """Returns all Asset Administration Shell Descriptors

     # noqa: E501

    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str
    :param asset_kind: The Asset&#39;s kind (Instance or Type)
    :type asset_kind: dict | bytes
    :param asset_type: The Asset&#39;s type (UTF8-BASE64-URL-encoded)
    :type asset_type: str

    :rtype: Union[GetAssetAdministrationShellDescriptorsResult, Tuple[GetAssetAdministrationShellDescriptorsResult, int], Tuple[GetAssetAdministrationShellDescriptorsResult, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        asset_kind =  AssetKind.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_all_submodel_descriptors_through_superpath(aas_identifier, limit=None, cursor=None):  # noqa: E501
    """Returns all Submodel Descriptors

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str

    :rtype: Union[GetSubmodelDescriptorsResult, Tuple[GetSubmodelDescriptorsResult, int], Tuple[GetSubmodelDescriptorsResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_asset_administration_shell_descriptor_by_id(aas_identifier):  # noqa: E501
    """Returns a specific Asset Administration Shell Descriptor

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str

    :rtype: Union[AssetAdministrationShellDescriptor, Tuple[AssetAdministrationShellDescriptor, int], Tuple[AssetAdministrationShellDescriptor, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_submodel_descriptor_by_id_through_superpath(aas_identifier, submodel_identifier):  # noqa: E501
    """Returns a specific Submodel Descriptor

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str

    :rtype: Union[SubmodelDescriptor, Tuple[SubmodelDescriptor, int], Tuple[SubmodelDescriptor, int, Dict[str, str]]
    """
    return 'do some magic!'


def post_asset_administration_shell_descriptor(asset_administration_shell_descriptor):  # noqa: E501
    """Creates a new Asset Administration Shell Descriptor, i.e. registers an AAS

     # noqa: E501

    :param asset_administration_shell_descriptor: Asset Administration Shell Descriptor object
    :type asset_administration_shell_descriptor: dict | bytes

    :rtype: Union[AssetAdministrationShellDescriptor, Tuple[AssetAdministrationShellDescriptor, int], Tuple[AssetAdministrationShellDescriptor, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        asset_administration_shell_descriptor = AssetAdministrationShellDescriptor.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_submodel_descriptor_through_superpath(aas_identifier, submodel_descriptor):  # noqa: E501
    """Creates a new Submodel Descriptor, i.e. registers a submodel

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_descriptor: Submodel Descriptor object
    :type submodel_descriptor: dict | bytes

    :rtype: Union[SubmodelDescriptor, Tuple[SubmodelDescriptor, int], Tuple[SubmodelDescriptor, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_descriptor = SubmodelDescriptor.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_asset_administration_shell_descriptor_by_id(aas_identifier, asset_administration_shell_descriptor):  # noqa: E501
    """Updates an existing Asset Administration Shell Descriptor

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param asset_administration_shell_descriptor: Asset Administration Shell Descriptor object
    :type asset_administration_shell_descriptor: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        asset_administration_shell_descriptor = AssetAdministrationShellDescriptor.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_submodel_descriptor_by_id_through_superpath(aas_identifier, submodel_identifier, submodel_descriptor):  # noqa: E501
    """Updates an existing Submodel Descriptor

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param submodel_identifier: The Submodel’s unique id (UTF8-BASE64-URL-encoded)
    :type submodel_identifier: str
    :param submodel_descriptor: Submodel Descriptor object
    :type submodel_descriptor: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        submodel_descriptor = SubmodelDescriptor.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
