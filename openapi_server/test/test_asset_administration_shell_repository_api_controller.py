import unittest

from flask import json

from openapi_server.models.asset_administration_shell import AssetAdministrationShell  # noqa: E501
from openapi_server.models.asset_information import AssetInformation  # noqa: E501
from openapi_server.models.base_operation_result import BaseOperationResult  # noqa: E501
from openapi_server.models.get_asset_administration_shells_result import GetAssetAdministrationShellsResult  # noqa: E501
from openapi_server.models.get_path_items_result import GetPathItemsResult  # noqa: E501
from openapi_server.models.get_references_result import GetReferencesResult  # noqa: E501
from openapi_server.models.get_submodel_elements_metadata_result import GetSubmodelElementsMetadataResult  # noqa: E501
from openapi_server.models.get_submodel_elements_result import GetSubmodelElementsResult  # noqa: E501
from openapi_server.models.get_submodel_elements_value_result import GetSubmodelElementsValueResult  # noqa: E501
from openapi_server.models.operation_request import OperationRequest  # noqa: E501
from openapi_server.models.operation_request_value_only import OperationRequestValueOnly  # noqa: E501
from openapi_server.models.operation_result import OperationResult  # noqa: E501
from openapi_server.models.operation_result_value_only import OperationResultValueOnly  # noqa: E501
from openapi_server.models.reference import Reference  # noqa: E501
from openapi_server.models.result import Result  # noqa: E501
from openapi_server.models.submodel import Submodel  # noqa: E501
from openapi_server.models.submodel_element import SubmodelElement  # noqa: E501
from openapi_server.models.submodel_element_metadata import SubmodelElementMetadata  # noqa: E501
from openapi_server.models.submodel_element_value import SubmodelElementValue  # noqa: E501
from openapi_server.models.submodel_metadata import SubmodelMetadata  # noqa: E501
from openapi_server.models.submodel_value import SubmodelValue  # noqa: E501
from openapi_server.test import BaseTestCase


