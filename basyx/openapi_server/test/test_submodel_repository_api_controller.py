import unittest

from flask import json

from ..models.get_path_items_result import GetPathItemsResult  # noqa: E501
from ..models.get_references_result import GetReferencesResult  # noqa: E501
from ..models.get_submodel_elements_metadata_result import GetSubmodelElementsMetadataResult  # noqa: E501
from ..models.get_submodel_elements_result import GetSubmodelElementsResult  # noqa: E501
from ..models.get_submodel_elements_value_result import GetSubmodelElementsValueResult  # noqa: E501
from ..models.get_submodels_metadata_result import GetSubmodelsMetadataResult  # noqa: E501
from ..models.get_submodels_result import GetSubmodelsResult  # noqa: E501
from ..models.get_submodels_value_result import GetSubmodelsValueResult  # noqa: E501
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


class TestSubmodelRepositoryAPIController(BaseTestCase):
    """SubmodelRepositoryAPIController integration test stubs"""

    def test_delete_file_by_path_submodel_repo(self):
        """Test case for delete_file_by_path_submodel_repo

        Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/attachment'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_submodel_by_id(self):
        """Test case for delete_submodel_by_id

        Deletes a Submodel
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}'.format(submodel_identifier='submodel_identifier_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_submodel_element_by_path_submodel_repo(self):
        """Test case for delete_submodel_element_by_path_submodel_repo

        Deletes a submodel element at a specified path within the submodel elements hierarchy
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_metadata_submodel_repository(self):
        """Test case for get_all_submodel_elements_metadata_submodel_repository

        Returns the metadata attributes of all submodel elements including their hierarchy
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/$metadata'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_path_submodel_repo(self):
        """Test case for get_all_submodel_elements_path_submodel_repo

        Returns all submodel elements including their hierarchy in the Path notation
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/$path'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_reference_submodel_repo(self):
        """Test case for get_all_submodel_elements_reference_submodel_repo

        Returns the References of all submodel elements
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'core')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/$reference'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_submodel_repository(self):
        """Test case for get_all_submodel_elements_submodel_repository

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
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_value_only_submodel_repo(self):
        """Test case for get_all_submodel_elements_value_only_submodel_repo

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
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/$value'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodels(self):
        """Test case for get_all_submodels

        Returns all Submodels
        """
        query_string = [('semanticId', 'semantic_id_example'),
                        ('idShort', 'id_short_example'),
                        ('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodels_metadata(self):
        """Test case for get_all_submodels_metadata

        Returns the metadata attributes of all Submodels
        """
        query_string = [('semanticId', 'semantic_id_example'),
                        ('idShort', 'id_short_example'),
                        ('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/$metadata',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodels_path(self):
        """Test case for get_all_submodels_path

        Returns all Submodels in the Path notation
        """
        query_string = [('semanticId', 'semantic_id_example'),
                        ('idShort', 'id_short_example'),
                        ('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/$path',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodels_reference(self):
        """Test case for get_all_submodels_reference

        Returns the References for all Submodels
        """
        query_string = [('semanticId', 'semantic_id_example'),
                        ('idShort', 'id_short_example'),
                        ('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'core')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/$reference',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodels_value_only(self):
        """Test case for get_all_submodels_value_only

        Returns all Submodels in their ValueOnly representation
        """
        query_string = [('semanticId', 'semantic_id_example'),
                        ('idShort', 'id_short_example'),
                        ('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/$value',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_file_by_path_submodel_repo(self):
        """Test case for get_file_by_path_submodel_repo

        Downloads file content from a specific submodel element from the Submodel at a specified path
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/attachment'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_operation_async_result_submodel_repo(self):
        """Test case for get_operation_async_result_submodel_repo

        Returns the Operation result of an asynchronous invoked Operation
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/operation-results/{handle_id}'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example', handle_id='handle_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_operation_async_result_value_only_submodel_repo(self):
        """Test case for get_operation_async_result_value_only_submodel_repo

        Returns the Operation result of an asynchronous invoked Operation
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/operation-results/{handle_id}/$value'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example', handle_id='handle_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_operation_async_status_submodel_repo(self):
        """Test case for get_operation_async_status_submodel_repo

        Returns the Operation status of an asynchronous invoked Operation
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/operation-status/{handle_id}'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example', handle_id='handle_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_by_id(self):
        """Test case for get_submodel_by_id

        Returns a specific Submodel
        """
        query_string = [('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_by_id_metadata(self):
        """Test case for get_submodel_by_id_metadata

        Returns the metadata attributes of a specific Submodel
        """
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/$metadata'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_by_id_path(self):
        """Test case for get_submodel_by_id_path

        Returns a specific Submodel in the Path notation
        """
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/$path'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_by_id_reference(self):
        """Test case for get_submodel_by_id_reference

        Returns the Reference of a specific Submodel
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/$reference'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_by_id_value_only(self):
        """Test case for get_submodel_by_id_value_only

        Returns a specific Submodel in the ValueOnly representation
        """
        query_string = [('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/$value'.format(submodel_identifier='submodel_identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_metadata_submodel_repo(self):
        """Test case for get_submodel_element_by_path_metadata_submodel_repo

        Returns the matadata attributes of a specific submodel element from the Submodel at a specified path
        """
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$metadata'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_path_submodel_repo(self):
        """Test case for get_submodel_element_by_path_path_submodel_repo

        Returns a specific submodel element from the Submodel at a specified path in the Path notation
        """
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$path'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_reference_submodel_repo(self):
        """Test case for get_submodel_element_by_path_reference_submodel_repo

        Returns the Referene of a specific submodel element from the Submodel at a specified path
        """
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$reference'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_submodel_repo(self):
        """Test case for get_submodel_element_by_path_submodel_repo

        Returns a specific submodel element from the Submodel at a specified path
        """
        query_string = [('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_value_only_submodel_repo(self):
        """Test case for get_submodel_element_by_path_value_only_submodel_repo

        Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation
        """
        query_string = [('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$value'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoke_operation_async_submodel_repo(self):
        """Test case for invoke_operation_async_submodel_repo

        Asynchronously invokes an Operation at a specified path
        """
        operation_request = {"inputArguments":[{},{}],"inoutputArguments":[{},{}],"clientTimeoutDuration":"clientTimeoutDuration"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/invoke-async'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(operation_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoke_operation_async_value_only_submodel_repo(self):
        """Test case for invoke_operation_async_value_only_submodel_repo

        Asynchronously invokes an Operation at a specified path
        """
        operation_request_value_only = {"inputArguments":"{}","inoutputArguments":"{}","clientTimeoutDuration":"clientTimeoutDuration"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/invoke-async/$value'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(operation_request_value_only),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoke_operation_submodel_repo(self):
        """Test case for invoke_operation_submodel_repo

        Synchronously invokes an Operation at a specified path
        """
        operation_request = {"inputArguments":[{},{}],"inoutputArguments":[{},{}],"clientTimeoutDuration":"clientTimeoutDuration"}
        query_string = [('async', False)]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/invoke'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(operation_request),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoke_operation_value_only_submodel_repo(self):
        """Test case for invoke_operation_value_only_submodel_repo

        Synchronously invokes an Operation at a specified path
        """
        operation_request_value_only = {"inputArguments":"{}","inoutputArguments":"{}","clientTimeoutDuration":"clientTimeoutDuration"}
        query_string = [('async', False)]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/invoke/$value'.format(aas_identifier='aas_identifier_example', submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(operation_request_value_only),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_by_id(self):
        """Test case for patch_submodel_by_id

        Updates an existing Submodel
        """
        submodel = null
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}'.format(submodel_identifier='submodel_identifier_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_by_id_metadata(self):
        """Test case for patch_submodel_by_id_metadata

        Updates the metadata attributes of an existing Submodel
        """
        submodel_metadata = null
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/$metadata'.format(submodel_identifier='submodel_identifier_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_metadata),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_by_id_value_only(self):
        """Test case for patch_submodel_by_id_value_only

        Updates the values of an existing Submodel
        """
        submodel_value = {"submodelElements":[null,null]}
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/$value'.format(submodel_identifier='submodel_identifier_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_value),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_element_by_path_metadata_submodel_repo(self):
        """Test case for patch_submodel_element_by_path_metadata_submodel_repo

        Updates the metadata attributes an existing SubmodelElement
        """
        submodel_element_metadata = null
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$metadata'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_element_metadata),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_element_by_path_submodel_repo(self):
        """Test case for patch_submodel_element_by_path_submodel_repo

        Updates an existing SubmodelElement
        """
        submodel_element = null
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_element),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_element_by_path_value_only_submodel_repo(self):
        """Test case for patch_submodel_element_by_path_value_only_submodel_repo

        Updates the value of an existing SubmodelElement
        """
        submodel_element_value = null
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/$value'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_element_value),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_submodel(self):
        """Test case for post_submodel

        Creates a new Submodel
        """
        submodel = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels',
            method='POST',
            headers=headers,
            data=json.dumps(submodel),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_submodel_element_by_path_submodel_repo(self):
        """Test case for post_submodel_element_by_path_submodel_repo

        Creates a new submodel element at a specified path within submodel elements hierarchy
        """
        submodel_element = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(submodel_element),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_submodel_element_submodel_repository(self):
        """Test case for post_submodel_element_submodel_repository

        Creates a new submodel element
        """
        submodel_element = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements'.format(submodel_identifier='submodel_identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(submodel_element),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_put_file_by_path_submodel_repo(self):
        """Test case for put_file_by_path_submodel_repo

        Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
        }
        data = dict(file_name='file_name_example',
                    file='/path/to/file')
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/attachment'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='PUT',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_submodel_by_id(self):
        """Test case for put_submodel_by_id

        Updates an existing Submodel
        """
        submodel = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}'.format(submodel_identifier='submodel_identifier_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(submodel),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_submodel_element_by_path_submodel_repo(self):
        """Test case for put_submodel_element_by_path_submodel_repo

        Updates an existing submodel element at a specified path within submodel elements hierarchy
        """
        submodel_element = null
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodels/{submodel_identifier}/submodel-elements/{id_short_path}'.format(submodel_identifier='submodel_identifier_example', id_short_path='id_short_path_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(submodel_element),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
