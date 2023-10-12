import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.environment import Environment  # noqa: E501
from openapi_server.models.result import Result  # noqa: E501
from openapi_server import util


def generate_serialization_by_ids(aas_ids=None, submodel_ids=None, include_concept_descriptions=None):  # noqa: E501
    """Returns an appropriate serialization based on the specified format (see SerializationFormat)

     # noqa: E501

    :param aas_ids: The Asset Administration Shells&#39; unique ids (UTF8-BASE64-URL-encoded)
    :type aas_ids: List[str]
    :param submodel_ids: The Submodels&#39; unique ids (UTF8-BASE64-URL-encoded)
    :type submodel_ids: List[str]
    :param include_concept_descriptions: Include Concept Descriptions?
    :type include_concept_descriptions: bool

    :rtype: Union[file, Tuple[file, int], Tuple[file, int, Dict[str, str]]
    """
    return 'do some magic!'
