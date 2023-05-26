# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import nexus_sdk
from nexus_sdk import api_client, configuration, schemas
from nexus_sdk.paths.v1_security_privileges_repository_content_selector_privilege_name import (  # noqa: E501
    put,
)

from .. import ApiTestMixin


class TestV1SecurityPrivilegesRepositoryContentSelectorPrivilegeName(
    ApiTestMixin, unittest.TestCase
):
    """
    V1SecurityPrivilegesRepositoryContentSelectorPrivilegeName unit test stubs
        Update a repository content selector type privilege.  # noqa: E501
    """

    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 400


if __name__ == "__main__":
    unittest.main()
