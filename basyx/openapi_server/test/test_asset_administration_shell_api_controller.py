import unittest

from flask import json

from ..models.asset_administration_shell import AssetAdministrationShell  # noqa: E501
from ..models.asset_information import AssetInformation  # noqa: E501
from ..models.base_operation_result import BaseOperationResult  # noqa: E501
from ..models.get_path_items_result import GetPathItemsResult  # noqa: E501
from ..models.get_references_result import GetReferencesResult  # noqa: E501
from ..models.get_submodel_elements_metadata_result import GetSubmodelElementsMetadataResult  # noqa: E501
from ..models.get_submodel_elements_result import GetSubmodelElementsResult  # noqa: E501
from ..models.get_submodel_elements_value_result import GetSubmodelElementsValueResult  # noqa: E501
from ..models.operation_request import OperationRequest  # noqa: E501
from ..models.operation_request_value_only import OperationRequestValueOnly  # noqa: E501
from ..models.operation_result import OperationResult  # noqa: E501
from ..models.operation_result_value_only import OperationResultValueOnly  # noqa: E501
from ..models.reference import Reference  # noqa: E501
from ..models.result import Result  # noqa: E501
from ..models.submodel import Submodel  # noqa: E501
from ..models.submodel_element import SubmodelElement  # noqa: E501
from ..models.submodel_element_metadata import SubmodelElementMetadata  # noqa: E501
from ..models.submodel_element_value import SubmodelElementValue  # noqa: E501
from ..models.submodel_metadata import SubmodelMetadata  # noqa: E501
from ..models.submodel_value import SubmodelValue  # noqa: E501
from ..test import BaseTestCase


