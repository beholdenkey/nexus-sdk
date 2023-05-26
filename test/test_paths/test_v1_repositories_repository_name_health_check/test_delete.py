# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import nexus_sdk
from nexus_sdk.paths.v1_repositories_repository_name_health_check import delete  # noqa: E501
from nexus_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1RepositoriesRepositoryNameHealthCheck(ApiTestMixin, unittest.TestCase):
    """
    V1RepositoriesRepositoryNameHealthCheck unit test stubs
        Disable repository health check. Proxy repositories only.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204


if __name__ == '__main__':
    unittest.main()
