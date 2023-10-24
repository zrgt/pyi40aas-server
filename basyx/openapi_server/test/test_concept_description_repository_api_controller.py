import unittest

from flask import json

from ..models.concept_description import ConceptDescription  # noqa: E501
from ..models.get_concept_descriptions_result import GetConceptDescriptionsResult  # noqa: E501
from ..models.result import Result  # noqa: E501
from ..test import BaseTestCase


class TestConceptDescriptionRepositoryAPIController(BaseTestCase):
    """ConceptDescriptionRepositoryAPIController integration test stubs"""

    def test_delete_concept_description_by_id(self):
        """Test case for delete_concept_description_by_id

        Deletes a Concept Description
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/concept-descriptions/{cd_identifier}'.format(cd_identifier='cd_identifier_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_concept_descriptions(self):
        """Test case for get_all_concept_descriptions

        Returns all Concept Descriptions
        """
        query_string = [('idShort', 'id_short_example'),
                        ('isCaseOf', 'is_case_of_example'),
                        ('dataSpecificationRef', 'data_specification_ref_example'),
                        ('limit', 56),
                        ('cursor', 'cursor_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/concept-descriptions',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_concept_description_by_id(self):
        """Test case for get_concept_description_by_id

        Returns a specific Concept Description
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/concept-descriptions/{cd_identifier}'.format(cd_identifier='cd_identifier_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_concept_description(self):
        """Test case for post_concept_description

        Creates a new Concept Description
        """
        concept_description = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/concept-descriptions',
            method='POST',
            headers=headers,
            data=json.dumps(concept_description),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_concept_description_by_id(self):
        """Test case for put_concept_description_by_id

        Updates an existing Concept Description
        """
        concept_description = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3.0/concept-descriptions/{cd_identifier}'.format(cd_identifier='cd_identifier_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(concept_description),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
