import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.result import Result  # noqa: E501
from openapi_server.models.service_description import ServiceDescription  # noqa: E501
from openapi_server import util


def get_description():  # noqa: E501
    """Returns the self-describing information of a network resource (ServiceDescription)

     # noqa: E501


    :rtype: Union[ServiceDescription, Tuple[ServiceDescription, int], Tuple[ServiceDescription, int, Dict[str, str]]
    """
    return 'do some magic!'
