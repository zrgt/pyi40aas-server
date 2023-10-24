import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from ..models.inline_response200 import InlineResponse200  # noqa: E501
from ..models.result import Result  # noqa: E501
from ..models.specific_asset_id import SpecificAssetId  # noqa: E501
from .. import util


def delete_all_asset_links_by_id(aas_identifier):  # noqa: E501
    """Deletes all specific Asset identifiers linked to an Asset Administration Shell to edit discoverable content

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_asset_administration_shell_ids_by_asset_link(asset_ids=None, limit=None, cursor=None):  # noqa: E501
    """Returns a list of Asset Administration Shell ids linked to specific Asset identifiers

     # noqa: E501

    :param asset_ids: A list of specific Asset identifiers. Each Asset identifier is a base64-url-encoded [SpecificAssetId](https://api.swaggerhub.com/domains/Plattform_i40/Part1-MetaModel-Schemas/V3.0.1#/components/schemas/SpecificAssetId)
    :type asset_ids: List[str]
    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str

    :rtype: Union[InlineResponse200, Tuple[InlineResponse200, int], Tuple[InlineResponse200, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_asset_links_by_id(aas_identifier):  # noqa: E501
    """Returns a list of specific Asset identifiers based on an Asset Administration Shell id to edit discoverable content

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str

    :rtype: Union[List[SpecificAssetId], Tuple[List[SpecificAssetId], int], Tuple[List[SpecificAssetId], int, Dict[str, str]]
    """
    return 'do some magic!'


def post_all_asset_links_by_id(aas_identifier, specific_asset_id):  # noqa: E501
    """Creates specific Asset identifiers linked to an Asset Administration Shell to edit discoverable content

     # noqa: E501

    :param aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
    :type aas_identifier: str
    :param specific_asset_id: A list of specific Asset identifiers
    :type specific_asset_id: list | bytes

    :rtype: Union[List[SpecificAssetId], Tuple[List[SpecificAssetId], int], Tuple[List[SpecificAssetId], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        specific_asset_id = [SpecificAssetId.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'
