from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ..models.base_model import Model
from ..models.model_type import ModelType
from .. import util

from ..models.model_type import ModelType  # noqa: E501

class DataSpecificationContent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, model_type=None):  # noqa: E501
        """DataSpecificationContent - a model defined in OpenAPI

        :param model_type: The model_type of this DataSpecificationContent.  # noqa: E501
        :type model_type: ModelType
        """
        self.openapi_types = {
            'model_type': ModelType
        }

        self.attribute_map = {
            'model_type': 'modelType'
        }

        self._model_type = model_type

    @classmethod
    def from_dict(cls, dikt) -> 'DataSpecificationContent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataSpecificationContent of this DataSpecificationContent.  # noqa: E501
        :rtype: DataSpecificationContent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def model_type(self) -> ModelType:
        """Gets the model_type of this DataSpecificationContent.


        :return: The model_type of this DataSpecificationContent.
        :rtype: ModelType
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type: ModelType):
        """Sets the model_type of this DataSpecificationContent.


        :param model_type: The model_type of this DataSpecificationContent.
        :type model_type: ModelType
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501

        self._model_type = model_type