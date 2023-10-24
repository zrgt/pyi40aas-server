import unittest

from flask import json

from ..models.get_package_descriptions_result import GetPackageDescriptionsResult  # noqa: E501
from ..models.package_description import PackageDescription  # noqa: E501
from ..models.result import Result  # noqa: E501
from ..test import BaseTestCase


class TestAASXFileServerAPIController(BaseTestCase):
    """AASXFileServerAPIController integration test stubs"""

    def test_delete_aasxby_package_id(self):
        """Test case for delete_aasxby_package_id

        Deletes a specific AASX package from the server
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/packages/{package_id}'.format(package_id='package_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_aasxby_package_id(self):
        """Test case for get_aasxby_package_id

        Returns a specific AASX package from the server
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/packages/{package_id}'.format(package_id='package_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_aasx_package_ids(self):
        """Test case for get_all_aasx_package_ids

        Returns a list of available AASX packages at the server
        """
        query_string = [('aasId', 'aas_id_example'),
                        ('limit', 56),
                        ('cursor', 'cursor_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/packages',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_post_aasx_package(self):
        """Test case for post_aasx_package

        Stores the AASX package at the server
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
        }
        data = dict(aas_ids=['aas_ids_example'],
                    file='/path/to/file',
                    file_name='file_name_example')
        response = self.client.open(
            '/api/v3.0/packages',
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_put_aasxby_package_id(self):
        """Test case for put_aasxby_package_id

        Updates the AASX package at the server
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
        }
        data = dict(aas_ids=['aas_ids_example'],
                    file='/path/to/file',
                    file_name='file_name_example')
        response = self.client.open(
            '/api/v3.0/packages/{package_id}'.format(package_id='package_id_example'),
            method='PUT',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
