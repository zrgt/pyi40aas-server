import unittest

from flask import json

from ..models.inline_response200 import InlineResponse200  # noqa: E501
from ..models.result import Result  # noqa: E501
from ..models.specific_asset_id import SpecificAssetId  # noqa: E501
from ..test import BaseTestCase


class TestAssetAdministrationShellBasicDiscoveryAPIController(BaseTestCase):
    """AssetAdministrationShellBasicDiscoveryAPIController integration test stubs"""

    def test_delete_all_asset_links_by_id(self):
        """Test case for delete_all_asset_links_by_id

        Deletes all specific Asset identifiers linked to an Asset Administration Shell to edit discoverable content
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/lookup/shells/{aas_identifier}'.format(aas_identifier='aas_identifier_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_asset_administration_shell_ids_by_asset_link(self):
        """Test case for get_all_asset_administration_shell_ids_by_asset_link

        Returns a list of Asset Administration Shell ids linked to specific Asset identifiers
        """
        query_string = [('assetIds', ['?assetIds=eyAibmFtZSI6ICJzb21lLWFzc2V0LWlkIiwgInZhbHVlIjogImh0dHA6Ly9leGFtcGxlLWNvbXBhbnkuY29tL215QXNzZXQiLCAiZXh0ZXJuYWxTdWJqZWN0SWQiOiB7ICJrZXlzIjogWyB7ICJ0eXBlIjogIkdsb2JhbFJlZmVyZW5jZSIsICJ2YWx1ZSI6ICJodHRwOi8vZXhhbXBsZS1jb21wYW55LmNvbS9leGFtcGxlLWNvbXBhbnlzLWFzc2V0LWtleXMiIH0gXSwgInR5cGUiOiAiR2xvYmFsUmVmZXJlbmNlIiB9IH0&assetIds=eyAibmFtZSI6ICJzb21lLW90aGVyLWFzc2V0LWlkIiwgInZhbHVlIjogIjEyMzQ1QUJDIiwgImV4dGVybmFsU3ViamVjdElkIjogeyAia2V5cyI6IFsgeyAidHlwZSI6ICJHbG9iYWxSZWZlcmVuY2UiLCAidmFsdWUiOiAiaHR0cDovL215LW93bi1jb21wYW55LmNvbS9rZXlzIiB9IF0sICJ0eXBlIjogIkdsb2JhbFJlZmVyZW5jZSIgfSB9']),
                        ('limit', 56),
                        ('cursor', 'cursor_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/lookup/shells',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_asset_links_by_id(self):
        """Test case for get_all_asset_links_by_id

        Returns a list of specific Asset identifiers based on an Asset Administration Shell id to edit discoverable content
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/lookup/shells/{aas_identifier}'.format(aas_identifier='aas_identifier_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_all_asset_links_by_id(self):
        """Test case for post_all_asset_links_by_id

        Creates specific Asset identifiers linked to an Asset Administration Shell to edit discoverable content
        """
        specific_asset_id = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/lookup/shells/{aas_identifier}'.format(aas_identifier='aas_identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(specific_asset_id),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
