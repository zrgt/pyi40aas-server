from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.submodel_element import SubmodelElement
from openapi_server import util

from openapi_server.models.submodel_element import SubmodelElement  # noqa: E501

class SubmodelValue(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, submodel_elements=None):  # noqa: E501
        """SubmodelValue - a model defined in OpenAPI

        :param submodel_elements: The submodel_elements of this SubmodelValue.  # noqa: E501
        :type submodel_elements: List[SubmodelElement]
        """
        self.openapi_types = {
            'submodel_elements': List[SubmodelElement]
        }

        self.attribute_map = {
            'submodel_elements': 'submodelElements'
        }

        self._submodel_elements = submodel_elements

    @classmethod
    def from_dict(cls, dikt) -> 'SubmodelValue':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubmodelValue of this SubmodelValue.  # noqa: E501
        :rtype: SubmodelValue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def submodel_elements(self) -> List[SubmodelElement]:
        """Gets the submodel_elements of this SubmodelValue.


        :return: The submodel_elements of this SubmodelValue.
        :rtype: List[SubmodelElement]
        """
        return self._submodel_elements

    @submodel_elements.setter
    def submodel_elements(self, submodel_elements: List[SubmodelElement]):
        """Sets the submodel_elements of this SubmodelValue.


        :param submodel_elements: The submodel_elements of this SubmodelValue.
        :type submodel_elements: List[SubmodelElement]
        """
        if submodel_elements is not None and len(submodel_elements) < 1:
            raise ValueError("Invalid value for `submodel_elements`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._submodel_elements = submodel_elements