class TestAssetAdministrationShellAPIController(BaseTestCase):
    """AssetAdministrationShellAPIController integration test stubs"""

    def test_delete_file_by_path_aas(self):
        """Test case for delete_file_by_path_aas

        Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/attachment'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_submodel_by_id_aas(self):
        """Test case for delete_submodel_by_id_aas

        Deletes the submodel from the Asset Administration Shell.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}'.format(submodel_identifier='submodel_identifier_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_submodel_element_by_path_aas(self):
        """Test case for delete_submodel_element_by_path_aas

        Deletes a submodel element at a specified path within the submodel elements hierarchy
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_submodel_reference_by_id(self):
        """Test case for delete_submodel_reference_by_id

        Deletes the submodel reference from the Asset Administration Shell. Does not delete the submodel itself!
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodel-refs/{submodel_identifier}'.format(submodel_identifier='submodel_identifier_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_thumbnail(self):
        """Test case for delete_thumbnail

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/asset-information/thumbnail',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_aas(self):
        """Test case for get_all_submodel_elements_aas

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
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_metadata_aas(self):
        """Test case for get_all_submodel_elements_metadata_aas

        Returns all submodel elements including their hierarchy
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/$metadata'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_path_aas(self):
        """Test case for get_all_submodel_elements_path_aas

        Returns all submodel elements including their hierarchy
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/$path'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_reference_aas(self):
        """Test case for get_all_submodel_elements_reference_aas

        Returns all submodel elements as a list of References
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'core')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/$reference'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_value_only_aas(self):
        """Test case for get_all_submodel_elements_value_only_aas

        Returns all submodel elements including their hierarchy in the ValueOnly representation
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/$value'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_references(self):
        """Test case for get_all_submodel_references

        Returns all submodel references
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodel-refs',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_asset_administration_shell(self):
        """Test case for get_asset_administration_shell

        Returns a specific Asset Administration Shell
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_asset_administration_shell_reference(self):
        """Test case for get_asset_administration_shell_reference

        Returns a specific Asset Administration Shell as a Reference
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/$reference',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_asset_information(self):
        """Test case for get_asset_information

        Returns the Asset Information
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/asset-information',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_file_by_path_aas(self):
        """Test case for get_file_by_path_aas

        Downloads file content from a specific submodel element from the Submodel at a specified path
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/attachment'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_operation_async_result_aas(self):
        """Test case for get_operation_async_result_aas

        Returns the Operation result of an asynchronous invoked Operation
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/operation-results/{handle_id}'.format(submodel_identifier='submodel_identifier_example', aas_identifier='aas_identifier_example', id_short_path='id_short_path_example', handle_id='handle_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_operation_async_result_value_only_aas(self):
        """Test case for get_operation_async_result_value_only_aas

        Returns the value of the Operation result of an asynchronous invoked Operation
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/operation-results/{handle_id}/$value'.format(submodel_identifier='submodel_identifier_example', aas_identifier='aas_identifier_example', id_short_path='id_short_path_example', handle_id='handle_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_operation_async_status_aas(self):
        """Test case for get_operation_async_status_aas

        Returns the Operation status of an asynchronous invoked Operation
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/operation-status/{handle_id}'.format(submodel_identifier='submodel_identifier_example', aas_identifier='aas_identifier_example', id_short_path='id_short_path_example', handle_id='handle_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_aas(self):
        """Test case for get_submodel_aas

        Returns the Submodel
        """
        query_string = [('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_aas(self):
        """Test case for get_submodel_element_by_path_aas

        Returns a specific submodel element from the Submodel at a specified path
        """
        query_string = [('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_metadata_aas(self):
        """Test case for get_submodel_element_by_path_metadata_aas

        Returns the metadata attributes if a specific submodel element from the Submodel at a specified path
        """
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$metadata'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_path_aas(self):
        """Test case for get_submodel_element_by_path_path_aas

        Returns a specific submodel element from the Submodel at a specified path in the Path notation
        """
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$path'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_reference_aas(self):
        """Test case for get_submodel_element_by_path_reference_aas

        Returns the Reference of a specific submodel element from the Submodel at a specified path in the ValueOnly representation
        """
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$reference'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_value_only_aas(self):
        """Test case for get_submodel_element_by_path_value_only_aas

        Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation
        """
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$value'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_metadata_aas(self):
        """Test case for get_submodel_metadata_aas

        Returns the Submodel's metadata elements
        """
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/$metadata'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_metadata_reference_aas(self):
        """Test case for get_submodel_metadata_reference_aas

        Returns the Submodel as a Reference
        """
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/$reference'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_path_aas(self):
        """Test case for get_submodel_path_aas

        Returns the Submodel's metadata elements
        """
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/$path'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_value_only_aas(self):
        """Test case for get_submodel_value_only_aas

        Returns the Submodel's ValueOnly representation
        """
        query_string = [('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/$value'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_thumbnail(self):
        """Test case for get_thumbnail

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/asset-information/thumbnail',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoke_operation_async_aas(self):
        """Test case for invoke_operation_async_aas

        Synchronously invokes an Operation at a specified path
        """
        operation_request = {"inputArguments":[{},{}],"inoutputArguments":[{},{}],"clientTimeoutDuration":"clientTimeoutDuration"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/invoke-async'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(operation_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoke_operation_async_value_only_aas(self):
        """Test case for invoke_operation_async_value_only_aas

        Asynchronously invokes an Operation at a specified path
        """
        operation_request_value_only = {"inputArguments":"{}","inoutputArguments":"{}","clientTimeoutDuration":"clientTimeoutDuration"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/invoke-asnyc/$value'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(operation_request_value_only),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoke_operation_sync_aas(self):
        """Test case for invoke_operation_sync_aas

        Synchronously invokes an Operation at a specified path
        """
        operation_request = {"inputArguments":[{},{}],"inoutputArguments":[{},{}],"clientTimeoutDuration":"clientTimeoutDuration"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/invoke'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(operation_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoke_operation_sync_value_only_aas(self):
        """Test case for invoke_operation_sync_value_only_aas

        Synchronously invokes an Operation at a specified path
        """
        operation_request_value_only = {"inputArguments":"{}","inoutputArguments":"{}","clientTimeoutDuration":"clientTimeoutDuration"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/invoke/$value'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(operation_request_value_only),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_aas(self):
        """Test case for patch_submodel_aas

        Updates the Submodel
        """
        submodel = null
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}'.format(submodel_identifier='submodel_identifier_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_element_value_by_path_aas(self):
        """Test case for patch_submodel_element_value_by_path_aas

        Updates an existing submodel element value at a specified path within submodel elements hierarchy
        """
        submodel_element = null
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_element),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_element_value_by_path_metadata_aas(self):
        """Test case for patch_submodel_element_value_by_path_metadata_aas

        Updates the metadata attributes of an existing submodel element value at a specified path within submodel elements hierarchy
        """
        submodel_element_metadata = null
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$metadata'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_element_metadata),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_element_value_by_path_value_only_aas(self):
        """Test case for patch_submodel_element_value_by_path_value_only_aas

        Updates the value of an existing submodel element value at a specified path within submodel elements hierarchy
        """
        submodel_element_value = null
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$value'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_element_value),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_metadata_aas(self):
        """Test case for patch_submodel_metadata_aas

        Updates the metadata attributes of the Submodel
        """
        submodel_metadata = null
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/$metadata'.format(submodel_identifier='submodel_identifier_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_metadata),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_value_only_aas(self):
        """Test case for patch_submodel_value_only_aas

        Updates teh values of the Submodel
        """
        submodel_value = {"submodelElements":[null,null]}
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/$value'.format(submodel_identifier='submodel_identifier_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_value),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_submodel_element_aas(self):
        """Test case for post_submodel_element_aas

        Creates a new submodel element
        """
        submodel_element = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements'.format(submodel_identifier='submodel_identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(submodel_element),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_submodel_element_by_path_aas(self):
        """Test case for post_submodel_element_by_path_aas

        Creates a new submodel element at a specified path within submodel elements hierarchy
        """
        submodel_element = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(submodel_element),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_submodel_reference(self):
        """Test case for post_submodel_reference

        Creates a submodel reference at the Asset Administration Shell
        """
        reference = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodel-refs',
            method='POST',
            headers=headers,
            data=json.dumps(reference),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_asset_administration_shell(self):
        """Test case for put_asset_administration_shell

        Updates an existing Asset Administration Shell
        """
        asset_administration_shell = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas',
            method='PUT',
            headers=headers,
            data=json.dumps(asset_administration_shell),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_asset_information(self):
        """Test case for put_asset_information

        Updates the Asset Information
        """
        asset_information = {"specificAssetIds":[null,null],"defaultThumbnail":{"path":"path","contentType":"contentType"},"globalAssetId":"globalAssetId","assetType":"assetType"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/asset-information',
            method='PUT',
            headers=headers,
            data=json.dumps(asset_information),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_put_file_by_path_aas(self):
        """Test case for put_file_by_path_aas

        Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
        }
        data = dict(file_name='file_name_example',
                    file='/path/to/file')
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/attachment'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='PUT',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_submodel_aas(self):
        """Test case for put_submodel_aas

        Updates the Submodel
        """
        submodel = null
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}'.format(submodel_identifier='submodel_identifier_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(submodel),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_submodel_element_by_path_aas(self):
        """Test case for put_submodel_element_by_path_aas

        Updates an existing submodel element at a specified path within submodel elements hierarchy
        """
        submodel_element = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/aas/submodels/{submodel_identifier}/submodel-elements/{id_short_path}'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(submodel_element),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_put_thumbnail(self):
        """Test case for put_thumbnail

        
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
        }
        data = dict(file_name='file_name_example',
                    file='/path/to/file')
        response = self.client.open(
            '/api/v3.0/aas/asset-information/thumbnail',
            method='PUT',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
