"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import unittest

import nxrm_sdk
from nxrm_sdk.api.security_management_users_api import (  # noqa: E501
    SecurityManagementUsersApi,
)
from nxrm_sdk.rest import ApiException


class TestSecurityManagementUsersApi(unittest.TestCase):
    """SecurityManagementUsersApi unit test stubs"""

    def setUp(self):
        self.api = SecurityManagementUsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_password(self):
        """Test case for change_password

        Change a user's password.  # noqa: E501
        """
        pass

    def test_create_user(self):
        """Test case for create_user

        Create a new user in the default source.  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete a user.  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        Retrieve a list of users. Note if the source is not 'default' the response is limited to 100 users.  # noqa: E501
        """
        pass

    def test_reset(self):
        """Test case for reset

        Reset the user token for the given user.  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Update an existing user.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