class TestAssetAdministrationShellRepositoryAPIController(BaseTestCase):
    """AssetAdministrationShellRepositoryAPIController integration test stubs"""

    def test_delete_asset_administration_shell_by_id(self):
        """Test case for delete_asset_administration_shell_by_id

        Deletes an Asset Administration Shell
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}'.format(aas_identifier='aas_identifier_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_file_by_path_aas_repository(self):
        """Test case for delete_file_by_path_aas_repository

        Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/attachment'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_submodel_by_id_aas_repository(self):
        """Test case for delete_submodel_by_id_aas_repository

        Deletes the submodel from the Asset Administration Shell and the Repository.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_submodel_element_by_path_aas_repository(self):
        """Test case for delete_submodel_element_by_path_aas_repository

        Deletes a submodel element at a specified path within the submodel elements hierarchy
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_submodel_reference_by_id_aas_repository(self):
        """Test case for delete_submodel_reference_by_id_aas_repository

        Deletes the submodel reference from the Asset Administration Shell. Does not delete the submodel itself!
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodel-refs/{submodel_identifier}'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_thumbnail_aas_repository(self):
        """Test case for delete_thumbnail_aas_repository

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/asset-information/thumbnail'.format(aas_identifier='aas_identifier_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_asset_administration_shells(self):
        """Test case for get_all_asset_administration_shells

        Returns all Asset Administration Shells
        """
        query_string = [('assetIds', ['?assetIds=eyAibmFtZSI6ICJzb21lLWFzc2V0LWlkIiwgInZhbHVlIjogImh0dHA6Ly9leGFtcGxlLWNvbXBhbnkuY29tL215QXNzZXQiLCAiZXh0ZXJuYWxTdWJqZWN0SWQiOiB7ICJrZXlzIjogWyB7ICJ0eXBlIjogIkdsb2JhbFJlZmVyZW5jZSIsICJ2YWx1ZSI6ICJodHRwOi8vZXhhbXBsZS1jb21wYW55LmNvbS9leGFtcGxlLWNvbXBhbnlzLWFzc2V0LWtleXMiIH0gXSwgInR5cGUiOiAiR2xvYmFsUmVmZXJlbmNlIiB9IH0&assetIds=eyAibmFtZSI6ICJzb21lLW90aGVyLWFzc2V0LWlkIiwgInZhbHVlIjogIjEyMzQ1QUJDIiwgImV4dGVybmFsU3ViamVjdElkIjogeyAia2V5cyI6IFsgeyAidHlwZSI6ICJHbG9iYWxSZWZlcmVuY2UiLCAidmFsdWUiOiAiaHR0cDovL215LW93bi1jb21wYW55LmNvbS9rZXlzIiB9IF0sICJ0eXBlIjogIkdsb2JhbFJlZmVyZW5jZSIgfSB9']),
                        ('idShort', 'id_short_example'),
                        ('limit', 56),
                        ('cursor', 'cursor_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_asset_administration_shells_reference(self):
        """Test case for get_all_asset_administration_shells_reference

        Returns References to all Asset Administration Shells
        """
        query_string = [('assetIds', ['?assetIds=eyAibmFtZSI6ICJzb21lLWFzc2V0LWlkIiwgInZhbHVlIjogImh0dHA6Ly9leGFtcGxlLWNvbXBhbnkuY29tL215QXNzZXQiLCAiZXh0ZXJuYWxTdWJqZWN0SWQiOiB7ICJrZXlzIjogWyB7ICJ0eXBlIjogIkdsb2JhbFJlZmVyZW5jZSIsICJ2YWx1ZSI6ICJodHRwOi8vZXhhbXBsZS1jb21wYW55LmNvbS9leGFtcGxlLWNvbXBhbnlzLWFzc2V0LWtleXMiIH0gXSwgInR5cGUiOiAiR2xvYmFsUmVmZXJlbmNlIiB9IH0&assetIds=eyAibmFtZSI6ICJzb21lLW90aGVyLWFzc2V0LWlkIiwgInZhbHVlIjogIjEyMzQ1QUJDIiwgImV4dGVybmFsU3ViamVjdElkIjogeyAia2V5cyI6IFsgeyAidHlwZSI6ICJHbG9iYWxSZWZlcmVuY2UiLCAidmFsdWUiOiAiaHR0cDovL215LW93bi1jb21wYW55LmNvbS9rZXlzIiB9IF0sICJ0eXBlIjogIkdsb2JhbFJlZmVyZW5jZSIgfSB9']),
                        ('idShort', 'id_short_example'),
                        ('limit', 56),
                        ('cursor', 'cursor_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/$reference',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_aas_repository(self):
        """Test case for get_all_submodel_elements_aas_repository

        Returns all submodel elements including their hierarchy
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_metadata_aas_repository(self):
        """Test case for get_all_submodel_elements_metadata_aas_repository

        Returns all submodel elements including their hierarchy
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/$metadata'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_path_aas_repository(self):
        """Test case for get_all_submodel_elements_path_aas_repository

        Returns all submodel elements including their hierarchy
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/$path'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_reference_aas_repository(self):
        """Test case for get_all_submodel_elements_reference_aas_repository

        Returns all submodel elements as a list of References
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'core')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/$reference'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_value_only_aas_repository(self):
        """Test case for get_all_submodel_elements_value_only_aas_repository

        Returns all submodel elements including their hierarchy in the ValueOnly representation
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/$value'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_references_aas_repository(self):
        """Test case for get_all_submodel_references_aas_repository

        Returns all submodel references
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodel-refs'.format(aas_identifier='aas_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_asset_administration_shell_by_id(self):
        """Test case for get_asset_administration_shell_by_id

        Returns a specific Asset Administration Shell
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}'.format(aas_identifier='aas_identifier_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_asset_administration_shell_by_id_reference_aas_repository(self):
        """Test case for get_asset_administration_shell_by_id_reference_aas_repository

        Returns a specific Asset Administration Shell as a Reference
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/$reference'.format(aas_identifier='aas_identifier_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_asset_information_aas_repository(self):
        """Test case for get_asset_information_aas_repository

        Returns the Asset Information
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/asset-information'.format(aas_identifier='aas_identifier_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_file_by_path_aas_repository(self):
        """Test case for get_file_by_path_aas_repository

        Downloads file content from a specific submodel element from the Submodel at a specified path
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/attachment'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_operation_async_result_aas_repository(self):
        """Test case for get_operation_async_result_aas_repository

        Returns the Operation result of an asynchronous invoked Operation
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/operation-results/{handle_id}'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example', handle_id='handle_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_operation_async_result_value_only_aas_repository(self):
        """Test case for get_operation_async_result_value_only_aas_repository

        Returns the ValueOnly notation of the Operation result of an asynchronous invoked Operation
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/operation-results/{handle_id}/$value'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example', handle_id='handle_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_operation_async_status_aas_repository(self):
        """Test case for get_operation_async_status_aas_repository

        Returns the Operation status of an asynchronous invoked Operation
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/operation-status/{handle_id}'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example', handle_id='handle_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_by_id_aas_repository(self):
        """Test case for get_submodel_by_id_aas_repository

        Returns the Submodel
        """
        query_string = [('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_by_id_metadata_aas_repository(self):
        """Test case for get_submodel_by_id_metadata_aas_repository

        Returns the Submodel's metadata elements
        """
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/$metadata'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_by_id_path_aas_repository(self):
        """Test case for get_submodel_by_id_path_aas_repository

        Returns the Submodel's metadata elements
        """
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/$path'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_by_id_reference_aas_repository(self):
        """Test case for get_submodel_by_id_reference_aas_repository

        Returns the Submodel as a Reference
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/$reference'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_by_id_value_only_aas_repository(self):
        """Test case for get_submodel_by_id_value_only_aas_repository

        Returns the Submodel's ValueOnly representation
        """
        query_string = [('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/$value'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_aas_repository(self):
        """Test case for get_submodel_element_by_path_aas_repository

        Returns a specific submodel element from the Submodel at a specified path
        """
        query_string = [('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_metadata_aas_repository(self):
        """Test case for get_submodel_element_by_path_metadata_aas_repository

        Returns the metadata attributes if a specific submodel element from the Submodel at a specified path
        """
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$metadata'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_path_aas_repository(self):
        """Test case for get_submodel_element_by_path_path_aas_repository

        Returns a specific submodel element from the Submodel at a specified path in the Path notation
        """
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$path'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_reference_aas_repository(self):
        """Test case for get_submodel_element_by_path_reference_aas_repository

        Returns the Reference of a specific submodel element from the Submodel at a specified path
        """
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$reference'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_value_only_aas_repository(self):
        """Test case for get_submodel_element_by_path_value_only_aas_repository

        Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation
        """
        query_string = [('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$value'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_thumbnail_aas_repository(self):
        """Test case for get_thumbnail_aas_repository

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/asset-information/thumbnail'.format(aas_identifier='aas_identifier_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoke_operation_aas_repository(self):
        """Test case for invoke_operation_aas_repository

        Synchronously invokes an Operation at a specified path
        """
        operation_request = {"inputArguments":[{},{}],"inoutputArguments":[{},{}],"clientTimeoutDuration":"clientTimeoutDuration"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/invoke'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(operation_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoke_operation_async_aas_repository(self):
        """Test case for invoke_operation_async_aas_repository

        Asynchronously invokes an Operation at a specified path
        """
        operation_request = {"inputArguments":[{},{}],"inoutputArguments":[{},{}],"clientTimeoutDuration":"clientTimeoutDuration"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/invoke-async'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(operation_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoke_operation_async_value_only_aas_repository(self):
        """Test case for invoke_operation_async_value_only_aas_repository

        Asynchronously invokes an Operation at a specified path
        """
        operation_request_value_only = {"inputArguments":"{}","inoutputArguments":"{}","clientTimeoutDuration":"clientTimeoutDuration"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/invoke-async/$value'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(operation_request_value_only),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoke_operation_value_only_aas_repository(self):
        """Test case for invoke_operation_value_only_aas_repository

        Synchronously invokes an Operation at a specified path
        """
        operation_request_value_only = {"inputArguments":"{}","inoutputArguments":"{}","clientTimeoutDuration":"clientTimeoutDuration"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/invoke/$value'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(operation_request_value_only),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_aas_repository(self):
        """Test case for patch_submodel_aas_repository

        Updates the Submodel
        """
        submodel = null
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_by_id_metadata_aas_repository(self):
        """Test case for patch_submodel_by_id_metadata_aas_repository

        Updates the metadata attributes of the Submodel
        """
        submodel_metadata = null
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/$metadata'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_metadata),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_by_id_value_only_aas_repository(self):
        """Test case for patch_submodel_by_id_value_only_aas_repository

        Updates teh values of the Submodel
        """
        submodel_value = {"submodelElements":[null,null]}
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/$value'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_value),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_element_value_by_path_aas_repository(self):
        """Test case for patch_submodel_element_value_by_path_aas_repository

        Updates an existing submodel element value at a specified path within submodel elements hierarchy
        """
        submodel_element = null
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_element),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_element_value_by_path_metadata(self):
        """Test case for patch_submodel_element_value_by_path_metadata

        Updates the metadata attributes of an existing submodel element value at a specified path within submodel elements hierarchy
        """
        submodel_element_metadata = null
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$metadata'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_element_metadata),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_element_value_by_path_value_only(self):
        """Test case for patch_submodel_element_value_by_path_value_only

        Updates the value of an existing submodel element value at a specified path within submodel elements hierarchy
        """
        submodel_element_value = null
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$value'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_element_value),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_asset_administration_shell(self):
        """Test case for post_asset_administration_shell

        Creates a new Asset Administration Shell
        """
        asset_administration_shell = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells',
            method='POST',
            headers=headers,
            data=json.dumps(asset_administration_shell),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_submodel_element_aas_repository(self):
        """Test case for post_submodel_element_aas_repository

        Creates a new submodel element
        """
        submodel_element = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(submodel_element),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_submodel_element_by_path_aas_repository(self):
        """Test case for post_submodel_element_by_path_aas_repository

        Creates a new submodel element at a specified path within submodel elements hierarchy
        """
        submodel_element = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(submodel_element),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_submodel_reference_aas_repository(self):
        """Test case for post_submodel_reference_aas_repository

        Creates a submodel reference at the Asset Administration Shell
        """
        reference = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodel-refs'.format(aas_identifier='aas_identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(reference),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_asset_administration_shell_by_id(self):
        """Test case for put_asset_administration_shell_by_id

        Updates an existing Asset Administration Shell
        """
        asset_administration_shell = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}'.format(aas_identifier='aas_identifier_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(asset_administration_shell),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_asset_information_aas_repository(self):
        """Test case for put_asset_information_aas_repository

        Updates the Asset Information
        """
        asset_information = {"specificAssetIds":[null,null],"defaultThumbnail":{"path":"path","contentType":"contentType"},"globalAssetId":"globalAssetId","assetType":"assetType"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/asset-information'.format(aas_identifier='aas_identifier_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(asset_information),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_put_file_by_path_aas_repository(self):
        """Test case for put_file_by_path_aas_repository

        Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
        }
        data = dict(file_name='file_name_example',
                    file='/path/to/file')
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/attachment'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='PUT',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_submodel_by_id_aas_repository(self):
        """Test case for put_submodel_by_id_aas_repository

        Updates the Submodel
        """
        submodel = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(submodel),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_submodel_element_by_path_aas_repository(self):
        """Test case for put_submodel_element_by_path_aas_repository

        Updates an existing submodel element at a specified path within submodel elements hierarchy
        """
        submodel_element = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/submodels/{submodel_identifier}/submodel-elements/{id_short_path}'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(submodel_element),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_put_thumbnail_aas_repository(self):
        """Test case for put_thumbnail_aas_repository

        
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
        }
        data = dict(file_name='file_name_example',
                    file='/path/to/file')
        response = self.client.open(
            '/api/v3.0/shells/{aas_identifier}/asset-information/thumbnail'.format(aas_identifier='aas_identifier_example'),
            method='PUT',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
