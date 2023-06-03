# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GroupDeployAttributes(object):
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
        'member_names': 'list[str]',
        'writable_member': 'str'
    }

    attribute_map = {
        'member_names': 'memberNames',
        'writable_member': 'writableMember'
    }

    def __init__(self, member_names=None, writable_member=None):  # noqa: E501
        """GroupDeployAttributes - a model defined in Swagger"""  # noqa: E501
        self._member_names = None
        self._writable_member = None
        self.discriminator = None
        if member_names is not None:
            self.member_names = member_names
        if writable_member is not None:
            self.writable_member = writable_member

    @property
    def member_names(self):
        """Gets the member_names of this GroupDeployAttributes.  # noqa: E501

        Member repositories' names  # noqa: E501

        :return: The member_names of this GroupDeployAttributes.  # noqa: E501
        :rtype: list[str]
        """
        return self._member_names

    @member_names.setter
    def member_names(self, member_names):
        """Sets the member_names of this GroupDeployAttributes.

        Member repositories' names  # noqa: E501

        :param member_names: The member_names of this GroupDeployAttributes.  # noqa: E501
        :type: list[str]
        """

        self._member_names = member_names

    @property
    def writable_member(self):
        """Gets the writable_member of this GroupDeployAttributes.  # noqa: E501

        Pro-only: This field is for the Group Deployment feature available in NXRM Pro.  # noqa: E501

        :return: The writable_member of this GroupDeployAttributes.  # noqa: E501
        :rtype: str
        """
        return self._writable_member

    @writable_member.setter
    def writable_member(self, writable_member):
        """Sets the writable_member of this GroupDeployAttributes.

        Pro-only: This field is for the Group Deployment feature available in NXRM Pro.  # noqa: E501

        :param writable_member: The writable_member of this GroupDeployAttributes.  # noqa: E501
        :type: str
        """

        self._writable_member = writable_member

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GroupDeployAttributes, dict):
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
        if not isinstance(other, GroupDeployAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other