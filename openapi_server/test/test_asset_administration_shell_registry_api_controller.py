import unittest

from flask import json

from openapi_server.models.asset_administration_shell_descriptor import AssetAdministrationShellDescriptor  # noqa: E501
from openapi_server.models.asset_kind import AssetKind  # noqa: E501
from openapi_server.models.get_asset_administration_shell_descriptors_result import GetAssetAdministrationShellDescriptorsResult  # noqa: E501
from openapi_server.models.get_submodel_descriptors_result import GetSubmodelDescriptorsResult  # noqa: E501
from openapi_server.models.result import Result  # noqa: E501
from openapi_server.models.submodel_descriptor import SubmodelDescriptor  # noqa: E501
from openapi_server.test import BaseTestCase


class TestAssetAdministrationShellRegistryAPIController(BaseTestCase):
    """AssetAdministrationShellRegistryAPIController integration test stubs"""

    def test_delete_asset_administration_shell_descriptor_by_id(self):
        """Test case for delete_asset_administration_shell_descriptor_by_id

        Deletes an Asset Administration Shell Descriptor, i.e. de-registers an AAS
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shell-descriptors/{aas_identifier}'.format(aas_identifier='aas_identifier_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_submodel_descriptor_by_id_through_superpath(self):
        """Test case for delete_submodel_descriptor_by_id_through_superpath

        Deletes a Submodel Descriptor, i.e. de-registers a submodel
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shell-descriptors/{aas_identifier}/submodel-descriptors/{submodel_identifier}'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_asset_administration_shell_descriptors(self):
        """Test case for get_all_asset_administration_shell_descriptors

        Returns all Asset Administration Shell Descriptors
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('assetKind', openapi_server.AssetKind()),
                        ('assetType', 'asset_type_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shell-descriptors',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_descriptors_through_superpath(self):
        """Test case for get_all_submodel_descriptors_through_superpath

        Returns all Submodel Descriptors
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shell-descriptors/{aas_identifier}/submodel-descriptors'.format(aas_identifier='aas_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_asset_administration_shell_descriptor_by_id(self):
        """Test case for get_asset_administration_shell_descriptor_by_id

        Returns a specific Asset Administration Shell Descriptor
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shell-descriptors/{aas_identifier}'.format(aas_identifier='aas_identifier_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_descriptor_by_id_through_superpath(self):
        """Test case for get_submodel_descriptor_by_id_through_superpath

        Returns a specific Submodel Descriptor
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shell-descriptors/{aas_identifier}/submodel-descriptors/{submodel_identifier}'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_asset_administration_shell_descriptor(self):
        """Test case for post_asset_administration_shell_descriptor

        Creates a new Asset Administration Shell Descriptor, i.e. registers an AAS
        """
        asset_administration_shell_descriptor = "{ \"id\": \"https://example.org/aas/motor\", \"endpoints\": [ { \"protocolInformation\": { \"href\": \"https://localhost:1234/api/v3.0/aas\", \"endpointProtocol\": \"HTTP\", \"endpointProtocolVersion\": [\"1.1\"] }, \"interface\": \"AAS-3.0\" }, { \"protocolInformation\": { \"href\": \"opc.tcp://localhost:4840\" }, \"interface\": \"AAS-3.0\" }, { \"protocolInformation\": { \"href\": \"https://localhost:5678\", \"endpointProtocol\": \"HTTP\", \"endpointProtocolVersion\": [\"1.1\"], \"subprotocol\": \"OPC UA Basic SOAP\", \"subprotocolBody\": \"ns=2;s=MyAAS\", \"subprotocolBodyEncoding\": \"application/soap+xml\" }, \"interface\": \"AAS-3.0\" } ] }"
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shell-descriptors',
            method='POST',
            headers=headers,
            data=json.dumps(asset_administration_shell_descriptor),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_submodel_descriptor_through_superpath(self):
        """Test case for post_submodel_descriptor_through_superpath

        Creates a new Submodel Descriptor, i.e. registers a submodel
        """
        submodel_descriptor = "{ \"id\": \"https://admin-shell.io/zvei/nameplate/1/0/Nameplate\", \"endpoints\": [ { \"href\": { \"href\": \"https://localhost:1234/api/v3.0/submodel\", \"endpointProtocol\": \"HTTP\", \"endpointProtocolVersion\": [\"1.1\"] }, \"interface\": \"AAS-3.0\" }, { \"protocolInformation\": { \"href\": \"opc.tcp://localhost:4840\" }, \"interface\": \"AAS-3.0\" }, { \"protocolInformation\": { \"href\": \"https://localhost:5678\", \"endpointProtocol\": \"HTTP\", \"endpointProtocolVersion\": [\"1.1\"], \"subprotocol\": \"OPC UA Basic SOAP\", \"subprotocolBody\": \"ns=2;s=MyAAS\", \"subprotocolBodyEncoding\": \"application/soap+xml\" }, \"interface\": \"AAS-3.0\" } ] }"
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shell-descriptors/{aas_identifier}/submodel-descriptors'.format(aas_identifier='aas_identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(submodel_descriptor),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_asset_administration_shell_descriptor_by_id(self):
        """Test case for put_asset_administration_shell_descriptor_by_id

        Updates an existing Asset Administration Shell Descriptor
        """
        asset_administration_shell_descriptor = "{ \"id\": \"https://example.org/aas/motor\", \"endpoints\": [ { \"protocolInformation\": { \"href\": \"https://localhost:1234/api/v3.0/aas\", \"endpointProtocol\": \"HTTP\", \"endpointProtocolVersion\": [\"1.1\"] }, \"interface\": \"AAS-3.0\" }, { \"protocolInformation\": { \"href\": \"opc.tcp://localhost:4840\" }, \"interface\": \"AAS-3.0\" }, { \"protocolInformation\": { \"href\": \"https://localhost:5678\", \"endpointProtocol\": \"HTTP\", \"endpointProtocolVersion\": [\"1.1\"], \"subprotocol\": \"OPC UA Basic SOAP\", \"subprotocolBody\": \"ns=2;s=MyAAS\", \"subprotocolBodyEncoding\": \"application/soap+xml\" }, \"interface\": \"AAS-3.0\" } ] }"
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shell-descriptors/{aas_identifier}'.format(aas_identifier='aas_identifier_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(asset_administration_shell_descriptor),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_submodel_descriptor_by_id_through_superpath(self):
        """Test case for put_submodel_descriptor_by_id_through_superpath

        Updates an existing Submodel Descriptor
        """
        submodel_descriptor = "{ \"id\": \"https://admin-shell.io/zvei/nameplate/1/0/Nameplate\", \"endpoints\": [ { \"href\": { \"href\": \"https://localhost:1234/api/v3.0/submodel\", \"endpointProtocol\": \"HTTP\", \"endpointProtocolVersion\": [\"1.1\"] }, \"interface\": \"AAS-3.0\" }, { \"protocolInformation\": { \"href\": \"opc.tcp://localhost:4840\" }, \"interface\": \"AAS-3.0\" }, { \"protocolInformation\": { \"href\": \"https://localhost:5678\", \"endpointProtocol\": \"HTTP\", \"endpointProtocolVersion\": [\"1.1\"], \"subprotocol\": \"OPC UA Basic SOAP\", \"subprotocolBody\": \"ns=2;s=MyAAS\", \"subprotocolBodyEncoding\": \"application/soap+xml\" }, \"interface\": \"AAS-3.0\" } ] }"
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shell-descriptors/{aas_identifier}/submodel-descriptors/{submodel_identifier}'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(submodel_descriptor),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
