import unittest

from flask import json

from ..models.result import Result  # noqa: E501
from ..models.service_description import ServiceDescription  # noqa: E501
from ..test import BaseTestCase


class TestDescriptionAPIController(BaseTestCase):
    """DescriptionAPIController integration test stubs"""

    def test_get_description(self):
        """Test case for get_description

        Returns the self-describing information of a network resource (ServiceDescription)
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/description',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
