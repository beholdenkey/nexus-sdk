# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import nexus_sdk
from nexus_sdk.paths.v1_status_writable import get  # noqa: E501
from nexus_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1StatusWritable(ApiTestMixin, unittest.TestCase):
    """
    V1StatusWritable unit test stubs
        Health check endpoint that validates server can respond to read and write requests  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200


if __name__ == '__main__':
    unittest.main()
