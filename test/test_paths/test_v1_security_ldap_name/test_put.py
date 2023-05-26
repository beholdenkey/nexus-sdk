# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import nexus_sdk
from nexus_sdk.paths.v1_security_ldap_name import put  # noqa: E501
from nexus_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1SecurityLdapName(ApiTestMixin, unittest.TestCase):
    """
    V1SecurityLdapName unit test stubs
        Update LDAP server  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204


if __name__ == '__main__':
    unittest.main()