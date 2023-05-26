# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import nexus_sdk
from nexus_sdk.paths.v1_repositories_docker_group import post  # noqa: E501
from nexus_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1RepositoriesDockerGroup(ApiTestMixin, unittest.TestCase):
    """
    V1RepositoriesDockerGroup unit test stubs
        Create Docker group repository  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 201


if __name__ == '__main__':
    unittest.main()
