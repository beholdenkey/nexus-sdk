# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import nexus_sdk
from nexus_sdk import api_client, configuration, schemas
from nexus_sdk.paths.v1_security_privileges_privilege_name import delete  # noqa: E501

from .. import ApiTestMixin


class TestV1SecurityPrivilegesPrivilegeName(ApiTestMixin, unittest.TestCase):
    """
    V1SecurityPrivilegesPrivilegeName unit test stubs
        Delete a privilege by name.  # noqa: E501
    """

    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 400


if __name__ == "__main__":
    unittest.main()
