import unittest

from flask import json

from openapi_server.models.base_operation_result import BaseOperationResult  # noqa: E501
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


class TestSubmodelAPIController(BaseTestCase):
    """SubmodelAPIController integration test stubs"""

    def test_delete_file_by_path(self):
        """Test case for delete_file_by_path

        Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}/attachment'.format(id_short_path='id_short_path_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_submodel_element_by_path(self):
        """Test case for delete_submodel_element_by_path

        Deletes a submodel element at a specified path within the submodel elements hierarchy
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}'.format(id_short_path='id_short_path_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements(self):
        """Test case for get_all_submodel_elements

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
            '/api/v3.0/submodel/submodel-elements',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_metadata(self):
        """Test case for get_all_submodel_elements_metadata

        Returns the metadata attributes of all submodel elements including their hierarchy
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/$metadata',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_path(self):
        """Test case for get_all_submodel_elements_path

        Returns all submodel elements including their hierarchy in the Path notation
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/$path',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_reference(self):
        """Test case for get_all_submodel_elements_reference

        Returns the References of all submodel elements
        """
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'core')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/$reference',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submodel_elements_value_only(self):
        """Test case for get_all_submodel_elements_value_only

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
            '/api/v3.0/submodel/submodel-elements/$value',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_file_by_path(self):
        """Test case for get_file_by_path

        Downloads file content from a specific submodel element from the Submodel at a specified path
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}/attachment'.format(id_short_path='id_short_path_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_operation_async_result(self):
        """Test case for get_operation_async_result

        Returns the Operation result of an asynchronous invoked Operation
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}/operation-results/{handle_id}'.format(id_short_path='id_short_path_example', handle_id='handle_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_operation_async_result_value_only(self):
        """Test case for get_operation_async_result_value_only

        Returns the value of the Operation result of an asynchronous invoked Operation
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}/operation-results/{handle_id}/$value'.format(id_short_path='id_short_path_example', handle_id='handle_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_operation_async_status(self):
        """Test case for get_operation_async_status

        Returns the Operation status of an asynchronous invoked Operation
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}/operation-status/{handle_id}'.format(id_short_path='id_short_path_example', handle_id='handle_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel(self):
        """Test case for get_submodel

        Returns the Submodel
        """
        query_string = [('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path(self):
        """Test case for get_submodel_element_by_path

        Returns a specific submodel element from the Submodel at a specified path
        """
        query_string = [('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}'.format(id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_metadata(self):
        """Test case for get_submodel_element_by_path_metadata

        Returns the matadata attributes of a specific submodel element from the Submodel at a specified path
        """
        query_string = [('cursor', 'cursor_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}/$metadata'.format(id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_path(self):
        """Test case for get_submodel_element_by_path_path

        Returns a specific submodel element from the Submodel at a specified path in the Path notation
        """
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}/$path'.format(id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_reference(self):
        """Test case for get_submodel_element_by_path_reference

        Returns the Referene of a specific submodel element from the Submodel at a specified path
        """
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}/$reference'.format(id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_element_by_path_value_only(self):
        """Test case for get_submodel_element_by_path_value_only

        Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation
        """
        query_string = [('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}/$value'.format(id_short_path='id_short_path_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_metadata(self):
        """Test case for get_submodel_metadata

        Returns the metadata attributes of a specific Submodel
        """
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/$metadata',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_path(self):
        """Test case for get_submodel_path

        Returns the Submodel in the Path notation
        """
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/$path',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_reference(self):
        """Test case for get_submodel_reference

        Returns the Reference of the Submodel
        """
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/$reference',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submodel_value_only(self):
        """Test case for get_submodel_value_only

        Returns the Submodel in the ValueOnly representation
        """
        query_string = [('level', 'deep'),
                        ('extent', 'withoutBlobValue')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/$value',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoke_operation(self):
        """Test case for invoke_operation

        Synchronously invokes an Operation at a specified path
        """
        operation_request = {"inputArguments":[{},{}],"inoutputArguments":[{},{}],"clientTimeoutDuration":"clientTimeoutDuration"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}/invoke'.format(id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(operation_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoke_operation_async(self):
        """Test case for invoke_operation_async

        Asynchronously invokes an Operation at a specified path
        """
        operation_request = {"inputArguments":[{},{}],"inoutputArguments":[{},{}],"clientTimeoutDuration":"clientTimeoutDuration"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}/invoke-async'.format(id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(operation_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoke_operation_async_value_only(self):
        """Test case for invoke_operation_async_value_only

        Asynchronously invokes an Operation at a specified path
        """
        operation_request_value_only = {"inputArguments":"{}","inoutputArguments":"{}","clientTimeoutDuration":"clientTimeoutDuration"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}/invoke-async/$value'.format(id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(operation_request_value_only),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoke_operation_sync_value_only(self):
        """Test case for invoke_operation_sync_value_only

        Synchronously invokes an Operation at a specified path
        """
        operation_request_value_only = {"inputArguments":"{}","inoutputArguments":"{}","clientTimeoutDuration":"clientTimeoutDuration"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}/invoke/$value'.format(id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(operation_request_value_only),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel(self):
        """Test case for patch_submodel

        Updates the Submodel
        """
        submodel = null
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel',
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_element_by_path(self):
        """Test case for patch_submodel_element_by_path

        Updates an existing SubmodelElement
        """
        submodel_element = null
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}'.format(id_short_path='id_short_path_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_element),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_element_by_path_metadata(self):
        """Test case for patch_submodel_element_by_path_metadata

        Updates the metadata attributes an existing SubmodelElement
        """
        get_submodel_elements_metadata_result = null
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}/$metadata'.format(id_short_path='id_short_path_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(get_submodel_elements_metadata_result),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_element_by_path_value_only(self):
        """Test case for patch_submodel_element_by_path_value_only

        Updates the value of an existing SubmodelElement
        """
        get_submodel_elements_value_result = null
        query_string = [('limit', 56),
                        ('cursor', 'cursor_example'),
                        ('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}/$value'.format(id_short_path='id_short_path_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(get_submodel_elements_value_result),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_metadata(self):
        """Test case for patch_submodel_metadata

        Updates the metadata attributes of the Submodel
        """
        submodel_metadata = null
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/$metadata',
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_metadata),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_submodel_value_only(self):
        """Test case for patch_submodel_value_only

        Updates the values of the Submodel
        """
        submodel_value = {"submodelElements":[null,null]}
        query_string = [('level', 'core')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/$value',
            method='PATCH',
            headers=headers,
            data=json.dumps(submodel_value),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_submodel_element(self):
        """Test case for post_submodel_element

        Creates a new submodel element
        """
        submodel_element = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements',
            method='POST',
            headers=headers,
            data=json.dumps(submodel_element),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_submodel_element_by_path(self):
        """Test case for post_submodel_element_by_path

        Creates a new submodel element at a specified path within submodel elements hierarchy
        """
        submodel_element = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}'.format(id_short_path='id_short_path_example'),
            method='POST',
            headers=headers,
            data=json.dumps(submodel_element),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_put_file_by_path(self):
        """Test case for put_file_by_path

        Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
        }
        data = dict(file_name='file_name_example',
                    file='/path/to/file')
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}/attachment'.format(id_short_path='id_short_path_example'),
            method='PUT',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_submodel(self):
        """Test case for put_submodel

        Updates the Submodel
        """
        submodel = null
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel',
            method='PUT',
            headers=headers,
            data=json.dumps(submodel),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_submodel_element_by_path(self):
        """Test case for put_submodel_element_by_path

        Updates an existing submodel element at a specified path within submodel elements hierarchy
        """
        submodel_element = null
        query_string = [('level', 'deep')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/submodel/submodel-elements/{id_short_path}'.format(id_short_path='id_short_path_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(submodel_element),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
