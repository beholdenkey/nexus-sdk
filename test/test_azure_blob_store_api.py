"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import unittest

import nxrm_sdk
from nxrm_sdk.api.azure_blob_store_api import AzureBlobStoreApi  # noqa: E501
from nxrm_sdk.rest import ApiException


class TestAzureBlobStoreApi(unittest.TestCase):
    """AzureBlobStoreApi unit test stubs"""

    def setUp(self):
        self.api = AzureBlobStoreApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_verify_connection2(self):
        """Test case for verify_connection2

        Verify connection using supplied Azure Blob Store settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
