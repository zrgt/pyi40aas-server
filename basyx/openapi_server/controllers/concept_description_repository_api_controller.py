import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from ..models.concept_description import ConceptDescription  # noqa: E501
from ..models.get_concept_descriptions_result import GetConceptDescriptionsResult  # noqa: E501
from ..models.result import Result  # noqa: E501
from .. import util


def delete_concept_description_by_id(cd_identifier):  # noqa: E501
    """Deletes a Concept Description

     # noqa: E501

    :param cd_identifier: The Concept Description’s unique id (UTF8-BASE64-URL-encoded)
    :type cd_identifier: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_concept_descriptions(id_short=None, is_case_of=None, data_specification_ref=None, limit=None, cursor=None):  # noqa: E501
    """Returns all Concept Descriptions

     # noqa: E501

    :param id_short: The Concept Description’s IdShort
    :type id_short: str
    :param is_case_of: IsCaseOf reference (UTF8-BASE64-URL-encoded)
    :type is_case_of: str
    :param data_specification_ref: DataSpecification reference (UTF8-BASE64-URL-encoded)
    :type data_specification_ref: str
    :param limit: The maximum number of elements in the response array
    :type limit: int
    :param cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
    :type cursor: str

    :rtype: Union[GetConceptDescriptionsResult, Tuple[GetConceptDescriptionsResult, int], Tuple[GetConceptDescriptionsResult, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_concept_description_by_id(cd_identifier):  # noqa: E501
    """Returns a specific Concept Description

     # noqa: E501

    :param cd_identifier: The Concept Description’s unique id (UTF8-BASE64-URL-encoded)
    :type cd_identifier: str

    :rtype: Union[ConceptDescription, Tuple[ConceptDescription, int], Tuple[ConceptDescription, int, Dict[str, str]]
    """
    return 'do some magic!'


def post_concept_description(concept_description):  # noqa: E501
    """Creates a new Concept Description

     # noqa: E501

    :param concept_description: Concept Description object
    :type concept_description: dict | bytes

    :rtype: Union[ConceptDescription, Tuple[ConceptDescription, int], Tuple[ConceptDescription, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        concept_description = ConceptDescription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_concept_description_by_id(cd_identifier, concept_description):  # noqa: E501
    """Updates an existing Concept Description

     # noqa: E501

    :param cd_identifier: The Concept Description’s unique id (UTF8-BASE64-URL-encoded)
    :type cd_identifier: str
    :param concept_description: Concept Description object
    :type concept_description: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        concept_description = ConceptDescription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
