import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from ..models.get_package_descriptions_result import GetPackageDescriptionsResult  # noqa: E501
from ..models.package_description import PackageDescription  # noqa: E501
from ..models.result import Result  # noqa: E501
from .. import util


def delete_aasxby_package_id(package_id):  # noqa: E501
    """Deletes a specific AASX package from the server

     # noqa: E501

    :param package_id: The package Id (UTF8-BASE64-URL-encoded)
    :type package_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_aasxby_package_id(package_id):  # noqa: E501
    """Returns a specific AASX package from the server

     # noqa: E501

    :param package_id: The package Id (UTF8-BASE64-URL-encoded)
    :type package_id: str

    :rtype: Union[file, Tuple[file, int], Tuple[file, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_aasx_package_ids(aas_id=None, limit=None, cursor=None):  # noqa: E501
    """Returns a list of available AASX packages at the server

     # noqa: E501

    :param aas_id: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_id: str
    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str

    :rtype: Union[GetPackageDescriptionsResult, Tuple[GetPackageDescriptionsResult, int], Tuple[GetPackageDescriptionsResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def post_aasx_package(aas_ids=None, file=None, file_name=None):  # noqa: E501
    """Stores the AASX package at the server

     # noqa: E501

    :param aas_ids: 
    :type aas_ids: List[str]
    :param file: 
    :type file: str
    :param file_name: 
    :type file_name: str

    :rtype: Union[PackageDescription, Tuple[PackageDescription, int], Tuple[PackageDescription, int, Dict[str, str]]
    """
    return 'do some magic!'


def put_aasxby_package_id(package_id, aas_ids=None, file=None, file_name=None):  # noqa: E501
    """Updates the AASX package at the server

     # noqa: E501

    :param package_id: The package Id (UTF8-BASE64-URL-encoded)
    :type package_id: str
    :param aas_ids: 
    :type aas_ids: List[str]
    :param file: 
    :type file: str
    :param file_name: 
    :type file_name: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'
