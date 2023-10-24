import unittest

from flask import json

from ..models.get_submodel_descriptors_result import GetSubmodelDescriptorsResult  # noqa: E501
from ..models.result import Result  # noqa: E501
from ..models.submodel_descriptor import SubmodelDescriptor  # noqa: E501
from ..test import BaseTestCase


class TestSubmodelRegistryAPIController(BaseTestCase):
    """SubmodelRegistryAPIController integration test stubs"""

    def test_delete_submodel_descriptor_by_id(self):
        """Test case for delete_submodel_descriptor_by_id

        Deletes a Submodel Descriptor, i.e. de-registers a submodel
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel-descriptors/{submodel_identifier}'.format(submodel_identifier='submodel_identifier_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_descriptors(self):
        """Test case for get_all_submodel_descriptors

        Returns all Submodel Descriptors
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel-descriptors',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_descriptor_by_id(self):
        """Test case for get_submodel_descriptor_by_id

        Returns a specific Submodel Descriptor
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel-descriptors/{submodel_identifier}'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_submodel_descriptor(self):
        """Test case for post_submodel_descriptor

        Creates a new Submodel Descriptor, i.e. registers a submodel
        """
        submodel_descriptor = "{ \"id\": \"https://admin-shell.io/zvei/nameplate/1/0/Nameplate\", \"endpoints\": [ { \"href\": { \"href\": \"https://localhost:1234/api/v3.0/submodel\", \"endpointProtocol\": \"HTTP\", \"endpointProtocolVersion\": [\"1.1\"] }, \"interface\": \"AAS-3.0\" }, { \"protocolInformation\": { \"href\": \"opc.tcp://localhost:4840\" }, \"interface\": \"AAS-3.0\" }, { \"protocolInformation\": { \"href\": \"https://localhost:5678\", \"endpointProtocol\": \"HTTP\", \"endpointProtocolVersion\": [\"1.1\"], \"subprotocol\": \"OPC UA Basic SOAP\", \"subprotocolBody\": \"ns=2;s=MyAAS\", \"subprotocolBodyEncoding\": \"application/soap+xml\" }, \"interface\": \"AAS-3.0\" } ] }"
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel-descriptors',
            method='POST',
            headers=headers,
            data=json.dumps(submodel_descriptor),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_submodel_descriptor_by_id(self):
        """Test case for put_submodel_descriptor_by_id

        Updates an existing Submodel Descriptor
        """
        submodel_descriptor = "{ \"id\": \"https://admin-shell.io/zvei/nameplate/1/0/Nameplate\", \"endpoints\": [ { \"href\": { \"href\": \"https://localhost:1234/api/v3.0/submodel\", \"endpointProtocol\": \"HTTP\", \"endpointProtocolVersion\": [\"1.1\"] }, \"interface\": \"AAS-3.0\" }, { \"protocolInformation\": { \"href\": \"opc.tcp://localhost:4840\" }, \"interface\": \"AAS-3.0\" }, { \"protocolInformation\": { \"href\": \"https://localhost:5678\", \"endpointProtocol\": \"HTTP\", \"endpointProtocolVersion\": [\"1.1\"], \"subprotocol\": \"OPC UA Basic SOAP\", \"subprotocolBody\": \"ns=2;s=MyAAS\", \"subprotocolBodyEncoding\": \"application/soap+xml\" }, \"interface\": \"AAS-3.0\" } ] }"
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel-descriptors/{submodel_identifier}'.format(submodel_identifier='submodel_identifier_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(submodel_descriptor),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
