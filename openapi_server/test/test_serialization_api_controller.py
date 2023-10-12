import unittest

from flask import json

from openapi_server.models.environment import Environment  # noqa: E501
from openapi_server.models.result import Result  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSerializationAPIController(BaseTestCase):
    """SerializationAPIController integration test stubs"""

    def test_generate_serialization_by_ids(self):
        """Test case for generate_serialization_by_ids

        Returns an appropriate serialization based on the specified format (see SerializationFormat)
        """
        query_string = [('aasIds', ['aas_ids_example']),
                        ('submodelIds', ['submodel_ids_example']),
                        ('includeConceptDescriptions', True)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/serialization',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
