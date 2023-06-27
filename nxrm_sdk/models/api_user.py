"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiUser:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'user_id': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email_address': 'str',
        'source': 'str',
        'status': 'str',
        'read_only': 'bool',
        'roles': 'list[str]',
        'external_roles': 'list[str]',
    }

    attribute_map = {
        'user_id': 'userId',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email_address': 'emailAddress',
        'source': 'source',
        'status': 'status',
        'read_only': 'readOnly',
        'roles': 'roles',
        'external_roles': 'externalRoles',
    }

    def __init__(
        self,
        user_id=None,
        first_name=None,
        last_name=None,
        email_address=None,
        source=None,
        status=None,
        read_only=None,
        roles=None,
        external_roles=None,
    ):  # noqa: E501
        """ApiUser - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._first_name = None
        self._last_name = None
        self._email_address = None
        self._source = None
        self._status = None
        self._read_only = None
        self._roles = None
        self._external_roles = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email_address is not None:
            self.email_address = email_address
        if source is not None:
            self.source = source
        self.status = status
        if read_only is not None:
            self.read_only = read_only
        if roles is not None:
            self.roles = roles
        if external_roles is not None:
            self.external_roles = external_roles

    @property
    def user_id(self):
        """Gets the user_id of this ApiUser.  # noqa: E501

        The userid which is required for login. This value cannot be changed.  # noqa: E501

        :return: The user_id of this ApiUser.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ApiUser.

        The userid which is required for login. This value cannot be changed.  # noqa: E501

        :param user_id: The user_id of this ApiUser.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def first_name(self):
        """Gets the first_name of this ApiUser.  # noqa: E501

        The first name of the user.  # noqa: E501

        :return: The first_name of this ApiUser.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ApiUser.

        The first name of the user.  # noqa: E501

        :param first_name: The first_name of this ApiUser.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this ApiUser.  # noqa: E501

        The last name of the user.  # noqa: E501

        :return: The last_name of this ApiUser.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ApiUser.

        The last name of the user.  # noqa: E501

        :param last_name: The last_name of this ApiUser.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email_address(self):
        """Gets the email_address of this ApiUser.  # noqa: E501

        The email address associated with the user.  # noqa: E501

        :return: The email_address of this ApiUser.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this ApiUser.

        The email address associated with the user.  # noqa: E501

        :param email_address: The email_address of this ApiUser.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def source(self):
        """Gets the source of this ApiUser.  # noqa: E501

        The user source which is the origin of this user. This value cannot be changed.  # noqa: E501

        :return: The source of this ApiUser.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ApiUser.

        The user source which is the origin of this user. This value cannot be changed.  # noqa: E501

        :param source: The source of this ApiUser.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def status(self):
        """Gets the status of this ApiUser.  # noqa: E501

        The user's status, e.g. active or disabled.  # noqa: E501

        :return: The status of this ApiUser.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiUser.

        The user's status, e.g. active or disabled.  # noqa: E501

        :param status: The status of this ApiUser.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError(
                'Invalid value for `status`, must not be `None`'
            )  # noqa: E501
        allowed_values = [
            'active',
            'locked',
            'disabled',
            'changepassword',
        ]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                'Invalid value for `status` ({}), must be one of {}'.format(  # noqa: E501
                    status, allowed_values
                )
            )

        self._status = status

    @property
    def read_only(self):
        """Gets the read_only of this ApiUser.  # noqa: E501

        Indicates whether the user's properties could be modified by the Nexus Repository Manager. When false only roles are considered during update.  # noqa: E501

        :return: The read_only of this ApiUser.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this ApiUser.

        Indicates whether the user's properties could be modified by the Nexus Repository Manager. When false only roles are considered during update.  # noqa: E501

        :param read_only: The read_only of this ApiUser.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def roles(self):
        """Gets the roles of this ApiUser.  # noqa: E501

        The roles which the user has been assigned within Nexus.  # noqa: E501

        :return: The roles of this ApiUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this ApiUser.

        The roles which the user has been assigned within Nexus.  # noqa: E501

        :param roles: The roles of this ApiUser.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def external_roles(self):
        """Gets the external_roles of this ApiUser.  # noqa: E501

        The roles which the user has been assigned in an external source, e.g. LDAP group. These cannot be changed within the Nexus Repository Manager.  # noqa: E501

        :return: The external_roles of this ApiUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_roles

    @external_roles.setter
    def external_roles(self, external_roles):
        """Sets the external_roles of this ApiUser.

        The roles which the user has been assigned in an external source, e.g. LDAP group. These cannot be changed within the Nexus Repository Manager.  # noqa: E501

        :param external_roles: The external_roles of this ApiUser.  # noqa: E501
        :type: list[str]
        """

        self._external_roles = external_roles

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, 'to_dict') else x, value)
                )
            elif hasattr(value, 'to_dict'):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], 'to_dict')
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(ApiUser, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
