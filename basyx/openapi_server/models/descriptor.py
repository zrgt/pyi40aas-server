from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ..models.base_model import Model
from ..models.extension import Extension
from ..models.lang_string_name_type import LangStringNameType
from ..models.lang_string_text_type import LangStringTextType
from .. import util

from ..models.extension import Extension  # noqa: E501
from ..models.lang_string_name_type import LangStringNameType  # noqa: E501
from ..models.lang_string_text_type import LangStringTextType  # noqa: E501

class Descriptor(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description=None, display_name=None, extensions=None):  # noqa: E501
        """Descriptor - a model defined in OpenAPI

        :param description: The description of this Descriptor.  # noqa: E501
        :type description: List[LangStringTextType]
        :param display_name: The display_name of this Descriptor.  # noqa: E501
        :type display_name: List[LangStringNameType]
        :param extensions: The extensions of this Descriptor.  # noqa: E501
        :type extensions: List[Extension]
        """
        self.openapi_types = {
            'description': List[LangStringTextType],
            'display_name': List[LangStringNameType],
            'extensions': List[Extension]
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'extensions': 'extensions'
        }

        self._description = description
        self._display_name = display_name
        self._extensions = extensions

    @classmethod
    def from_dict(cls, dikt) -> 'Descriptor':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Descriptor of this Descriptor.  # noqa: E501
        :rtype: Descriptor
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self) -> List[LangStringTextType]:
        """Gets the description of this Descriptor.


        :return: The description of this Descriptor.
        :rtype: List[LangStringTextType]
        """
        return self._description

    @description.setter
    def description(self, description: List[LangStringTextType]):
        """Sets the description of this Descriptor.


        :param description: The description of this Descriptor.
        :type description: List[LangStringTextType]
        """

        self._description = description

    @property
    def display_name(self) -> List[LangStringNameType]:
        """Gets the display_name of this Descriptor.


        :return: The display_name of this Descriptor.
        :rtype: List[LangStringNameType]
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: List[LangStringNameType]):
        """Sets the display_name of this Descriptor.


        :param display_name: The display_name of this Descriptor.
        :type display_name: List[LangStringNameType]
        """

        self._display_name = display_name

    @property
    def extensions(self) -> List[Extension]:
        """Gets the extensions of this Descriptor.


        :return: The extensions of this Descriptor.
        :rtype: List[Extension]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions: List[Extension]):
        """Sets the extensions of this Descriptor.


        :param extensions: The extensions of this Descriptor.
        :type extensions: List[Extension]
        """
        if extensions is not None and len(extensions) < 1:
            raise ValueError("Invalid value for `extensions`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._extensions = extensions